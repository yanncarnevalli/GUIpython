import tkinter as tk

# Funções para impedir de digitar no visor
def liberarVisor():
    visor.config(state="normal")

def travarVisor():
    visor.config(state="readonly")

# Inserir os números
def digitar(numero):
    liberarVisor()
    visor.insert(tk.END, numero)
    travarVisor()

# Limpar visor e zerar as variaveis
def limpar():
    global n1, n2, ope, resultado
    liberarVisor()
    visor.delete(0, tk.END)
    travarVisor()

    n1 = 0
    n2 = 0
    ope = ""
    resultado = 0

# Função de apagar um numero
def retirar():
    liberarVisor()
    visor.delete(len(visor.get()) - 1, tk.END)
    travarVisor()

# Inserir o ponto e impedir de colocar 2 pontos
def ponto():
    if "." not in visor.get():
        liberarVisor()
        visor.insert(tk.END, ".")
        travarVisor()
# Receber o primeiro número e o sinal
def operacao(sinal):
    global n1, ope
    n1 = float(visor.get())
    liberarVisor()
    visor.delete(0, tk.END)
    travarVisor()

    liberarVisor()
    visor.insert(tk.END, sinal)
    ope = visor.get()
    visor.delete(0, tk.END)
    travarVisor()

# Receber o segundo número e calcular
def mostrar():
    global n1, n2, resultado

    if visor.get() == "" or ope == "":
        return

    n2 = float(visor.get())
    
    match ope:
        case "+":
            resultado = n1 + n2
        case "-":
            resultado = n1 - n2
        case "x":
            resultado = n1 * n2
        case "÷":
            if n2 == 0:
                resultado = "Indefinido: não é possivel dividir por 0"
            else:
                resultado = n1 / n2

    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado)

    liberarVisor()
    visor.delete(0, tk.END)
    visor.insert(tk.END, resultado)
    travarVisor()
    
janela = tk.Tk()
janela.title("Calculadora")

visor = tk.Entry(janela, width=35, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=6, pady=6, ipady=8)

botao_c = tk.Button(janela, text="C", width=6, height=2, command=limpar)
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_r = tk.Button(janela, text="⌫", width=6, height=2, command=retirar)
botao_r.grid(row=1, column=1, padx=2, pady=2)

botao_divisao = tk.Button(janela, text="÷", width=6, height=2, command=lambda: operacao("÷"))
botao_divisao.grid(row=1, column=2, padx=2, pady=2)

botao_multi = tk.Button(janela, text="x", width=6, height=2, command=lambda: operacao("x"))
botao_multi.grid(row=1, column=3, padx=2, pady=2)

botao_7 = tk.Button(janela, text="7", width=6, height=2, command=lambda: digitar("7"))
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, height=2, command=lambda: digitar("8"))
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=6, height=2, command=lambda: digitar("9"))
botao_9.grid(row=2, column=2, padx=2, pady=2)

botao_menos = tk.Button(janela, text="-", width=6,  height=2, command=lambda: operacao("-"))
botao_menos.grid(row=2, column=3, padx=2, pady=2)

botao_4 = tk.Button(janela, text="4", width=6, height=2, command=lambda: digitar("4"))
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, height=2, command=lambda: digitar("5"))
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=6, height=2, command=lambda: digitar("6"))
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_soma = tk.Button(janela, text="+", width=6, height=2, command=lambda: operacao("+"))
botao_soma.grid(row=3, column=3, padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=6, height=2, command=lambda: digitar("1"))
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=6, height=2, command=lambda: digitar("2"))
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=6, height=2, command=lambda: digitar("3"))
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_0 = tk.Button(janela, text="0", width=14, height=2, command=lambda: digitar("0"))
botao_0.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

botao_p = tk.Button(janela, text=".", width=6, height=2, command=ponto)
botao_p.grid(row=5, column=2, padx=2, pady=2)

botao_ig = tk.Button(janela, text="=", width=6, height=5, command=mostrar )
botao_ig.grid(row=4, column=3, rowspan=2, padx=2, pady=2)

janela.mainloop()