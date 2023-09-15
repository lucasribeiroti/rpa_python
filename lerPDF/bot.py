# Import for the Desktop Bot

from botcity.document_processing import *
import pathlib
import pandas as pd
import os

os.system('cls')

dados = []

def lerPDF(arquivo):
    reader = PDFReader ()
    parser = reader.read_file(arquivo)
        
    _date = parser.get_first_entry('Date:')
    date = parser.read(_date, 1.428571, -1.3, 3.214286, 2.8)
    print('Date: ' + date)

    _bill_to = parser.get_first_entry('Bill to:')
    bill_to = parser.read(_bill_to, 1.296296, -1.6, 2.962963, 3.5)
    print('Bill to: ' + bill_to)
    
    
    _contact = parser.get_first_entry('Contact:')
    contact = parser.read(_contact, 1.236842, -1.2, 8.328947, 2.8)
    print('Contact: ' + contact)
    
    _balance_due = parser.get_first_entry('Balance due:')
    balance_due = parser.read(_balance_due, 1.1, -1.5, 2.66, 3)
    print('Balance due: ' + balance_due)

    dados.append([date, bill_to, contact, balance_due])

arquivos = pathlib.Path(r'C:\Users\lucas\developer\back-end\rpa_python\lerPDF\docs').glob('*.pdf')

for arquivo in arquivos:
    # print(arquivo)
    lerPDF(arquivo)

df = pd.DataFrame(dados, columns=['Date', 'Bill to', 'Contact', 'Balance due'])
df.to_csv('dados_pdf.csv', sep=',', index = False)