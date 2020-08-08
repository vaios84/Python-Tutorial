#!/usr/bin/env python

"""Use pdftotext to extract text from PDFs."""

import pdftotext

with open("CNAVER.pdf") as f:
    pdf = pdftotext.PDF(f)

# Iterate over all the pages
for page in pdf:
    print(page)
