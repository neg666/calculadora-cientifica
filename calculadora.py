import tkinter as tk
from math import *

class CalculadoraCientifica:
    def __init__(self):
        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Científica")
        self.ventana.geometry("400x500")

        # Entrada de texto
        self.entrada = tk.Entry(self.ventana, width=40, font=("Arial", 14))
        self.entrada.pack(padx=10, pady=10)

        # Botones
        self.botones = {}
        for fila in range(7):
            for columna in range(4):
                texto = ""
                if fila == 0:
                    if columna == 0:
                        texto = "C"
                    elif columna == 1:
                        texto = "("
                    elif columna == 2:
                        texto = ")"
                    elif columna == 3:
                        texto = "/"
                elif fila == 1:
                    if columna == 0:
                        texto = "7"
                    elif columna == 1:
                        texto = "8"
                    elif columna == 2:
                        texto = "9"
                    elif columna == 3:
                        texto = "*"
                elif fila == 2:
                    if columna == 0:
                        texto = "4"
                    elif columna == 1:
                        texto = "5"
                    elif columna == 2:
                        texto = "6"
                    elif columna == 3:
                        texto = "-"
                elif fila == 3:
                    if columna == 0:
                        texto = "1"
                    elif columna == 1:
                        texto = "2"
                    elif columna == 2:
                        texto = "3"
                    elif columna == 3:
                        texto = "+"
                elif fila == 4:
                    if columna == 0:
                        texto = "0"
                    elif columna == 1:
                        texto = "."
                    elif columna == 2:
                        texto = "="
                    elif columna == 3:
                        texto = "π"
                elif fila == 5:
                    if columna == 0:
                        texto = "sin"
                    elif columna == 1:
                        texto = "cos"
                    elif columna == 2:
                        texto = "tan"
                    elif columna == 3:
                        texto = "x^2"
                elif fila == 6:
                    if columna == 0:
                        texto = "√"
                    elif columna == 1:
                        texto = "∛"
                    elif columna == 2:
                        texto = "ln"
                    elif columna == 3:
                        texto = "log10"

                boton = tk.Button(self.ventana, text=texto, font=("Arial", 12), width=5, command=self.boton_pulsado)
                boton.grid(row=fila, column=columna, padx=5, pady=5)
                self.botones[texto] = boton

        # Funciones de los botones
        self.operacion = None
        self.numero1 = None
        self.numero2 = None

        def calcular():
            try:
                if self.operacion is None:
                    return
                self.numero2 = float(self.entrada.get())
                resultado = 0
                if self.operacion == "+":
                    resultado = self.numero1 + self.numero2
                elif self.operacion == "-":
                    resultado = self.numero1 - self.numero2
                elif self.operacion == "*":
                    resultado = self.numero1 * self.numero2
                elif self.operacion == "/":
                    resultado = self.numero1 / self.numero2
                elif self.operacion == "x^2":
                    resultado = self.numero1 ** 2
                elif self.operacion == "sin":
                    resultado = sin(self.numero1)
                elif self.operacion == "cos":
                    resultado = cos(self.numero1)
                elif self.operacion == "tan":
                    resultado = tan(self.numero1)
                elif self.operacion == "√":
                    resultado = sqrt(self.numero1)
                elif self.operacion == "∛":
                    resultado = cbrt(self.numero1)
                elif self.operacion == "ln":
                    resultado = log(self.numero1)
                elif self.operacion == "log10":
                    resultado = log10(self.numero1)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(resultado))
            except Exception as e:
                print(e)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Error")

        def boton_pulsado(self, event):
            texto = self.botones[event.widget]["text"]
            if texto in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                self.entrada.insert(tk.END, texto)
            elif texto in ["+", "-", "*", "/"]:
                self.operacion = texto
                self.numero1 = float(self.entrada.get())
                self.entrada.delete(0, tk.END)
            elif texto in ["=", "C"]:
                if texto == "=":
                    calcular()
                else:
                    self.entrada.delete(0, tk.END)
                    self.operacion = None
                    self.numero1 = None
                    self.numero2 = None
            else:
                if self.entrada.get() != "":
                    numero = float(self.entrada.get())
                    if texto == "π":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(pi))
                    elif texto == "sin":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(sin(numero)))
                    elif texto == "cos":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(cos(numero)))
                    elif texto == "tan":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(tan(numero)))
                    elif texto == "√":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(sqrt(numero)))
                    elif texto == "∛":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(cbrt(numero)))
                    elif texto == "ln":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(log(numero)))
                    elif texto == "log10":
                        self.entrada.delete(0, tk.END)
                        self.entrada.insert(0, str(log10(numero)))

        # Bucle principal
        self.ventana.mainloop()

calculadora = CalculadoraCientifica()
