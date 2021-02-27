from pathlib import Path
from appium import webdriver
import unittest


def des_cap():
    desired_caps = dict(
        platformName='Android',
        platformVersion='9',
        automationName='uiautomator2',
        deviceName='Pixel 2 API 28 2',
        appPackage='com.google.android.youtube',
        appActivity='com.google.android.apps.youtube.app.WatchWhileActivity')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


drive_instance = des_cap()
el = drive_instance.find_element_by_accessibility_id('Search')
el.click()
edit_box = drive_instance.find_element_by_id('search_edit_text')
edit_box.click()
edit_box.send_keys("Appium automation")
drive_instance.find_element_by_id('com.google.android.youtube:id/text').click()