from selenium.webdriver.common.by import By
from selenium import webdriver

# class webdriver():
def chrome(webdriver):
    webdriver.chrome()

def url(driver):
    webdriver.get("https://www.google.co.in/")

def maximize(driver):
    webdriver.maximize_window()

def googletxtbox(driver):
    webdriver.find_element(By.NAME,"q").send_keys("flipkart")

def textvalue(googletxtbox):
    googletxtbox.send_keys("flipkart")

def googlesearch(driver):
    webdriver.find_element(By.NAME,"btnK").click()

def flipkartlink(driver):
    webdriver.find_element(By.XPATH,"//h3[text()='Flipkart']").click()

def act_title(driver):
    webdriver.title

exp_title="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"

if(act_title==exp_title):
        print("Homepage is displayed")
else:
        print("Homepage not displayed")

def close(driver):
    webdriver.close()

ch=chrome(webdriver)
ur=url(webdriver)
max=maximize(webdriver)
gtxt=googletxtbox(webdriver)
txtval=textvalue(webdriver)
gsearch=googlesearch(webdriver)
link=flipkartlink(webdriver)
cl=close(webdriver)





