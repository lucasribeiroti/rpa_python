from botcity.core import DesktopBot, Backend

bot = DesktopBot()
path = 'C:/Users/lucas/developer/back-end/rpa_python/MyCRM/app/MyCRM.exe'

bot.execute(path)
bot.wait(1000)
bot.connect_to_app(backend=Backend.UIA, path=path)

janela_principal = bot.find_app_window(title='My CRM (Sample App)')
janela_principal.menu_select('File -> Clear Fields')
janela_principal.type_keys('%{t} Lucas')
janela_principal.type_keys('%{l} Ribeiro')
janela_principal.Edit10.type_keys('JF')
janela_principal.Male.click()
janela_principal.Company.select()
janela_principal.Other.select()
janela_principal.People.select()
janela_principal.menu_select('File -> Open')
# print(janela_principal.print_control_identifiers())
