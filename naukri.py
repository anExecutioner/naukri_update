from selenium import webdriver
import time

class naukri_update():
    pre_text = 'Python Automation Engineer with B.Tech/B.E. in Computers currently living in Mumbai'

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def launch_browser(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("https://www.naukri.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def update(self):
        print(" --- you are logged in and we are ready to update your profile!! --- ")
        profile = driver.find_element_by_xpath("//a[@href='/mnjuser/profile']")
        driver.execute_script("arguments[0].click();",profile)
        edit = "//div[@class='widgetHead']//span[text()='Resume headline']/following-sibling::span"
        driver.find_element_by_xpath(edit).click()
        txt = driver.find_element_by_id("resumeHeadlineTxt")
        assert naukri_update.pre_text == txt.text, "Fail"
        txt.clear()
        time.sleep(3)
        txt.send_keys(naukri_update.pre_text)
        driver.find_element_by_xpath("//button[text()='Save']").click()

    def login(self):
        login_locator = "login_Layer"
        driver.find_element_by_id(login_locator).click()
        user = driver.find_element_by_xpath("//*[text()='Email ID / Username']/following-sibling::input")
        user.send_keys(self.username)
        pwd = driver.find_element_by_xpath("//*[text()='Password']/following-sibling::input")
        pwd.send_keys(self.password)
        login_btn = driver.find_element_by_xpath("//button[contains(@class,'loginButton')]")
        login_btn.click()
    
    def exit(self):
        time.sleep(2)
        driver.quit()

if __name__ == '__main__':
    username= "pankajgle7@gmail.com"
    password = 'Pankaj.soni@321'
    naukri = naukri_update(username,password)
    naukri.launch_browser()
    naukri.login()
    naukri.update()
    naukri.exit()