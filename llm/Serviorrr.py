from flask import Flask, request, jsonify

app = Flask(__name__)

stored_data = {}  # Global variable to store received data
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pathlib
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings
from time import time as t
warnings.simplefilter('ignore')
ScriptDir = pathlib.Path().absolute()
url = "https://chat.openai.com/c/043e4ee0-b1ff-4af2-80ff-b77a88e91ab2"


# Use undetected_chromedriver
options = uc.ChromeOptions()
options.add_argument('--profile-directory=Default')
options.add_argument(f'--user-data-dir={ScriptDir}\\chromedata')
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get(url=url)

def ChatGpt(query,link:str=""):
    C=t()
    prompt_element=driver.find_element(By.ID,"prompt-textarea")

    prompt_element.clear()
    prompt_element.send_keys(query)
    prompt_element.send_keys(Keys.ENTER)
    sleep(1)
    while 1:
        try:
            sleep(0.1)
            
            driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[2]/form/div/div/div/button').click()
            break
        except :
            pass
        try:
            driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/button").click()
        except:
            pass
    A=driver.find_elements(By.CLASS_NAME,"markdown")[-1].text
    while 1:
        sleep(0.6)
        if driver.find_elements(By.CLASS_NAME,"markdown")[-1].text==A:
            break
        else:
            A=driver.find_elements(By.CLASS_NAME,"markdown")[-1].text
    print(t()-C)
    return A
# Endpoint to receive JSON data
@app.route('/', methods=['POST'])
def receive_json():
    try:
        received_data = request.json  # Accessing the JSON data sent in the request
        # Storing the received data
        
        # Returning a success message
        return jsonify({"message": ChatGpt(received_data["prompt"])})
    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message)

# Endpoint to send back the stored data
if __name__ == '__main__':
    app.run(port=4445)
