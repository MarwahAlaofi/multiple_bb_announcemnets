from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

import sys
import os

# a list of course ids (i.e. section ids)
# ids can be taken from the url of your bb section page
# e.g. https://lms.taibahu.edu.sa/ultra/courses/_1648134_1/
# each user should add their course ids into courses.txt (one per line)

def load_course_ids(file_path="courses.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


# Instructor info (loaded securely from .env)
#####################
load_dotenv()

BB_USERNAME = os.getenv("BB_USERNAME")
BB_PASSWORD = os.getenv("BB_PASSWORD")

if not BB_USERNAME or not BB_PASSWORD:
    raise ValueError("Missing Blackboard credentials. Set them in .env file")

# command line arguments
args = sys.argv

if len(args) < 3:
    raise ValueError("Usage: python script.py 'subject' 'message'")

# setup driver (auto-managed)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 20)

# go to login page
driver.get('https://lms.taibahu.edu.sa/')

print("logging into blackboard ...")

# accept cookies if present
try:
    cookie_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="agree_button"]'))
    )
    cookie_btn.click()
except:
    pass  # cookie button may not appear


# login into bb
bb_username = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="user_id"]'))
)
bb_password = driver.find_element(By.XPATH, '//*[@id="password"]')
bb_ok = driver.find_element(By.XPATH, '//*[@id="entry-login"]')

# fill in and submit login credentials
bb_username.send_keys(BB_USERNAME)
bb_password.send_keys(BB_PASSWORD)
bb_ok.click()


# load course ids
COURSE_IDS = load_course_ids()

for course_id in COURSE_IDS:
    print(f"posting announcement for {course_id} ...")

    # Ultra announcement create page
    new_announcement_page = f"https://lms.taibahu.edu.sa/ultra/courses/{course_id}/announcements/announcement-detail?courseId={course_id}&mode=create"
    driver.get(new_announcement_page)

    # wait for subject field (Ultra UI)
    subject = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//input[contains(@placeholder,"announcement title")]')
        )
    )
    subject.click()
    subject.send_keys(args[1])

    msg = wait.until(
        EC.presence_of_element_located((By.ID, "bb-editor-textbox"))
    )
    msg.click()
    msg.send_keys(args[2])

    send_email = wait.until(
        EC.presence_of_element_located((By.ID, "send-email-checkbox"))
    )

    if not send_email.is_selected():
        driver.execute_script("arguments[0].click();", send_email)

    # verify
    wait.until(lambda d: send_email.is_selected())

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Post"]]'))
    )
    submit_btn.click()

print("Done!")
