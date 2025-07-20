import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator


translator = Translator()

def translate_text():
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter text to translate")
        return
    
    try:
        result = translator.translate(input_text, src=src_lang, dest=dest_lang)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, result.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

languages = {
    'English': 'english',
    'French': 'french',
    'Spanish': 'spanish',
    'German': 'german',
    'Chinese (Simplified)': 'chiense',
    'Japanese': 'japanese',
    'Hindi':'hindi',
    
}

root = tk.Tk()
root.title("Language Translation Tool")

src_lang_var = tk.StringVar(value='en')
dest_lang_var = tk.StringVar(value='fr')

tk.Label(root, text="Enter Text:").grid(row=0, column=0, padx=5, pady=5)
text_input = tk.Text(root, height=8, width=50)
text_input.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Source Language:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
src_lang_menu = ttk.Combobox(root, textvariable=src_lang_var, values=list(languages.values()))
src_lang_menu.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Target Language:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
dest_lang_menu = ttk.Combobox(root, textvariable=dest_lang_var, values=list(languages.values()))
dest_lang_menu.grid(row=3, column=1, padx=5, pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="Translated Text:").grid(row=5, column=0, padx=5, pady=5)
text_output = tk.Text(root, height=8, width=50)
text_output.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
