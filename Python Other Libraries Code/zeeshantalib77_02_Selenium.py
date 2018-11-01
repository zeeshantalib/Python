# take username and password as an input then open facebook in chrome automatically
from selenium import webdriver
from time import sleep

usr=input("Enter Email id: ")
pwd=input("Enter Password: ")

driver=webdriver.chrome()
driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

username_box=driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id Entered")
sleep(1)

password_box=driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password Entered")

login_box=driver.find_element_by_id('loginbutton')
login_box.click();

print("Done")
input("Press any thing to quit")
driver.quit()
print("Finished")
