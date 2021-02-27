from Automation_for_Native_application.android_capability import des_cap_learn_android_using_source_code
import time

drive_instance = des_cap_learn_android_using_source_code()
time.sleep(3)
Ui_widget = drive_instance.find_elements_by_id("com.tutorials.learn.androidexample:id/example")
for el in Ui_widget:
    if el.text == 'Android UI Widgets':
        el.click()
        print('element clicked')
        break

