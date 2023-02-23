from tkinter import *
from tkinter.filedialog import *
import requests
from tika import parser

def collect_input():
    r_insc = int(input_insc.get(1.0, 'end-1c'))
    r_ini = int(input_nti.get(1.0, 'end-1c'))
    r_fin = int(input_ntf.get(1.0, 'end-1c'))
    dir = askdirectory()


    for i in range(r_ini, r_fin+1):
        url = f"http://nfe.maraba.pa.gov.br/eSiat/Valida_NFE_Emissao.aspx?InscricaoMunicipal={r_insc}&NumeroNota={i}&Origem=RELACAO"
        response = requests.request("GET", url)
        raw = parser.from_buffer(response.text)
        endereco = f'{dir}\\{i}.pdf'
        if len(raw['metadata']['pdf:unmappedUnicodeCharsPerPage']) != 6:
            with open(endereco, 'wb') as novo_arquivo:
                novo_arquivo.write(response.content)
        else:
            break

janela = Tk()
janela.geometry('400x200')
janela.title('Download NFS-e')

Label(janela, text='Inscrição municipal:').grid(column=0, row=0, padx=10, pady=0)
input_insc = Entry(janela, width=15)
input_insc.grid(column=1, row=0, padx=10, pady=10)

Label(janela, text='Número de nota inicial:').grid(column=0, row=1, padx=10, pady=0)
input_nti = Entry(janela, width=15)
input_nti.grid(column=1, row=1, padx=10, pady=10)

Label(janela, text='Número de nota final:').grid(column=0, row=2, padx=10, pady=0)
input_ntf = Entry(janela, width=15)
input_ntf.grid(column=1, row=2, padx=10, pady=10)

button = Button(janela, text='Download', command=collect_input).grid(column=2, row=3)

Label(janela, text='Feito por JV :)').grid(column=0, row=4, pady=30)

janela.mainloop()