import pyttsx3
import PyPDF2

book = open('it.pdf', 'rb')
pdfread = PyPDF2.PdfFileReader(book)
pages = pdfread.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfread.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()