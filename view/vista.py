import tkinter as tk
from tkinter import ttk, scrolledtext

class App:
    def __init__(self, root):
        self.root = root
        root.title("Simulación de moneda (MVC)")

        frm_opts = ttk.Frame(root, padding=10)
        frm_opts.grid(row=0, column=0, sticky="ew")

        ttk.Label(frm_opts, text="Selecciona lado:").grid(row=0, column=0, sticky="w")
        self.lado_var = tk.IntVar(value=0)
        ttk.Radiobutton(frm_opts, text="CARA (0)", variable=self.lado_var, value=0).grid(row=0, column=1)
        ttk.Radiobutton(frm_opts, text="CRUZ (1)", variable=self.lado_var, value=1).grid(row=0, column=2)

        self.btn_simular = ttk.Button(frm_opts, text="Simular")
        self.btn_simular.grid(row=0, column=3, padx=8)

        frm_res = ttk.Frame(root, padding=(10,0,10,10))
        frm_res.grid(row=1, column=0, sticky="nsew")

        ttk.Label(frm_res, text="Resultados:").grid(row=0, column=0, sticky="w")
        self.text = scrolledtext.ScrolledText(frm_res, width=60, height=20, wrap=tk.NONE)
        self.text.grid(row=1, column=0, sticky="nsew", pady=5)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        frm_res.rowconfigure(1, weight=1)
        frm_res.columnconfigure(0, weight=1)

    def bind_simular(self, callback):
        """Permite al controlador vincular la acción de simular"""
        self.btn_simular.config(command=callback)

    def mostrar_resultado(self, lado_str, lanzamientos, probabilidades):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, f"Simulando para {lado_str}...\n\n")
        header = f"{'Lanzamientos':>12} | {'Probabilidad (%)':>16}\n"
        self.text.insert(tk.END, header)
        self.text.insert(tk.END, "-" * 32 + "\n")
        for n, prob in zip(lanzamientos, probabilidades):
            self.text.insert(tk.END, f"{n:12} | {prob:16.2f}\n")
