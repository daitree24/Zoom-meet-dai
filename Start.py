# # import os
# # import subprocess
# # from importlib.resources import path
# # import threading
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time
# # from selenium.webdriver.chrome.options import Options
# # import configparser
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import NoSuchElementException

# # from cgitb import reset
# # import secrets
# # import time
# # import gspread
# # import colorama
# # from colorama import Fore, Back, Style
# # print(Style.BRIGHT + Fore.RESET + "Welcome To Ramgadiya Program")
# # print(Style.BRIGHT + Fore.RESET +
# #       "Contact us on Whatsapp For Software Activation +91 8059199600")
# # print(Style.BRIGHT + Fore.RESET +
# #       "Visit Site for More detail https://ramgadiya.com")
# # colorama.init(autoreset=True)

# # config = configparser.ConfigParser()
# # config.read('Config.ini')
# # PROXY = []
# # with open("ip.txt", "r") as ip:
# #     for i in range(30):
# #         PROXY.append(ip.readline())

# # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
# # options = webdriver.ChromeOptions()

# # prefs = {
# #     "profile.default_content_setting_values.media_stream_mic": 1,  # 1 = allow, 2 = block
# #     "profile.default_content_setting_values.media_stream_camera": 1,
# #     "profile.default_content_setting_values.notifications": 2,  # 1 = allow, 2 = block
# #     "profile.default_content_setting_values.geolocation": 2,
# # }
# # options.add_experimental_option("prefs", prefs)

# # options.add_experimental_option('excludeSwitches', ['enable-logging'])
# # options.add_argument(f'user-agent={user_agent}')
# # options.add_experimental_option("detach", True)
# # options.add_argument('--ignore-certificate-errors')
# # options.add_argument('--allow-running-insecure-content')
# # options.add_argument("--disable-extensions")
# # options.add_argument("--proxy-server='direct://'")
# # options.add_argument("--proxy-bypass-list=*")
# # options.add_argument("--use-fake-device-for-media-stream")
# # options.add_argument("--start-maximized")
# # # options.add_argument('--headless')

# # count = 0
# # number = (int(config['ZOOM']['Member_Count']))
# # meet_code = config['ZOOM']['Meeting_ID']
# # passcode = config['ZOOM']['Meeting_Pass']
# # sec = config['ZOOM']['Member_Hold_Time']


# # lis = []
# # with open("name.txt", 'r') as f:
# #     for i in range(5):
# #         lis.append(f.readline())


# # n = 0
# # def fun(n, count):
# #     p = PROXY[count]
# #     options.add_argument(f"--proxy-server={p}")
# #     driver = webdriver.Chrome(service=Service(
# #         ChromeDriverManager().install()), options=options)

    
# #     driver.get(f'https://zoom.us/wc/join/{meet_code}')

# #     wait = WebDriverWait(driver, 10)

# #     wait.until(EC.presence_of_element_located((By.ID, "input-for-name")))
# #     inp = driver.find_element(by='id', value='input-for-name')
# #     inp.send_keys(f"{lis[n]}")
    
    
# #     # time.sleep(1)

# #     # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "preview-join-button")))
# #     # btn2 = driver.find_element(by='class', value='preview-join-button')

# #     try:
# #         elem = driver.find_element(
# #             by='id', value='onetrust-accept-btn-handler')
# #         elem.click()
# #         time.sleep(1)
# #     except NoSuchElementException:
# #         pass

# #     try:
# #         elem = driver.find_element(by='id', value='wc_agree1')
# #         elem.click()
# #     except NoSuchElementException:
# #         pass

# #     wait.until(EC.presence_of_element_located((By.ID, "input-for-pwd")))
# #     inp2 = driver.find_element(by='id', value='input-for-pwd')
# #     inp2.send_keys(passcode)
    
# #     wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'preview-join-button')))
# #     btn3 = driver.find_element(By.CLASS_NAME, value='preview-join-button')
# #     btn3.click()

# #     time.sleep(5)
# #     # element = WebDriverWait(driver, 30).until(
# #     #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/button")))

# #     # element.click()


# #     try:
# #         notification = driver.find_element(By.CLASS_NAME, 'notification-message-wrap__layer')
# #         if notification.is_displayed():
# #             driver.execute_script("arguments[0].style.display = 'none';", notification)
# #     except NoSuchElementException:
# #         pass
    
    
# #     joinAudioBtn = WebDriverWait(driver, 20).until(
# #         EC.element_to_be_clickable((By.CLASS_NAME, 'join-audio-by-voip__join-btn'))
# #     )
# #     driver.execute_script("arguments[0].scrollIntoView(true);", joinAudioBtn)
# #     driver.execute_script("arguments[0].click();", joinAudioBtn)

# #     print(Style.BRIGHT + Fore.YELLOW +
# #           f"{lis[n]}{Style. RESET_ALL}{Style.BRIGHT+Fore.GREEN}Join Done\n")
    
    
# #     time.sleep(5)
    
# #     # element = WebDriverWait(driver, 30).until(
# #     #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div[2]/div/div/div[1]/div/div")))

# #     # element.click()
    
# #     # element = WebDriverWait(driver, 30).until(
# #     #     EC.element_to_be_clickable(
# #     #         (By.XPATH, "//button[text()='Join Audio by Computer']")))
# #     # element.click()
# #     # time.sleep(2)
    
# #     # element = WebDriverWait(driver, 30).until(
# #     #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div/div[1]/div/div[5]/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")))

# #     # element.click()
    

# #     # element = WebDriverWait(driver, 50).until(EC.presence_of_element_located(
# #     #     (By.ID, "multi-view-video")))
# #     # driver.execute_script(
# #     #     "arguments[0].style.visibility='hidden'", element)
# #     # print("hide video")

# #     count += 1
# #     if count == 30:
# #         count = 0
# #     # n+=1
# #     # time.sleep(2)


# # while n < number:
# #     a = threading.Thread(target=fun, args=(n, count,))
# #     a.start()
# #     n += 1
# #     time.sleep(10)

# # input()

# import os
# import subprocess
# import threading
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.chrome.options import Options
# import configparser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# import colorama
# from colorama import Fore, Style

# print(Style.BRIGHT + Fore.RESET + "Welcome To Ramgadiya Program")
# print(Style.BRIGHT + Fore.RESET + "Contact us on Whatsapp For Software Activation +91 8059199600")
# print(Style.BRIGHT + Fore.RESET + "Visit Site for More detail https://ramgadiya.com")
# colorama.init(autoreset=True)

# # Read configuration
# config = configparser.ConfigParser()
# config.read('Config.ini')

# PROXY = []
# with open("ip.txt", "r") as ip:
#     for i in range(30):
#         PROXY.append(ip.readline().strip())

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chrome in headless mode
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# prefs = {
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.notifications": 2,
#     "profile.default_content_setting_values.geolocation": 2,
# }
# options.add_experimental_option("prefs", prefs)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument(f'user-agent={user_agent}')
# options.add_experimental_option("detach", True)
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--use-fake-device-for-media-stream")
# options.add_argument("--start-maximized")

# count = 0
# number = (int(config['ZOOM']['Member_Count']))
# meet_code = config['ZOOM']['Meeting_ID']
# print(meet_code)
# passcode = config['ZOOM']['Meeting_Pass']
# sec = config['ZOOM']['Member_Hold_Time']

# lis = []
# with open("name.txt", 'r') as f:
#     for i in range(number):  # Adjust based on number of members
#         lis.append(f.readline().strip())

# def fun(n, count):
#     p = PROXY[count]
#     options.add_argument(f"--proxy-server={p}")
#     driver = webdriver.Chrome(service=Service(
#         ChromeDriverManager().install()), options=options)

#     driver.get(f'https://zoom.us/wc/join/{meet_code}')
#     wait = WebDriverWait(driver, 10)

#     wait.until(EC.presence_of_element_located((By.ID, "input-for-name")))
#     inp = driver.find_element(by='id', value='input-for-name')
#     inp.send_keys(f"{lis[n]}")

#     try:
#         elem = driver.find_element(by='id', value='onetrust-accept-btn-handler')
#         elem.click()
#         time.sleep(1)
#     except NoSuchElementException:
#         pass

#     try:
#         elem = driver.find_element(by='id', value='wc_agree1')
#         elem.click()
#     except NoSuchElementException:
#         pass

#     wait.until(EC.presence_of_element_located((By.ID, "input-for-pwd")))
#     inp2 = driver.find_element(by='id', value='input-for-pwd')
#     inp2.send_keys(passcode)

#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'preview-join-button')))
#     btn3 = driver.find_element(By.CLASS_NAME, value='preview-join-button')
#     btn3.click()

#     time.sleep(5)

#     try:
#         notification = driver.find_element(By.CLASS_NAME, 'notification-message-wrap__layer')
#         if notification.is_displayed():
#             driver.execute_script("arguments[0].style.display = 'none';", notification)
#     except NoSuchElementException:
#         pass

#     joinAudioBtn = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, 'join-audio-by-voip__join-btn'))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", joinAudioBtn)
#     driver.execute_script("arguments[0].click();", joinAudioBtn)

#     print(Style.BRIGHT + Fore.YELLOW + f"{lis[n]}{Style. RESET_ALL}{Style.BRIGHT+Fore.GREEN} Join Done\n")
#     time.sleep(5)

#     count += 1
#     if count == len(PROXY):  # Avoid exceeding proxy list length
#         count = 0

# # Start threads based on the Member_Count
# threads = []
# for i in range(number):
#     t = threading.Thread(target=fun, args=(i, count))
#     threads.append(t)
#     t.start()
#     count += 1
#     if count == len(PROXY):
#         count = 0
#     time.sleep(10)

# # # Ensure all threads complete
# # for t in threads:
# #     t.join()


# import os
# import threading
# import signal
# import sys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.chrome.options import Options
# import configparser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# import colorama
# from colorama import Fore, Style

# print(Style.BRIGHT + Fore.RESET + "Welcome To Ramgadiya Program")
# print(Style.BRIGHT + Fore.RESET + "Contact us on Whatsapp For Software Activation +91 8059199600")
# print(Style.BRIGHT + Fore.RESET + "Visit Site for More detail https://ramgadiya.com")
# colorama.init(autoreset=True)

# # Read configuration
# config = configparser.ConfigParser()
# config.read('Config.ini')

# PROXY = []
# with open("ip.txt", "r") as ip:
#     for i in range(30):
#         PROXY.append(ip.readline().strip())

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chrome in headless mode
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# prefs = {
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.notifications": 2,
#     "profile.default_content_setting_values.geolocation": 2,
# }
# options.add_experimental_option("prefs", prefs)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument(f'user-agent={user_agent}')
# options.add_experimental_option("detach", True)
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--use-fake-device-for-media-stream")
# options.add_argument("--start-maximized")

# count = 0
# number = int(config['ZOOM']['Member_Count'])
# meet_code = config['ZOOM']['Meeting_ID']
# passcode = config['ZOOM']['Meeting_Pass']
# sec = config['ZOOM']['Member_Hold_Time']

# lis = []
# with open("name.txt", 'r') as f:
#     for i in range(number):
#         lis.append(f.readline().strip())

# def fun(n, count):
#     p = PROXY[count]
#     options.add_argument(f"--proxy-server={p}")
#     driver = webdriver.Chrome(service=Service(
#         ChromeDriverManager().install()), options=options)

#     driver.get(f'https://zoom.us/wc/join/{meet_code}')
#     wait = WebDriverWait(driver, 10)

#     wait.until(EC.presence_of_element_located((By.ID, "input-for-name")))
#     inp = driver.find_element(by='id', value='input-for-name')
#     inp.send_keys(f"{lis[n]}")

#     try:
#         elem = driver.find_element(by='id', value='onetrust-accept-btn-handler')
#         elem.click()
#         time.sleep(1)
#     except NoSuchElementException:
#         pass

#     try:
#         elem = driver.find_element(by='id', value='wc_agree1')
#         elem.click()
#     except NoSuchElementException:
#         pass

#     wait.until(EC.presence_of_element_located((By.ID, "input-for-pwd")))
#     inp2 = driver.find_element(by='id', value='input-for-pwd')
#     inp2.send_keys(passcode)

#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'preview-join-button')))
#     btn3 = driver.find_element(By.CLASS_NAME, value='preview-join-button')
#     btn3.click()

#     time.sleep(3)

#     try:
#         notification = driver.find_element(By.CLASS_NAME, 'notification-message-wrap__layer')
#         if notification.is_displayed():
#             driver.execute_script("arguments[0].style.display = 'none';", notification)
#     except NoSuchElementException:
#         pass

#     joinAudioBtn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CLASS_NAME, 'join-audio-by-voip__join-btn'))
#     )
#     driver.execute_script("arguments[0].scrollIntoView(true);", joinAudioBtn)
#     driver.execute_script("arguments[0].click();", joinAudioBtn)

#     print(Style.BRIGHT + Fore.YELLOW + f"{lis[n]}{Style. RESET_ALL}{Style.BRIGHT+Fore.GREEN} Join Done\n")
#     time.sleep(3)

#     count += 1
#     if count == len(PROXY):
#         count = 0

# # Stop event
# stop_event = threading.Event()

# def signal_handler(sig, frame):
#     print("Stopping script...")
#     stop_event.set()

# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# # Start threads
# threads = []
# for i in range(number):
#     t = threading.Thread(target=fun, args=(i, count))
#     threads.append(t)
#     t.start()
#     count += 1
#     if count == len(PROXY):
#         count = 0
#     time.sleep(8)

# # Wait for all threads to finish
# for t in threads:
#     t.join()

# print("All threads have finished. Script will now run indefinitely until manually stopped.")

# # Run indefinitely until stop event is set
# try:
#     while not stop_event.is_set():
#         time.sleep(8)
# finally:
#     print("Stopping the script as requested.")



import threading
import time
import configparser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import colorama
from colorama import Fore, Style

print(Style.BRIGHT + Fore.RESET + "Welcome To Ramgadiya Program")
print(Style.BRIGHT + Fore.RESET + "Contact us on Whatsapp For Software Activation +91 8059199600")
print(Style.BRIGHT + Fore.RESET + "Visit Site for More detail https://ramgadiya.com")
colorama.init(autoreset=True)

# Read configuration
config = configparser.ConfigParser()
config.read('Config.ini')

PROXY = []
with open("ip.txt", "r") as ip:
    for i in range(30):
        PROXY.append(ip.readline().strip())

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

prefs = {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_setting_values.geolocation": 2,
}
options.add_experimental_option("prefs", prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--use-fake-device-for-media-stream")
options.add_argument("--start-maximized")

count = 0
number = (int(config['ZOOM']['Member_Count']))
meet_code = config['ZOOM']['Meeting_ID']
passcode = config['ZOOM']['Meeting_Pass']
sec = config['ZOOM']['Member_Hold_Time']

lis = []
with open("name.txt", 'r') as f:
    for i in range(number):
        lis.append(f.readline().strip())

def fun(n, count):
    p = PROXY[count]
    options.add_argument(f"--proxy-server={p}")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    driver.get(f'https://zoom.us/wc/join/{meet_code}')
    wait = WebDriverWait(driver, 25)

    wait.until(EC.presence_of_element_located((By.ID, "input-for-name")))
    inp = driver.find_element(by='id', value='input-for-name')
    inp.send_keys(f"{lis[n]}")

    try:
        elem = driver.find_element(by='id', value='onetrust-accept-btn-handler')
        elem.click()
        time.sleep(1)
    except NoSuchElementException:
        pass

    try:
        elem = driver.find_element(by='id', value='wc_agree1')
        elem.click()
    except NoSuchElementException:
        pass

    wait.until(EC.presence_of_element_located((By.ID, "input-for-pwd")))
    inp2 = driver.find_element(by='id', value='input-for-pwd')
    inp2.send_keys(passcode)

    wait.until(EC.presence_of_all_elements_located((By.ID, "preview-audio-control-button")))
    audioBtn = driver.find_element(By.ID, "preview-audio-control-button")
    audioBtn.click()
    time.sleep(1)
    audioBtn.click()
    time.sleep(1)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'preview-join-button')))
    btn3 = driver.find_element(By.CLASS_NAME, value='preview-join-button')
    btn3.click()

    time.sleep(2)

    # try:
    #     notification = driver.find_element(By.CLASS_NAME, 'notification-message-wrap__layer')
    #     if notification.is_displayed():
    #         driver.execute_script("arguments[0].style.display = 'none';", notification)
    # except NoSuchElementException:
    #     pass

    # joinAudioBtn = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, 'join-audio-by-voip__join-btn'))
    # )
    # driver.execute_script("arguments[0].scrollIntoView(true);", joinAudioBtn)
    # driver.execute_script("arguments[0].click();", joinAudioBtn)

    print(Style.BRIGHT + Fore.YELLOW + f"{lis[n]}{Style. RESET_ALL}{Style.BRIGHT+Fore.GREEN} Join Done\n")
    # time.sleep(5)

    count += 1
    if count == len(PROXY):
        count = 0

threads = []
for i in range(number):
    t = threading.Thread(target=fun, args=(i, count))
    threads.append(t)
    t.start()
    count += 1
    if count == len(PROXY):
        count = 0
    time.sleep(4)

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads completed. Exiting script...")