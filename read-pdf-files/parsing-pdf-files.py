from PyPDF2 import PdfFileReader, PdfFileWriter
from math import log

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("words-by-frequency.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)


def extractionOfText():
	file_path = 'CNAVER.pdf'
	pdf = PdfFileReader(file_path)

	with open('Notes.txt', 'w') as f:
	    for page_num in range(pdf.numPages):
		# print('Page: {0}'.format(page_num))
		pageObj = pdf.getPage(page_num)

		try:
		    txt = pageObj.extractText()
		    print(''.center(100, '-'))
		except:
		    pass
		else:
		    f.write('Page {0}\n'.format(page_num+1))
		    f.write(''.center(100, '-'))
		    f.write(u'<{0}/>'.format(txt).encode('ascii', 'ignore').decode('ascii'))
	    f.close()


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


extractionOfText()
d = open("Notes.txt", "r")
#print(d.read())
#print(infer_spaces(d.read())) 
