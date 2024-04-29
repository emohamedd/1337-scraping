import os
import time
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import telebot
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
   # Import the required modules
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import warnings
from dotenv import load_dotenv
import telebot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore") 
print(Fore.RED + Style.BRIGHT + """
 ██╗██████╗ ██████╗ ███████╗              ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
███║╚════██╗╚════██╗╚════██║              ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
╚██║ █████╔╝ █████╔╝    ██╔╝    █████╗    ███████╗██║     ██████╔╝██║██████╔╝   ██║   
 ██║ ╚═══██╗ ╚═══██╗   ██╔╝     ╚════╝    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
 ██║██████╔╝██████╔╝   ██║                ███████║╚██████╗██║  ██║██║██║        ██║   
 ╚═╝╚═════╝ ╚═════╝    ╚═╝                ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       
""" + Style.RESET_ALL)
 
print(Fore.YELLOW + Style.BRIGHT + "𝘾𝙃𝙀𝘾𝙆-𝙄𝙉 & 𝙋𝙊𝙊𝙇" + Style.RESET_ALL)


print(Fore.GREEN + Style.BRIGHT + " 🤖 ------  > Starting the bot <  ------ 🤖 " + Style.RESET_ALL)


def transcribe(url):
    with open('.temp', 'wb') as f:
        f.write(requests.get(url).content)

def click_checkbox(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver.find_element(By.ID, "recaptcha-anchor-label").click()
    driver.switch_to.default_content()

def request_audio_version(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA challenge expires in two minutes']"))
    driver.find_element(By.ID, "recaptcha-audio-button").click()

def solve_audio_captcha(driver):
    text = transcribe(driver.find_element(By.ID, "audio-source").get_attribute('src'))
    driver.find_element(By.ID, "audio-response").send_keys(text)
    driver.find_element(By.ID, "recaptcha-verify-button").click()

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# url = "https://candidature.1337.ma/meetings"
url = "https://candidature.1337.ma/piscines"

bot = telebot.TeleBot(TOKEN)

def send_telegram_message(text):
    bot.send_message(CHAT_ID, text)

driver = webdriver.Chrome()

driver.get('https://candidature.1337.ma/users/sign_in')

email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'user[email]'))
)

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'user[password]'))
)
email_field.send_keys('tahayassirboutaib12@gmail.com') # Your email
password_field.send_keys('HjAt$CRFq27zmSC') # Your password

password_field.send_keys(Keys.RETURN)

time.sleep(5)

driver.get(url)

# Call the captcha solver functions
click_checkbox(driver)
time.sleep(1)

# checkin_message = "New 'check-ins' spots will open soon. To be informed when some will open, you can follow us on twitter or like us on facebook:" # Check-in message
pool_message = "No Piscines are currently open. To be informed when it will open, you can follow us on twitter or like us on facebook:" # Pool message

soup = BeautifulSoup(driver.page_source, 'html.parser')
# old_content = checkin_message in soup.text 
old_content = pool_message in soup.text

send_telegram_message("🤖 1337 Bot started successfully  -- Waiting For New Update 🔄")
while True:
    driver.refresh()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # new_content = checkin_message in soup.text
    new_content = pool_message in soup.text

    if new_content != old_content:
        print(Fore.RED + Style.BRIGHT + "🚨 CHECK-IN 🚨" + Style.RESET_ALL)
        for i in range(10):
            send_telegram_message(f" 🚨 CHECK-IN 🚨 {url}")
        exit()

    time.sleep(5)
