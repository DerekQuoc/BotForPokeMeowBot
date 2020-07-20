# Test program to see if selenium works
# You should see a google chrome window pop up 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

print("if you can read this, selenium is working")