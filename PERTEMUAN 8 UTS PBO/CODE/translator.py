from googletrans import Translator
import tkinter as tk

def translate_text():
    text_to_translate = entry.get()
    translator = Translator()

    try:
        translation_en = translator.translate(text_to_translate, dest='en')
        translation_mn = translator.translate(text_to_translate, dest='mn')
        translation_no = translator.translate(text_to_translate, dest='no')

        translated_text_en.set(translation_en.text)
        translated_text_mn.set(translation_mn.text)
        translated_text_no.set(translation_no.text)

    except Exception as e:
        translated_text_en.set("Error")
        translated_text_mn.set("Error")
        translated_text_no.set("Error")
        print(f"Error: {e}")

root = tk.Tk()
root.title("Translator")

label = tk.Label(root, text="Masukkan teks:")
label.pack()
entry = tk.Entry(root)
entry.pack()

translate_button = tk.Button(root, text="Terjemahkan", command=translate_text)
translate_button.pack()

translated_text_en = tk.StringVar()
translated_text_mn = tk.StringVar()
translated_text_no = tk.StringVar()

label_en = tk.Label(root, text="Inggris:")
label_en.pack()
result_display_en = tk.Label(root, textvariable=translated_text_en)
result_display_en.pack()

label_mn = tk.Label(root, text="Mongolia:")
label_mn.pack()
result_display_mn = tk.Label(root, textvariable=translated_text_mn)
result_display_mn.pack()

label_no = tk.Label(root, text="Norwegia:")
label_no.pack()
result_display_no = tk.Label(root, textvariable=translated_text_no)
result_display_no.pack()

root.mainloop()
