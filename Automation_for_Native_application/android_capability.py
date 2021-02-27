from pathlib import Path
from appium import webdriver
import unittest

common_cap_dict = dict(
    platformName='Android',
    platformVersion='9',
    automationName='uiautomator2',
    deviceName='Pixel 2 API 28 2')


def des_cap_youtube():
    desired_caps = dict(
        # platformName='Android',
        # platformVersion='9',
        # automationName='uiautomator2',
        # deviceName='Pixel 2 API 28 2',
        common_cap_dict,
        appPackage='com.google.android.youtube',
        appActivity='com.google.android.apps.youtube.app.WatchWhileActivity')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def des_cap_learn_android_using_source_code():
    desired_caps = dict(
        common_cap_dict,
        # appPackage='com.tutorials.learn.androidexample',
        # appActivity='com.tutorials.learn.androidexample.MainActivity')
        app='/Users/localadmin/Downloads/APK/Learn_Android_With_Source.apk')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
