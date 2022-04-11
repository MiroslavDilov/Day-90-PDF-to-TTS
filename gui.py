from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory

from pdf_read import extract_text
from get_tts import make_tts_file

# COLORS
BG_COLOR = "#FBF8F1"
FG_COLOR = "#54BAB9"


class TextToSpeechGUI:
    def __init__(self):
        self.window = Tk()
        # self.window.minsize(width=800, height=600)
        self.window.configure(bg=BG_COLOR)
        self.window.title("PDF to TTS app")

        # Title:
        self.label = Label(text="PDF File to TTS", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 16, 'bold'))
        self.label.grid(row=0, column=1, padx=30, pady=30)

        # PDF Read Button
        self.pdf_label = Label(text="Choose the PDF File's location", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 12, "bold"))
        self.pdf_label.grid(row=1, column=0)

        self.pdf_button = Button(text="Browse", command=self.select_pdf)
        self.pdf_button.grid(row=1, column=1, pady=30)

        # MP3 Path
        self.mp3_label = Label(text="Choose MP3 TTS path", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 12, 'bold'))
        self.mp3_label.grid(row=2, column=0)

        self.mp3_button = Button(text="Browse", command=self.select_mp3_path)
        self.mp3_button.grid(row=2, column=1)

        # Export File Button
        self.export_button = Button(text="Export MP3 File", command=self.export_file)
        self.export_button.grid(row=3, column=1, pady=30)

        # Variablies
        self.pdf_text = ""
        self.mp3_path = ""

        self.window.mainloop()

    def select_pdf(self):
        filetypes = (
            ('PDF', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )

        self.pdf_text = extract_text(filename)
        print(self.pdf_text)

    def select_mp3_path(self):
        self.mp3_path = askdirectory()
        print(self.mp3_path)

    def export_file(self):
        make_tts_file(text=self.pdf_text, path=self.mp3_path)