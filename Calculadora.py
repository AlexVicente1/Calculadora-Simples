# Importando a biblioteca tkinter para criar a interface gráfica
import tkinter as tk

# Função que vai ser chamada quando um botão for pressionado
def button_click(value):
    current = entry.get()  # Obtém o texto que está na tela de entrada
    entry.delete(0, tk.END)  # Apaga o texto atual
    entry.insert(tk.END, current + str(value))  # Insere o novo valor no campo de entrada

# Função para calcular a expressão
def calculate():
    try:
        result = eval(entry.get())  # A função eval avalia a expressão inserida
        entry.delete(0, tk.END)  # Limpa o campo de entrada
        entry.insert(tk.END, result)  # Exibe o resultado
    except Exception as e:
        entry.delete(0, tk.END)  # Limpa a entrada caso aconteça algum erro
        entry.insert(tk.END, "Erro")  # Exibe "Erro" em caso de erro na operação

# Função para apagar tudo
def clear():
    entry.delete(0, tk.END)  # Apaga tudo que está na tela de entrada

# Criando a janela principal da calculadora
root = tk.Tk()
root.title("Calculadora Simples")

# Criando o campo de entrada onde os números e resultados vão aparecer
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Criando os botões da calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Adicionando os botões à interface
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Criando o botão de limpar
clear_button = tk.Button(root, text="C", width=10, height=3, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Iniciando a interface gráfica
root.mainloop()
