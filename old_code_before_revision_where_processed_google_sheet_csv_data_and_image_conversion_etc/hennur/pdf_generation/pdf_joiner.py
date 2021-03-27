import os
from PyPDF2 import PdfFileMerger


def PdfJoiner(list_page_order, source_dir='pdf', filename='pdf.pdf'):
    merger = PdfFileMerger()
    for page in list_page_order:
        merger.append(source_dir + '/' + page)
    merger.write(filename)
    merger.close()
    print("PDF JOIN Successful: ")
