from botcity.core import DesktopBot

# from botcity.maestro import *

def not_found(label):
    print(f"Element not found: {label}")

def cadastraFaturas():
    bot = DesktopBot()
    path_app = r'C:\Program Files (x86)\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe'

    bot.execute(path_app)
    bot.wait(1500)
    bot.maximize_window()
    bot.wait(1000)
    
    
    if not bot.find( "invoices", matching=0.97, waiting_time=10000):
        not_found("invoices")
    bot.click()
    
    if not bot.find( "novo_registro", matching=0.97, waiting_time=10000):
        not_found("novo_registro")
    bot.click()
        
        
        
        
    if not bot.find( "date", matching=0.97, waiting_time=10000):
        not_found("date")
    bot.click_relative(71, 8)
    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])
    bot.paste('09/15/2023')

    bot.tab()
    bot.paste('123456')
    bot.tab()
    bot.paste('bot@gmail.com')
    bot.tab()
    bot.paste('10000')
    
    if not bot.find( "status-inicio", matching=0.97, waiting_time=10000):
        not_found("status-inicio")
    bot.click_relative(56, 7)
       
    if not bot.find( "univoiced", matching=0.97, waiting_time=10000):
        not_found("univoiced")
    bot.click_relative(62, 32)
    
    if not bot.find( "invoiced", matching=0.97, waiting_time=10000):
        not_found("invoiced")
    bot.click_relative(62, 56)
    
    if not bot.find( "paid", matching=0.97, waiting_time=10000):
        not_found("paid")
    bot.click_relative(60, 76)
    
    
    
cadastraFaturas()







