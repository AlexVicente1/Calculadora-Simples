import tkinter as tk

# Função para adicionar números e operadores ao visor
def press(key):
    current = entry.get()  # Pega o que está na tela
    entry.delete(0, tk.END)  # Limpa a tela
    entry.insert(tk.END, current + str(key))  # Adiciona o novo caractere

# Função para calcular o resultado da expressão
def evaluate():
    try:
        result = eval(entry.get())  # Usa eval para calcular a expressão
        entry.delete(0, tk.END)  # Limpa a tela
        entry.insert(tk.END, result)  # Mostra o resultado
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")  # Se der erro, mostra "Erro"

# Função para limpar a tela
def clear():
    entry.delete(0, tk.END)  # Limpa a tela

# Função para apagar o último caractere
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)  # Apaga o último caractere

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")  # Título da janela
root.geometry("400x500")  # Tamanho da janela
root.config(bg="#333")  # Cor de fundo

# Estilo do campo de entrada (onde a expressão é digitada)
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="sunken", justify="right", bg="#eee", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definição dos botões e seus respectivos lugares
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('←', 5, 1)
]

# Criando os botões e atribuindo ações a eles
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#4CAF50", fg="white", command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#f44336", fg="white", command=clear)
    elif text == "←":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#ff9800", fg="white", command=backspace)
    else:
        # Botões numéricos e operadores básicos
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#3e8e41", fg="white", command=lambda key=text: press(key))
    
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Tornando as linhas e colunas redimensionáveis
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Inicia a interface gráfica
root.mainloop()
