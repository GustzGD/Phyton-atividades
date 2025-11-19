import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def salvar_dados():
    nome = entry_nome.get()
    modelo = entry_modelo.get()
    placa = entry_placa.get()
    servico = entry_servico.get("1.0", tk.END).strip()
    data = entry_data.get()

    # Validação simples
    if not (nome and modelo and placa and servico and data):
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return

    # Exibe os dados no console
    print("===== Dados do Serviço =====")
    print(f"Nome: {nome}")
    print(f"Modelo do Veículo: {modelo}")
    print(f"Placa: {placa}")
    print(f"Serviço: {servico}")
    print(f"Data: {data}")
    print("============================")

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

    # Limpa os campos
    entry_nome.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_placa.delete(0, tk.END)
    entry_servico.delete("1.0", tk.END)
    entry_data.delete(0, tk.END)
    entry_data.insert(0, datetime.now().strftime("%d/%m/%Y"))

# Criação da janela principal
root = tk.Tk()
root.title("Formulário - Oficina")
root.geometry("400x450")

# Labels e campos de entrada
tk.Label(root, text="Nome do Cliente:").pack(pady=5)
entry_nome = tk.Entry(root, width=40)
entry_nome.pack()

tk.Label(root, text="Modelo do Veículo:").pack(pady=5)
entry_modelo = tk.Entry(root, width=40)
entry_modelo.pack()

tk.Label(root, text="Placa do Veículo:").pack(pady=5)
entry_placa = tk.Entry(root, width=20)
entry_placa.pack()

tk.Label(root, text="Serviço Realizado:").pack(pady=5)
entry_servico = tk.Text(root, height=5, width=40)
entry_servico.pack()

tk.Label(root, text="Data do Serviço:").pack(pady=5)
entry_data = tk.Entry(root, width=20)
entry_data.pack()
entry_data.insert(0, datetime.now().strftime("%d/%m/%Y"))

# Botão para salvar
btn_salvar = tk.Button(root, text="Salvar", command=salvar_dados)
btn_salvar.pack(pady=20)

# Executa o programa
root.mainloop()
