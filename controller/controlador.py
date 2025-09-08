from tkinter import messagebox

class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.vista.bind_simular(self.on_simular)

    def on_simular(self):
        lado = self.vista.lado_var.get()
        lado_str = "CARA" if lado == 0 else "CRUZ"
        self.vista.btn_simular.config(state="disabled")
        try:
            probabilidades, lanzamientos = self.modelo(lado)
            self.vista.mostrar_resultado(lado_str, lanzamientos, probabilidades)
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar el modelo:\n{e}")
        finally:
            self.vista.btn_simular.config(state="normal")
