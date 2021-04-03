from reportlab.platypus import PageBegin
from pdf_generation.pages.birthdays.table import generate as table_generate


def generate():
    elements = table_generate()  # [PageBegin()] +
    return elements
