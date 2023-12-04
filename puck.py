import pandas as pd
import tkinter as tk
from tkinter import ttk
import datetime as dt


#pip install pandas


lista_tipos = ["Codigo","Nivel_de_emergência","Data_da_ocorrencia","Relato"]
lista_codigo = []


def imprimir_relatorios():
    for item in lista_codigo:
        print(item)


def inserir():
    descroçao = entry_descrição.get()
    selecionar = selecionar_urgencia.get()
    relatorio = entry_relatorio.get()
    data_criaçao = dt.datetime.now()
    data_criaçao = data_criaçao.strftime("%d/%m/%y  %H:%M")
    
    if descroçao=='m001' or descroçao=='m002' or descroçao=='m003'  or descroçao=='m004':
        produto='mouse'
    elif descroçao=='t001' or descroçao=='t002' or descroçao=='t003' or descroçao=='t004':
        produto='teclado'
    elif descroçao=='c001' or descroçao=='c002' or descroçao=='c003' or descroçao=='c004':
        produto='cadeira'
    else:
        produto='codigo nao registrado no sistema'
        


    if descroçao=='m001' or descroçao=='m002' or descroçao=='m003'  or descroçao=='m004':
        preço=25.70
    elif descroçao=='t001' or descroçao=='t002' or descroçao=='t003' or descroçao=='t004':
        preço= 37.50
    elif descroçao=='c001' or descroçao=='c002' or descroçao=='c003' or descroçao=='c004':
        preço= 175.35
    else:
        preço='codigo nao registrado no sistema'
        
    
    tabela= { 'codigo': [descroçao],
         'produto': [produto],
         'preço': [preço],     
         'Nivel de urgencia': [selecionar],
         'Horario e Data da ocorrencia': [data_criaçao],
         'relato': [relatorio],
    }
    
    
    lista_codigo.append((descroçao,selecionar,relatorio,data_criaçao))


    
    tabela_df = pd.DataFrame(tabela )
    tabela_df.to_excel('excelcopia.xlsx',index=False)
      
    tabela_df_velha= pd.read_excel('excelcopia.xlsx')
    tabela_df_nova= pd.read_excel('excelPuck.xlsx')
    
       


    tabela_df_Unificada= pd.concat([tabela_df_nova,tabela_df_velha])
    tabela_df_Unificada.to_excel('excelPuck.xlsx',index=False)
        
    display(tabela_df_Unificada)  
    
    
    
    
    
tabela_df=inserir


janela = tk.Tk()


janela.title('PUCK')



label_Puck = tk.Label(text="PUCK")
label_Puck.grid(row=1,column=0, padx=10, pady= 10, sticky='nswe', columnspan=4)



label_tipo_codigo = tk.Label(text='⚫codigo:')
label_tipo_codigo.grid(row=2,column=1, padx=1, pady= 1, sticky='nswe', columnspan=1)
entry_descrição = tk.Entry()
entry_descrição.grid(row=3, column=2,padx=1,pady=1,sticky='nsew', columnspan=2)



label_tipo_urgencia = tk.Label(text='⚫Nível de urgencia:')
label_tipo_urgencia.grid(row=4,column=1, padx=1, pady= 1, sticky='nswe', columnspan=2)
selecionar_urgencia = ttk.Combobox(values='urgente' 'Não urgente')
selecionar_urgencia.grid(row=5, column=2,padx=1,pady=1,sticky='nsew', columnspan=2)



label_tipo_Relatorio = tk.Label(text='⚫Relatório:')
label_tipo_Relatorio.grid(row=6,column=1, padx=1, pady= 1, sticky='nswe', columnspan=1)
entry_relatorio = tk.Entry()
entry_relatorio.grid(row=7, column=1,padx=1,pady=1,sticky='nsew', columnspan=4,rowspan=1)


butao_enviar = tk.Button(text='enviar relatorio', command=inserir)
butao_enviar.grid(row=9, column=1,padx=1,pady=1,sticky='nsew', columnspan=4,)








janela.mainloop()

