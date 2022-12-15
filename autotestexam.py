from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def capture_sceenshot():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(3)
    driver.get_screenshot_as_file("screenshot.png")
    driver.close()

def count_cards():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div").click()
    time.sleep(3)
    card_info_list = []
    cardinformation = driver.find_elements(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]//a")
    for info in cardinformation:
        card_info_list.append(info.get_attribute('href'))
    print("Totally %d items"%len(card_info_list))
    driver.get_screenshot_as_file("screenshot2.png")
    driver.close()

def count_stop_cards():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/")
    lis = driver.find_elements(By.CLASS_NAME, "swiper-wrapper")
    screenshot_numbers = 0
    
    for i in range(1,len(lis)+1):
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[%s]"%i).click()
        driver.get_screenshot_as_file("%s.png"%i)
        screenshot_numbers+=1
    if (screenshot_numbers) == len(lis):
        print("Stop card items : %d"%len(lis))
        print("Screenshot numbers : %d"%(screenshot_numbers))
    else:
        print("screenshot numbers are not same as stop card numbers")
    driver.close()

if __name__ == '__main__':
    capture_sceenshot()
    count_cards()
    count_stop_cards()