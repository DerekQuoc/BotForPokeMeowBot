from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import getpass
import time
import asyncio

class Messenger:
    """Facilitates sending discord messages as a user"""
    email = ""
    password = ""
    driver = 0
    textElement = 0

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # hardcoded to 'pokemon1' in the lam server
        # maybe make this more flexible?
        testServer =  "https://discord.com/channels/734655457037254718/734655532618481674"
        #lamPokemon1 = "https://discord.com/channels/179380913891704832/732764955677556776"
        self.driver.get(testServer)

        try:
            time.sleep(2)
            emailEntry = self.driver.find_element_by_name('email')
            passwordEntry = self.driver.find_element_by_name('password')
        except:
            time.sleep(5)
            emailEntry = self.driver.find_element_by_name('email')
            passwordEntry = self.driver.find_element_by_name('password')

        emailEntry.clear()
        passwordEntry.clear()

        self.setUserInfo()

        emailEntry.send_keys(self.email)
        passwordEntry.send_keys(self.password)
        passwordEntry.send_keys(Keys.RETURN)

        try:
            time.sleep(5)
            self.textElement = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
        except:
            time.sleep(10)
            self.textElement = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')

    def __del__(self):
        self.driver.close()

    def setUserInfo(self):
        # don't want to hardcode our emails and passwords, so just get them from user
        self.email = input("Enter your discord email: ")
        self.password = getpass.getpass("Enter your password: ")


    def send(self, message):
        self.textElement.send_keys(message)
        self.textElement.send_keys(Keys.RETURN)