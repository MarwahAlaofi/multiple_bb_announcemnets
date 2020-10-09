# Description
This script is used to post the same announcement to multiple course sections in Blackboard (bb).

# How to use?
Follow the steps below to get things up and running:
1. Download <strong>python</strong>: https://www.python.org/downloads/
2. Add Python directory to the *environment path*
3. Download **selenium** and **pandas** by running the following commands:
<code>python -m pip install selenium </code><br>
<code>python -m pip install pandas</code>
4. **Set** your section IDs in the script.
7. **Run** the script using the following command:<br>
<code>python scriptname.py 'announcement subject' 'announcement body formatted (if needed) using html)'</code> **example:**
<code>python cspost.py 'Regarding Quiz 2' 'Dear students <br> this is to remind you of today's quiz which will be available at 12 pm. All the best! :)'</code><br>
