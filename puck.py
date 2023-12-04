import pandas as pd
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import datetime as dt

senha_admin = "mundosenai"


def fazer_relatorio():
    
    def inserir():
        descricao = entry_descrição.get()
        urgencia = selecionar_urgencia.get()
        relato = entry_relatorio.get("1.0", tk.END)
        data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")

        if descricao in ['m001', 'm002', 'm003', 'm004']:
            produto = 'mouse'
            preco = 25.70
        elif descricao in ['t001', 't002', 't003', 't004']:
            produto = 'teclado'
            preco = 37.50
        elif descricao in ['c001', 'c002', 'c003', 'c004']:
            produto = 'cadeira'
            preco = 175.35
        else:
            produto = 'codigo nao registrado no sistema'
            preco = 0.00


        tabela = {
            'codigo': [descricao],
            'produto': [produto],
            'preço': [preco],
            'Nivel de urgencia': [urgencia],
            'Horario e Data da ocorrencia': [data_criacao],
            'relato': [relato],
        }

        tabela_df = pd.DataFrame(tabela)


        
        tabela_df = pd.DataFrame(tabela )
        tabela_df.to_excel('excelcopia.xlsx',index=False)
        
        tabela_df_velha= pd.read_excel('excelcopia.xlsx')
        tabela_df_nova= pd.read_excel('excelPuck.xlsx')
        
        

        tabela_df_Unificada= pd.concat([tabela_df_nova,tabela_df_velha])
        tabela_df_Unificada.to_excel('excelPuck.xlsx',index=False)

        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

    
    relatorio_janela = tk.Toplevel(janela)
    relatorio_janela.title("Relatório PUCK")
    relatorio_janela.iconbitmap('IconePuck.ico')

    fonte_titulo = ("Bodoni FLF", 40, "bold")
    fonte = ("Bodoni FLF", 16, "bold")
    
    label_Puck = tk.Label(relatorio_janela, text="SGBD PUCK", font=fonte_titulo, fg="purple")
    label_Puck.grid(row=0, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')

    label_tipo_codigo = tk.Label(relatorio_janela, text='Código:', font=fonte)
    label_tipo_codigo.grid(row=1, column=0, padx=20, pady=10, sticky='w')
    
    entry_descrição = tk.Entry(relatorio_janela, font=fonte)
    entry_descrição.grid(row=1, column=1, padx=20, pady=10, sticky='ew', columnspan=3)

    label_tipo_urgencia = tk.Label(relatorio_janela, text='Nível de urgência:', font=fonte)
    label_tipo_urgencia.grid(row=2, column=0, padx=20, pady=10, sticky='w')

    selecionar_urgencia = ttk.Combobox(relatorio_janela, values=['Urgente', 'Não urgente'], font=fonte)
    selecionar_urgencia.grid(row=2, column=1, padx=20, pady=10, sticky='ew', columnspan=3)

    label_tipo_Relatorio = tk.Label(relatorio_janela, text='Relatório:', font=fonte)
    label_tipo_Relatorio.grid(row=3, column=0, padx=20, pady=10, sticky='w')

    entry_relatorio = tk.Text(relatorio_janela, wrap=tk.WORD, font=fonte, height=10, width=40)
    entry_relatorio.grid(row=3, column=1, padx=20, pady=10, sticky='nsew', columnspan=3, rowspan=2)

    botao_enviar = tk.Button(relatorio_janela, text='Enviar relatório', command=inserir, font=("Bodoni FLF", 20, "bold"))
    botao_enviar.grid(row=5, column=0, padx=20, pady=20, columnspan=4, sticky='nsew')

    for i in range(6):
        relatorio_janela.grid_rowconfigure(i, weight=1)
    for i in range(4):
        relatorio_janela.grid_columnconfigure(i, weight=1)

excel_filename = 'excelPuck.xlsx'

def administracao():
    senha = simpledialog.askstring("Senha de Administração", "Digite a senha de administração:")
    
    

    if senha == senha_admin:
        
        
        administracao_janela = tk.Toplevel(janela)
        administracao_janela.title("Tela de Administração")
        administracao_janela.iconbitmap('IconePuck.ico')
       
        # Lê os dados de um arquivo Excel (excel_filename) e carrega em um DataFrame (df).
        df = pd.read_excel(excel_filename)

        # Cria um widget Treeview na janela de administração.
        treeview = ttk.Treeview(administracao_janela)
        treeview["columns"] = list(df.columns)

        # Configura as colunas do Treeview com os nomes das colunas do DataFrame.
        for col in df.columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=100)

        # Insere os dados do DataFrame no Treeview.
        for _, row in df.iterrows():
            values = list(row)
            treeview.insert("", "end", values=values)

        # Faz com que o Treeview preencha todo o espaço disponível na janela.
        treeview.pack(fill="both", expand=True)

        # Mantém a janela aberta.
        administracao_janela.mainloop()

    else:
        tk.messagebox.showerror("Acesso Negado", "Senha incorreta!")

janela = tk.Tk()
largura_janela = 400
altura_janela = 460
janela.geometry(f"{largura_janela}x{altura_janela}")
janela.title("Puck")
janela.iconbitmap('IconePuck.ico')  # Defina o ícone para a janela principal


botao_relatorio = tk.Button(janela, text="Fazer Relatório", command=fazer_relatorio, padx=50, pady=20, font=("Bodoni FLF", 20, "bold"))
botao_administracao = tk.Button(janela, text="Administração", command=administracao, padx=50, pady=20, font=("Bodoni FLF", 20, "bold"))




fonte_titulo = ("Bodoni FLF", 40, "bold")
label_Puck = tk.Label(janela, text="SGBD PUCK", font=fonte_titulo, fg="purple")
label_Puck.pack(padx=20, pady=20)

botao_relatorio.pack(pady=25)
botao_administracao.pack()

janela.mainloop()