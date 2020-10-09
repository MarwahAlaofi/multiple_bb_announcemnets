from selenium import webdriver
import sys

# a list of course ids (i.e. section ids)
# ids can be taken from the url of your bb section page
#e.g. https://lms.taibahu.edu.sa/..../collabultra?course_id=[_1328373_1]
COURSE_IDS = ['section_1_id','section_2_id'] # add more sections as needed

# Instructor info
#####################
BB_USERNAME = 'BLACKBOARD_USERNAME'
BB_PASSWORD = 'BLACKBOARD_PASSWORD'

args = sys.argv # command line arguments

driver = webdriver.Chrome()

driver.get('https://lms.taibahu.edu.sa')

# login into bb
bb_cookie_accept = driver.find_element_by_xpath('//*[@id="agree_button"]')
bb_username = driver.find_element_by_xpath('//*[@id="user_id"]')
bb_password = driver.find_element_by_xpath('//*[@id="password"]')
bb_ok = driver.find_element_by_xpath('//*[@id="entry-login"]')

bb_cookie_accept.click()

print("logging into blackboard ...")

# fill in and submit login credintials
bb_username.send_keys(BB_USERNAME)
bb_password.send_keys(BB_PASSWORD)
bb_ok.click()

for id in COURSE_IDS:
    print("posting announcement ...")
    new_announcement_page = 'https://lms.taibahu.edu.sa/webapps/blackboard/execute/announcement?blackboard.platform.security.NonceUtil.nonce=9949fc6a-bb58-46dc-80d3-71191c5fd6bd&method=add&viewChoice=2&editMode=true&tabAction=false&announcementId=&course_id='+id+'&context=course&internalHandle=my_announcements&searchSelect=' + id
    driver.get(new_announcement_page)
    # wait for the page to load
    driver.implicitly_wait(50)
    subject = driver.find_element_by_xpath('//*[@id="subject"]')
    subject.send_keys(args[1])
    msg = driver.find_element_by_xpath('//*[@id="messagetext"]')
    msg.send_keys(args[2])
    send_email = driver.find_element_by_xpath('//*[@id="pushNotify_true"]')
    send_email.click()
    submit_btn = driver.find_element_by_xpath('//*[@id="bottom_Submit"]')
    submit_btn.click()
print("Done!")
