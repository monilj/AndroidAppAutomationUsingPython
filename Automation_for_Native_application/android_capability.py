from pathlib import Path
from appium import webdriver
import unittest


def des_cap_for_youtube():
    desired_caps = dict(
        platformName='Android',
        platformVersion='9',
        automationName='uiautomator2',
        deviceName='Pixel 2 API 28 2',
        appPackage='com.google.android.youtube',
        appActivity='com.google.android.apps.youtube.app.WatchWhileActivity')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def des_cap_for_learn_android_with_source_code():
    desired_caps = dict(
        platformName='Android',
        platformVersion='9',
        automationName='uiautomator2',
        deviceName='Pixel 2 API 28 2',
        appPackage='com.tutorials.learn.androidexample',
        appActivity='com.tutorials.learn.androidexample.MainActivity')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
