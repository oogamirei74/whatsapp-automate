import pandas as pd
import time
import urllib.parse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(r"E:\Whatsapp_automate\chromedriver.exe")
driver = webdriver.Chrome(service=service)

data = pd.read_excel("contacts.xlsx")

message = "Assalamu Alaikum. I love you."

driver.get("https://web.whatsapp.com")

print("Scan QR code in WhatsApp Web")
input("Press ENTER after scanning")

for number in data["Number"]:

    url = f"https://web.whatsapp.com/send?phone={number}"
    driver.get(url)

    try:
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )

        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

        print("Message sent to:", number)

    except:
        print("Failed to send to:", number)

    time.sleep(6)

driver.quit()