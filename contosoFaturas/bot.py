from botcity.core import DesktopBot
import pandas as pd

# from botcity.maestro import *

def not_found(label):
    print(f"Element not found: {label}")

dados = pd.read_excel('C:/Users/lucas/developer/back-end/rpa_python/contosoFaturas/file/Contoso Coffee Shop Invoices.xlsx')
print(dados)

bot = DesktopBot()
path_app = 'C:/Program Files (x86)/Contoso, Inc/Contoso Invoicing/LegacyInvoicingApp.exe'

bot.execute(path_app)
bot.wait(1500)
bot.maximize_window()
bot.wait(1000)

if not bot.find( "invoices", matching=0.97, waiting_time=10000):
    not_found("invoices")
bot.click()

def cadastraFaturas(data, conta, contato, valor, status):
    if not bot.find( "novo_registro", matching=0.97, waiting_time=10000):
        not_found("novo_registro")
    bot.click()
               
    if not bot.find( "date", matching=0.97, waiting_time=10000):
        not_found("date")
    bot.click_relative(71, 8)
    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])
    bot.paste(data)

    bot.tab()
    bot.paste(conta)
    bot.tab()
    bot.paste(contato)
    bot.tab()
    bot.paste(valor)
    
    coluna = status

    if not bot.find( "status-inicio", matching=0.97, waiting_time=10000):
        not_found("status-inicio")
    bot.click_relative(56, 7)
       
    if coluna == "Uninvoiced":
        if not bot.find( "univoiced", matching=0.97, waiting_time=10000):
            not_found("univoiced")
        bot.click_relative(62, 32)

    elif coluna == "Invoiced":
        if not bot.find( "invoiced", matching=0.97, waiting_time=10000):
            not_found("invoiced")
        bot.click_relative(62, 56)
    
    else:
        if not bot.find( "paid", matching=0.97, waiting_time=10000):
            not_found("paid")
        bot.click_relative(60, 76)
        
    if not bot.find( "salvar", matching=0.97, waiting_time=10000):
        not_found("salvar")
    bot.click()
    
for coluna in dados.itertuples():
    cadastraFaturas(str(coluna[1]), str(coluna[2]), str(coluna[3]), str(coluna[4]), str(coluna[5]))

bot.alt_f4()