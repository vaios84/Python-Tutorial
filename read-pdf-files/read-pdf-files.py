import PyPDF2

pdfFile = "CNAVER.pdf"

pdfRead = PyPDF2.PdfFileReader(pdfFile)
page = pdfRead.getPage(0)
pageContent = page.extractText()
print(pageContent)
