import tkinter as tk
from tkinter import ttk

class MedicalExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Expert App")

        # Create a style for a more modern look
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TCheckbutton', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))

        # Create a frame for better organization
        frame = ttk.Frame(root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Add a title label
        title_label = ttk.Label(frame, text="Welcome to the Medical Expert App", style='TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Add instructions
        instruction_label = ttk.Label(frame, text="Please select any symptoms you are experiencing:", style='TLabel')
        instruction_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Symptoms checkboxes
        self.cough_var = tk.BooleanVar()
        self.cough_checkbox = ttk.Checkbutton(frame, text="Cough", variable=self.cough_var, style='TCheckbutton')
        self.cough_checkbox.grid(row=2, column=0, padx=10)

        self.fever_var = tk.BooleanVar()
        self.fever_checkbox = ttk.Checkbutton(frame, text="Fever", variable=self.fever_var, style='TCheckbutton')
        self.fever_checkbox.grid(row=2, column=1, padx=10)

        self.headache_var = tk.BooleanVar()
        self.headache_checkbox = ttk.Checkbutton(frame, text="Headache", variable=self.headache_var, style='TCheckbutton')
        self.headache_checkbox.grid(row=2, column=2, padx=10)

        # Diagnose button
        self.diagnose_button = ttk.Button(frame, text="Diagnose", command=self.diagnose, style='TButton')
        self.diagnose_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Result label
        self.result_label = ttk.Label(frame, text="", style='TLabel')
        self.result_label.grid(row=4, column=0, columnspan=3)

    def diagnose(self):
        cough = self.cough_var.get()
        fever = self.fever_var.get()
        headache = self.headache_var.get()

        # Simple rule-based logic using if-else statements
        if cough and fever:
            result = "You may have the flu."
        elif cough and not fever and headache:
            result = "You may have a cold."
        elif not cough and fever and headache:
            result = "You may have a migraine."
        else:
            result = "You seem to be healthy."

        # Update the result label
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalExpertSystem(root)
    root.mainloop()
