import sys
from pathlib import Path
import tkinter as tk
from model.lanzamiento_moneda import simular_moneda
from view.vista import App

def main():
    root = tk.Tk()
    app = App(root, simular_moneda)  
    root.mainloop()

if __name__ == "__main__":
    main()
