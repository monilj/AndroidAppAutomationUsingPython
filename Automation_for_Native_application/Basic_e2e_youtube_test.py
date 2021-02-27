from Automation_for_Native_application.android_capability import des_cap

drive_instance = des_cap()
el = drive_instance.find_element_by_accessibility_id('Search')
el.click()
edit_box = drive_instance.find_element_by_id('search_edit_text')
edit_box.click()
edit_box.send_keys("Appium automation")
drive_instance.find_element_by_id('com.google.android.youtube:id/text').click()