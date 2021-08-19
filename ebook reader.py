import pyttsx3
import PyPDF2

hikaye = open("Stock Market Wizards_ Interviews with America's Top Stock Traders - PDF Room.pdf", "rb")
pdfOkuyucu = PyPDF2.PdfFileReader(hikaye)

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voices", voices[0].id)
for sayfa_numarasi in range (0, pdfOkuyucu.numPages):
    sayfa= pdfOkuyucu.getPage(sayfa_numarasi)
    yazi = sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()
