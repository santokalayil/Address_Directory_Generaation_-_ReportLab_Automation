from pdf_generation.sub_elements.table import Table
from reportlab.lib import colors

from reportlab.platypus import Image, SimpleDocTemplate, PageBreak  # automatically centers content
# from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch

from pdf_generation.page_settings import *


# PAGE_WIDTH, PAGE_HEIGHT = 140*mm, 215*mm
# page_size = (PAGE_WIDTH, PAGE_HEIGHT)
#
# TOP_MARGIN = 0.5*inch
# BOTTOM_MARGIN = 0.5*inch
# LEFT_MARGIN = 0.5*inch
# RIGHT_MARGIN = 0.5*inch
#
# PAGE_FRAME_SIZE = PAGE_WIDTH - (LEFT_MARGIN + RIGHT_MARGIN)

# from reportlab.rl_config import defaultPageSize
# PAGE_HEIGHT = defaultPageSize[1]; PAGE_WIDTH = defaultPageSize[0]



class Book:
	def __init__(self, filename):
		self.filename = filename


class Page(Book):
	def __init__(self, elems = [], page_size = page_size, filename = 'pdf.pdf'):
		super(Page, self).__init__(filename)
		self.page_size = page_size
		self.elems = elems + [PageBreak()]

	def generate(self):
		pdf = SimpleDocTemplate(filename = self.filename,
								pagesize=self.page_size,
								topMargin=TOP_MARGIN,
								bottomMargin=BOTTOM_MARGIN,
								leftMargin=LEFT_MARGIN,
								rightMargin=RIGHT_MARGIN,
								)
		pdf.build(self.elems)
