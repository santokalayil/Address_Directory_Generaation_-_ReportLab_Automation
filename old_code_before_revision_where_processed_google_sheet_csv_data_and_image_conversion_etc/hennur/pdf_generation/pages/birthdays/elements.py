from reportlab.platypus import PageBegin
from pdf_generation.pages.birthdays.table import generate as table_generate


def generate():
    tables = table_generate()
    elements = [PageBegin()] + tables
    return elements
