import os
from reportlab.platypus import (Paragraph, Spacer, CondPageBreak, FrameBreak, PageBegin,
                                NextPageTemplate, PageBreak, PageTemplate)
# from reportlab.lib.units import inch, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from pdf_generation.page_settings import *
from pdf_generation.fonts import register_font
from pdf_generation.sub_elements.masters import (document, master_1, master_2, master_3, master_4,
                                                 single_column_frame_template,
                                                 double_column_frame_template,
                                                 double_row_frame_template)
from pdf_generation.sub_elements.templates import vicar_message, history_of_parish
from pdf_generation.pages.families import generate as families_elements
from pdf_generation.pages.birthdays.elements import generate as birthdays_elements

# registering fonts
register_font()

styles = getSampleStyleSheet()

doc = document()  # document

# master pages templates
empty_page = master_1
message_master = master_2
history_master = master_3
address_master = master_4

# frames

single_frame = single_column_frame_template(doc, id='normal')
dual_column_frame = double_column_frame_template(doc, ids=['col1', 'col2'])
dual_row_frame = double_row_frame_template(doc, ids=['box1', 'box2'])

book_title_style = ParagraphStyle(name='normal',
                                  alignment=1,
                                  fontSize=24,
                                  textColor=colors.darkslategray
                                  )

Elements = []  # Elements Flow List
# book_title_style.alignment=1
book_title = Paragraph(Title, book_title_style)

# section ids
title_section_id = 'Title'
photos_section_id = 'PhotoSection'  # Pope, Catholicos, Makkariios, Holy Epicopal Synod, The Late Prelates of the Syro Malankara Cathoic Church
# Bangalore District Priests, Former Vicars, Former Assistant Vicars,
history_section_id = 'History' # parish  history
message_section_id = 'Messages'  # From the Vicar's Desk,
parishes_and_convenet_id = ''  # Our Parishes  and Convents in Bangalore,

# Priests from Our Parish - Name, Address, Email ID, Phone, Date of Birth, Date of Ordination, Feast Day
# INDEX
address_section_id = 'Addresses'
birthday_section_id = 'Birthdays'
# Wedding Anniversaries

# Title Page First
Elements.append(NextPageTemplate(title_section_id))
Elements.append(Spacer(1, PAGE_HEIGHT * 0.3))
Elements.append(book_title)  # title of the book first page

Elements.append(PageBreak())  # skipping the other side of first title page

# Messages Pages
Elements += [NextPageTemplate(message_section_id), PageBreak()]
Elements += vicar_message()

# History Pages
Elements += [NextPageTemplate(history_section_id), PageBreak()] + history_of_parish()

# Address Pages
Elements += [NextPageTemplate(address_section_id), PageBreak()] + families_elements()

# Birthday Pages
Elements += [NextPageTemplate(birthday_section_id), PageBreak()] + birthdays_elements()


doc.addPageTemplates([PageTemplate(id=title_section_id, frames=single_frame, onPage=empty_page),
                      PageTemplate(id=message_section_id, frames=single_frame, onPage=message_master),
                      PageTemplate(id=history_section_id, frames=dual_column_frame, onPage=history_master),
                      PageTemplate(id=address_section_id, frames=dual_row_frame, onPage=address_master),
                      PageTemplate(id=birthday_section_id, frames=single_frame, onPage=empty_page)
                      ])
# start the construction of the pdf
doc.build(Elements)



