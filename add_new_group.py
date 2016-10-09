# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from group import Group
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new_group (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        self.wd.implicitly_wait(60)

    def open_homepage(self, wd):
        wd.get("http://localhost/addressbook/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("grupy").click()

    def add_new_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.header)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.name)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Wyloguj się").click()

    def test_add_full_group(self):
        success = True
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.add_new_group(wd, Group(header="New group", name="New group", footer="New group"))
        self.return_to_group_page(wd)
        self.logout(wd)
        self.assertTrue(success)

    def test_add_empty_group(self):
        success = True
        wd = self.wd
        self.open_homepage(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.add_new_group(wd, Group(header="", name="", footer=""))
        self.return_to_group_page(wd)
        self.logout(wd)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
