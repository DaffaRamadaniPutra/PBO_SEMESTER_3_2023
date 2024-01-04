import tkinter as tk

def convert():
    try:
        temperature = float(entry.get())
        unit = dropdown.get()

        if unit == "Celsius":
            celsius.set(temperature)
            fahrenheit.set((temperature * 9/5) + 32)
            kelvin.set(temperature + 273.15)
            reamur.set(temperature * 4/5)
        elif unit == "Fahrenheit":
            celsius.set((temperature - 32) * 5/9)
            fahrenheit.set(temperature)
            kelvin.set((temperature - 32) * 5/9 + 273.15)
            reamur.set((temperature - 32) * 4/9)
        elif unit == "Kelvin":
            celsius.set(temperature - 273.15)
            fahrenheit.set((temperature - 273.15) * 9/5 + 32)
            kelvin.set(temperature)
            reamur.set((temperature - 273.15) * 4/5)
        elif unit == "Reamur":
            celsius.set(temperature * 5/4)
            fahrenheit.set(temperature * 9/4 + 32)
            kelvin.set(temperature * 5/4 + 273.15)
            reamur.set(temperature)
    except ValueError:
        celsius.set("")
        fahrenheit.set("")
        kelvin.set("")
        reamur.set("")
        result_label.config(text="Masukkan angka yang valid")

# Membuat window
root = tk.Tk()
root.title("Konversi Suhu")

# Label dan Entry untuk memasukkan suhu
label = tk.Label(root, text="Masukkan suhu:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Dropdown untuk memilih satuan suhu
units = ["Celsius", "Fahrenheit", "Kelvin", "Reamur"]
dropdown = tk.StringVar(root)
dropdown.set(units[0])  # Default unit
menu = tk.OptionMenu(root, dropdown, *units)
menu.pack()

# Tombol untuk konversi
convert_button = tk.Button(root, text="Konversi", command=convert)
convert_button.pack()

# Label untuk menampilkan hasil konversi
result_label = tk.Label(root, text="Hasil Konversi:")
result_label.pack()

# Variabel untuk menyimpan hasil konversi
celsius = tk.StringVar()
fahrenheit = tk.StringVar()
kelvin = tk.StringVar()
reamur = tk.StringVar()

# Menampilkan hasil konversi
result_display = tk.Label(root, textvariable=celsius)
result_display.pack()
result_display = tk.Label(root, textvariable=fahrenheit)
result_display.pack()
result_display = tk.Label(root, textvariable=kelvin)
result_display.pack()
result_display = tk.Label(root, textvariable=reamur)
result_display.pack()

root.mainloop()
