from .splitter import pdf_splitter

# save individual pages as seperate pdfs

from PyPDF2 import PdfFileReader
import os

def pdf_2_individual_pages(pdf_url, location=False, until=False):
    with open(pdf_url, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        print(f"The total number of pages in the pdf document is {pdf_reader.numPages}")
        num_pages = pdf_reader.numPages
    until = until if until else num_pages
    for i in range(until):
        file_name = f"page_{i+1}.pdf"
        output_file = os.path.join(location, file_name) if location else file_name
        pdf_splitter(file_url=pdf_url, pages=i, output_file=output_file)

# from i in 
