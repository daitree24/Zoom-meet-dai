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

PROXY = []
with open("ip.txt", "r") as ip:
    for i in range(number):
        PROXY.append(ip.readline().strip())

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
    audioBtn = driver.find_element(by='id', value="preview-audio-control-button")
    audioBtn.click()
    time.sleep(2)
    audioBtn.click()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'preview-join-button')))
    btn3 = driver.find_element(By.CLASS_NAME, value='preview-join-button')
    btn3.click()

    # time.sleep(2)

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
    time.sleep(6)

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads completed. Exiting script...")