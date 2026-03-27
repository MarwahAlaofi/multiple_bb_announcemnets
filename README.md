# Description
This script is used to post the same announcement to multiple course sections in Blackboard (bb Ultra).

---

# What the script does
- Logs into Blackboard automatically  
- Posts the same announcement to all listed courses  
- Ticks the box to send email notifications to students  

---

# How to use?
Clone the project and follow the steps below to get things up and running:

---

## 1. Make sure Python is installed

If not, download it from:  
https://www.python.org/downloads/

---

## 2. Install required packages

Open Terminal (or Command Prompt) and run:

`python -m pip install selenium webdriver-manager python-dotenv`

---

## 3. Set your Blackboard credentials (IMPORTANT)

Create a file named `.env` in the same folder as the script.

Add the following:

BB_USERNAME=your_username  
BB_PASSWORD=your_password  

---

## 4. Add your course section IDs

Create a file named `courses.txt` in the same folder.

Add your course IDs (one per line), for example:

_1648134_1  
_1328373_1  

You can find the course ID in the course URL, e.g.:  
https://lms.taibahu.edu.sa/ultra/courses/_1648134_1/

---

## 5. Run the script

Use the following command:

python post_multiple_announcements.py "announcement subject" "announcement message"

---

### Example usage

`python post_multiple_announcements.py "Regarding Quiz 2" "Dear students, this is to remind you of today's quiz which will be available at 12 pm. All the best!"`

---