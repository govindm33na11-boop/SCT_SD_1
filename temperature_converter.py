import tkinter as tk
from tkinter import messagebox

def convert_temp():
    try:
        temp_val = float(entry_temp.get())
        scale = scale_var.get()
        
        if scale == "Celsius":
            c = temp_val
            f = (temp_val * 9/5) + 32
            k = temp_val + 273.15
        elif scale == "Fahrenheit":
            c = (temp_val - 32) * 5/9
            f = temp_val
            k = c + 273.15
        elif scale == "Kelvin":
            c = temp_val - 273.15
            f = (c * 9/5) + 32
            k = temp_val
            
        result_label.config(
            text=f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K",
            fg="#00f2fe"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature value.")


root = tk.Tk()
root.title("SCT_SD_1 - Temperature Converter")
root.geometry("400x480")
root.config(bg="#0f172a") 
root.minsize(360, 440)     


root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)


header_label = tk.Label(root, text="🌡️ Temperature Converter", font=("Segoe UI", 16, "bold"), bg="#0f172a", fg="#f8fafc")
header_label.pack(pady=(25, 15))


card_frame = tk.Frame(root, bg="#1e293b", bd=0, relief="flat")
card_frame.pack(padx=25, fill="both", expand=True, pady=(0, 25))


tk.Label(card_frame, text="Enter Temperature:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="#94a3b8").pack(anchor="w", padx=20, pady=(20, 5))
entry_temp = tk.Entry(card_frame, font=("Segoe UI", 12), justify="center", bg="#0f172a", fg="#f8fafc", insertbackground="white", bd=0, relief="flat")
entry_temp.pack(padx=20, fill="x", ipady=8, pady=(0, 15))


tk.Label(card_frame, text="Select Source Scale:", font=("Segoe UI", 11, "bold"), bg="#1e293b", fg="#94a3b8").pack(anchor="w", padx=20, pady=(0, 5))

scale_var = tk.StringVar(value="Celsius")
scale_menu = tk.OptionMenu(card_frame, scale_var, "Celsius", "Fahrenheit", "Kelvin")
scale_menu.config(font=("Segoe UI", 11), bg="#0f172a", fg="#f8fafc", activebackground="#334155", activeforeground="#f8fafc", relief="flat", highlightthickness=0)
scale_menu["menu"].config(font=("Segoe UI", 10), bg="#1e293b", fg="#f8fafc")
scale_menu.pack(padx=20, fill="x", pady=(0, 20))


convert_btn = tk.Button(card_frame, text="Convert Temperature", font=("Segoe UI", 11, "bold"), bg="#0ea5e9", fg="#ffffff", activebackground="#0284c7", activeforeground="white", relief="flat", cursor="hand2", command=convert_temp)
convert_btn.pack(padx=20, fill="x", ipady=10, pady=(0, 15))


result_frame = tk.Frame(card_frame, bg="#0f172a", bd=0, relief="flat")
result_frame.pack(padx=20, fill="x", pady=(0, 20))

result_label = tk.Label(result_frame, text="Converted results will appear here", font=("Segoe UI", 11, "bold"), bg="#0f172a", fg="#64748b", justify="center")
result_label.pack(padx=10, pady=14)

root.mainloop()