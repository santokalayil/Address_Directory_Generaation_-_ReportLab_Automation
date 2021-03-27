from reportlab.lib import colors

# intra-modular imports
from pdf_generation.sub_elements.table import Table
from pdf_generation.sub_elements.page import Page
from pdf_generation.sub_elements.data import Data, getFam
from pdf_generation.sub_elements.box import Box

from pdf_generation.pdf_joiner import PdfJoiner


from reportlab.platypus import Image, SimpleDocTemplate, Spacer  # automatically centers content
# from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm

# DATA FRAME
import pandas as pd


def page_generate(ids, filename):
	merg = pd.read_csv('csv/merg.csv')
	mem = pd.read_csv('csv/members.csv')
	header = ["Name", "Relationship", "Proffession", "Phone", "DOB", "DOM/DOO", "Blood"]

	def box_generate(famid):
		com_head, ca_ls, em, na_ls, na_par, na_dio, fam, img_link = getFam(famid, merg, mem)
		data= [header,] + fam

		data = Data(data).process_data()

		box = Box(table_data = data,
			img_path = img_link,
			heading = com_head,
			cur_addr = ca_ls,
			email = em,
			nat_addr = na_ls,
			na_par = na_par,
			na_dio = na_dio,
			)
		return box.generate()

	try:
		box1 = box_generate(ids[0])
		box2 = box_generate(ids[1])
		page = Page(elems = [
			box1, Spacer(1, 35), box2],
			filename = 'pdf/'+filename
			)
	except:
		box1 = box_generate(ids[0])
		page = Page(elems = [
			box1, Spacer(1, 35)],
			filename = 'pdf/'+filename
			)


	page.generate()


# FIRSTLY RUN data_preprocess.py then DO THIS
famids = list(pd.read_csv('csv/merg.csv')['famid'])

print(100* "=")
###############################################################################

to_remove_photoids = [16, ]   ##### HERE WE USE TO REMOVE FAMILYE IDS
print(f"REMOVING ID {to_remove_photoids} as per ids found in photo names.....")
temp = [i for i in famids if i not in to_remove_photoids]

famids = temp
#############################################################################

print(100* "=")
# # print(famids)


# Grouping into tuples of two ids as two boxes in one page
ls = famids
comb_ls = [(i, famids[famids.index(j)+1]) for i, j in zip(ls, ls) if j != famids[-1]]
#print(comb_ls)
even = [i for i in range(len(comb_ls)) if i%2 == 0]
#################################################################

list_pdf_pages = []
for e in even:
	ids = comb_ls[e]
	filename = f'{"-".join([str(Id) for Id in ids])}.pdf'
	list_pdf_pages.append(filename)
	page_generate(ids, filename)
# print(list_pdf_pages)

PdfJoiner(list_pdf_pages)

#print(0/2)
