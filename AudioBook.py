import win32api
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdf_Reader = PyPDF2.PdfFileReader(book)
pages = pdf_Reader.numPages

bot = pyttsx3.init()
input_rate = int(input("rate:"))
bot.setProperty("rate",input_rate)

for num in range(0,pages):
    page = pdf_Reader.getPage(num)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()    