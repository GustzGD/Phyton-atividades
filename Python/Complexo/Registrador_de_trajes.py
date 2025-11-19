import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def salvar():
    nome = entry_nome.get()
    trajes = entry_trajes.get()
    modelo = entry_modelo.get()
    funcao = entry_funcao.get("1.0", tk.END).strip()
    data = entry_data.get()

    if not (nome and trajes and modelo and funcao and data):
        messagebox.showwarning("!!Atenção!!", "Algum campo vazio foi detectado, favor preencher.")
        return

    print("          <Dados sobre os trajes em funcionamento>          ")
    print(f"Nome: {nome}")
    print(f"Traje: {trajes}")
    print(f"Modelo: {modelo}")
    print(f"Função: {funcao}")
    print(f"Data: {data}")

    messagebox.showinfo("Sucesso", "Dados salvos!")

    entry_nome.delete(0, tk.END)
    entry_trajes.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_funcao.delete("1.0", tk.END)
    entry_data.delete(0, tk.END)

root = tk.Tk()
root.title("Registro de trajes - Freddy's Fazbear")
root.geometry("400x500")

tk.Label(root, text="Nome do Traje: ").pack(pady=5)
entry_nome = tk.Entry(root, width=20)
entry_nome.pack()

tk.Label(root, text="Traje: ").pack(pady=5)
entry_trajes = tk.Entry(root, width=40)
entry_trajes.pack()

tk.Label(root, text="Modelo: ").pack(pady=5)
entry_modelo = tk.Entry(root, width=40)
entry_modelo.pack()

tk.Label(root, text="Função do traje: ").pack(pady=5)
entry_funcao = tk.Text(root, height=5, width=40)
entry_funcao.pack()

tk.Label(root, text="Data de criação: ").pack(pady=5)
entry_data = tk.Entry(root, width=20)
entry_data.pack()
entry_data.insert(0, datetime.now().strftime("%d/%m/%Y"))

button_salvar = tk.Button(root, text="Salvar traje", command=salvar)
button_salvar.pack(pady=20)

root.mainloop()
