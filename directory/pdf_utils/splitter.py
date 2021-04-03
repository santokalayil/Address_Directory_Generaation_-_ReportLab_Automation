# pip install PyPDF2
# https://www.codeforests.com/2020/08/08/how-to-split-or-merge-pdf-files/

from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_splitter(file_url, pages, output_file):
    input_pdf = PdfFileReader(file_url)
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(pages))
    with open(output_file, "wb") as output_stream:
        output.write(output_stream)
