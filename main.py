import sys
from pathlib import Path
import tkinter as tk
from model.lanzamiento_moneda import simular_moneda
from view.vista import App
from controller.controlador import Controlador

def main():
    root = tk.Tk()
    vista = App(root)
    controlador = Controlador(vista, simular_moneda)
    root.mainloop()

if __name__ == "__main__":
    main()
