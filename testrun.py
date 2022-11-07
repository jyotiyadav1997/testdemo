from selenium import webdriver
from percy import percy_snapshot

driverPath = "C:\\Users\\jyoti.y\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.maximize_window()
driver.get("https://facebook.com")
percy_snapshot(driver, 'testrun');