# #!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = True

# path to firefox
binary = FirefoxBinary('/opt/firefox/firefox')
# path to geckodriver
browser = webdriver.Firefox(capabilities=capabilities, firefox_binary=binary, executable_path='./geckodriver')
browser.get('https://google.com')
browser.quit()
