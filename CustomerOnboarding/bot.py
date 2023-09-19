# Import for the Web Bot
from botcity.web import WebBot, Browser, By

from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager

import requests
import pandas as pd
from botcity.web.util import element_as_select

url = 'https://aai-devportal-media.s3.us-west-2.amazonaws.com/challenges/customer-onboarding-challenge.csv'
r = requests.get(url, allow_redirects=True)
open('MissingCustomers.csv', 'wb').write(r.content)

dados = pd.read_csv('MissingCustomers.csv', sep=',')

bot = WebBot()
bot.headless = False
bot.browser = Browser.FIREFOX
bot.driver_path = GeckoDriverManager().install()
# bot.driver_path = ChromeDriverManager().install()

bot.browse("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")
bot.wait(1000)
bot.maximize_window()

for colunas in dados.itertuples():
    bot.find_element('customerName', By.ID).send_keys(colunas[1])
    bot.find_element('customerID ', By.NAME).send_keys(colunas[2])
    bot.find_element('primaryContact', By.ID).send_keys(colunas[3])
    bot.find_element('street ', By.NAME).send_keys(colunas[4])
    bot.find_element('city', By.ID).send_keys(colunas[5])
    state = bot.find_element(selector='state', by=By.ID)
    state = element_as_select(state)
    state.select_by_value(value=colunas[6])
    bot.find_element('zip', By.ID).send_keys(colunas[7])
    bot.find_element('email', By.ID).send_keys(colunas[8])

    if colunas[9] == 'YES':
        bot.find_element('activeDiscountYes', By.ID).click()
    else:
        bot.find_element('activeDiscountNo', By.ID).click()

    if colunas[10] == 'NO':
        bot.find_element('NDA', By.ID).click()

    bot.find_element('submit_button', By.ID).click()

bot.wait(100)
bot.screenshot('Accuracy.png')
bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")
