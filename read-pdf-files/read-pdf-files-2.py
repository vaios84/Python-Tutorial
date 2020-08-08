import PyPDF2

def Read(startPage, endPage):
    global text
    text = []
    cleanText = ""
    pdfFileObj = open('CNAVER.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    while startPage <= endPage:
        pageObj = pdfReader.getPage(startPage)
        text += pageObj.extractText()
        startPage += 1
    pdfFileObj.close()
    for myWord in text:
        if myWord != '\n':
            cleanText += myWord
    text = cleanText.split()
    print(text)


Read(0,0)
