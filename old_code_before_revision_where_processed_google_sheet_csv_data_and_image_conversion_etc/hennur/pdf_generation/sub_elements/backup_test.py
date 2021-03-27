#
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch, mm
# styles = getSampleStyleSheet()
#
# Title = "DIRECTORY - 2020"
# page_info = "Directory 2020 - MCC Hennur"
#
# file_name = 'simple_doc_pdf.pdf'
# PAGE_WIDTH, PAGE_HEIGHT = 140*mm, 215*mm
# page_size = (PAGE_WIDTH, PAGE_HEIGHT)
# TOP_MARGIN, BOTTOM_MARGIN = 0.5*inch, 0.5*inch
# LEFT_MARGIN, RIGHT_MARGIN = 0.5*inch, 0.5*inch
#
#
# def master_page_1(canvas, doc):
#     canvas.saveState()
#     canvas.setFont('Times-Bold', 16)
#     canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
#     canvas.setFont('Times-Roman', 9)
#     canvas.drawString(0.5 * inch, 0.3 * inch, f"First Page / {page_info}")
#     canvas.restoreState()
#     canvas.showPage()  # applying page break
#
#
# def master_page_2(canvas, doc):
#     canvas.saveState()
#     canvas.setFont('Times-Roman', 9)
#     canvas.drawString(0.5 * inch, 0.3 * inch, f"Page {doc.page} {page_info}")
#     canvas.restoreState()
#
#
# def vicar_message():
#     paragraph_space = Spacer(1, 0.2*inch)
#     paragraphs = [paragraph_space, ]
#     message_heading_style = styles["Heading1"]
#     heading_of_message = Paragraph("From Vicar's Desk", message_heading_style)
#     paragraphs.append(heading_of_message)
#     with open("message_vicar.txt", 'r') as txt_file_message_of_vicar:
#         message_of_vicar = txt_file_message_of_vicar.readlines()
#     message_paragraph_style = styles["Normal"]
#     for line_of_message in message_of_vicar:
#         p = Paragraph(line_of_message, message_paragraph_style)
#         paragraphs.append(p)
#         paragraphs.append(paragraph_space)
#     paragraphs.append(PageBreak())
#     return paragraphs
#
#
# def create_document():
#     doc = SimpleDocTemplate(filename=file_name,
#                             pagesize=page_size,
#                             topMargin=TOP_MARGIN,
#                             bottomMargin=BOTTOM_MARGIN,
#                             leftMargin=LEFT_MARGIN,
#                             rightMargin=RIGHT_MARGIN)
#     story = []
#     story.append(PageBreak())  # to skip other side of first page
#     story += vicar_message()  # adding vicar message
#     story += vicar_message()  # adding vicar message
#     doc.build(story, onFirstPage=master_page_1, onLaterPages=master_page_2)
#
#
# create_document()