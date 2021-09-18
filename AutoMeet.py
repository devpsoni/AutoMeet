"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from time import sleep
import schedule
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


meetCode = {meeting code}
email = {email}
passwd = {password}
exitMeetNum = 30 #will exit meeting when participant number reaches below this
driver = webdriver.Firefox()

driver.get('https://apps.google.com/intl/en-GB/meet/')
sleep(5)

#Login
print("Signing in...")
signupButton = driver.find_element_by_link_text('Sign in')
signupButton.click()
sleep(5)
emailField = driver.find_element_by_id('identifierId') #email
emailField.click()
emailField.send_keys(email)
sleep(1)
signupButton = driver.find_element_by_id('identifierNext')
signupButton.click()
sleep(3)
passwdField = driver.find_element_by_xpath("//input[@name='password']")#password
passwdField.click()
passwdField.send_keys(passwd)
sleep(1)
signupButton = driver.find_element_by_id('passwordNext')
signupButton.click()
print("Signed in!")
sleep(3)

# JOINING CONFERENCE
#Meeting Entrance page
print("Joining the meeting...")
meetingcodeField = driver.find_element_by_id('i3')
meetingcodeField.click()
meetingcodeField.send_keys(meetCode)
sleep(3)
driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d cjtUbb']").click()
print("checkpoint")
sleep(10)
driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac']").click()
print("Joined! or Asked to Join!")
sleep(10)
while True:
    try:
        driver.find_element_by_class_name("uGOf1d")
    except NoSuchElementException:
        print("Wating to be accepted...")
        sleep(2)
        continue
    break

def checkMeetingStatus():
    while True:
        try:
            driver.find_element_by_class_name("uGOf1d")
        except NoSuchElementException:
            print("Wating to be accepted...")
            sleep(2)
            return False
        return True
        break

def getParticipantNum():
    participantNum = driver.find_element_by_class_name("uGOf1d").text
    return int(participantNum)
sleep(5)
print("Started...")
while checkMeetingStatus():
    print(getParticipantNum())
    if getParticipantNum()<=exitMeetNum:
        driver.find_element_by_xpath("//button[@class='VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c jh0Tpd Gt6sbf QQrMi ftJPW']").click()
        sleep(3)
        print("Call Ended!")
        driver.close()
        break
    else:
        sleep(2)
        continue

