import pyttsx3
from tkinter import *
from tkinter import filedialog, messagebox
import PyPDF2
from Crypto.Cipher import AES

key = "1234"

speaker = pyttsx3.init()


def upload():
    file_path = filedialog.asksaveasfilename(
        filetypes=[("Text files", "*.pdf"), ("All files", "*.*")])
    read_pdf = PyPDF2.PdfReader(file_path, strict=False)
    print(read_pdf)

    pages = len(read_pdf.pages)

    for page_num in range(pages):
        text = read_pdf.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', '    ')
        print(clean_text)
        text_to_read.insert(INSERT, f"{clean_text}\n")
        text_to_read.tag_add("text", "1.0", END)
        text_to_read.tag_configure("text", background="black", foreground="green")
        window.update()

        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[1].id)
        new_voice_rate = 145
        speaker.setProperty('rate', new_voice_rate)
        speaker.say(clean_text)
        speaker.runAndWait()
        text_to_read.delete("1.0", END)

    def decrypt(t):
        k = bytes(key, "UTF-8")
        cipher = AES.new(k, AES.MODE_CBC)

        print("Decryption Cipher: ")
        return cipher.decrypt(t).decode("UTF-8")

    return decrypt(clean_text)


window = Tk()
window.title("AudioRead")
window.geometry("400x400")
window.config()
label = Label(text="Welcome to AudioRead App! Please: ", font=("bahnschrift", 10))
label.pack()
button = Button(text="Upload Text", command=upload)
button.pack()
text_to_read = Text(window, wrap=WORD, height=15, width=35)
text_to_read.pack()

window.mainloop()
