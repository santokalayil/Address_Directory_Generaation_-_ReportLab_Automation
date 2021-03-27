
def generate_paragraph_flowable(famid):
    from pdf_generation.sub_elements.data import family_common_data
    from reportlab.platypus import Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    family_general = family_common_data(famid)
    family_general_para = family_general['paragraph']
    # family_head = family_general['head']
    para_style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=8,)
    full_paragraph = Paragraph(family_general_para, style=para_style)
    return full_paragraph

#
# f'<u>{"CURRENT ADDRESS".title()}</u>: ' + self.cur_addr +
# f'<br />Email: {self.email}'
# f'<br /><u>{"Native Place Address & Parish".title()}</u>: ' + self.nat_addr +
# f'<br /> <u>Native Parish</u>: {self.na_par}<br /><u>Diocese</u>: {self.na_dio}'



#
#
# from pdf_generation.sub_elements.table import Table, colors
# from pdf_generation.sub_elements.image import FamImage
# from pdf_generation.sub_elements.page import PAGE_FRAME_HEIGHT, PAGE_FRAME_WIDTH
# # print(PAGE_FRAME_SIZE)
#
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.platypus import Spacer, TableStyle, Paragraph
# from reportlab.platypus import Table as RPTable
# from reportlab.lib.units import mm, inch
#
#
#
#
#
#
# class Box:
#     def __init__(self):
#         self.table_data = table_data
#         self.img_path = img_path
#         self.heading = heading
#         self.cur_addr = cur_addr
#         self.nat_addr = nat_addr
#         self.email = email
#         self.na_par = na_par
#         self.na_dio = na_dio
#
#     def table(self):
#         return Table(self.table_data)
#
#     def image(self):
#         im = FamImage(self.img_path)
#         return im.generate()
#
#     def header(self):
#         head_box = RPTable([[self.heading]], colWidths=[PAGE_FRAME_WIDTH], rowHeights=[PAGE_FRAME_HEIGHT])
#         head_box_style = TableStyle(
#             [
#                 ("BACKGROUND", (0, 0), (-1, -1), colors.Color(0.5, 0.1, 0.6)),
#                 ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
#                 ("TOPPADDING", (0, 0), (-1, -1), 0),
#                 ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
#                 ("LEFTPADDING", (0, 0), (-1, -1), 7),
#                 ("RIGHTPADDING", (0, 0), (-1, -1), 0),
#                 ("ALIGN", (0, 0), (-1, -1), "LEFT"),
#                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
#
#             ]
#         )
#         head_box.setStyle(head_box_style)
#         return head_box
#
#     def cur_adr_table(self):
#         para_style = ParagraphStyle(
#             name='Normal',
#             fontName='oswald_light',
#             fontSize=8,
#         )
#         cur_adr_para = Paragraph(
#             f'<u>{"CURRENT ADDRESS".title()}</u>: ' + self.cur_addr +
#             f'<br />Email: {self.email}'
#             f'<br /><u>{"Native Place Address & Parish".title()}</u>: ' + self.nat_addr +
#             f'<br /> <u>Native Parish</u>: {self.na_par}<br /><u>Diocese</u>: {self.na_dio}',
#             style=para_style)
#         cur_adr_table = def_table([[cur_adr_para]])
#         cur_adr_table_style = TableStyle(
#             [
#                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
#                 ("ALIGN", (0, 0), (-1, -2), "CENTER"),  # -2 for only for address column and not for img col
#
#                 ("BOTTOMPADDING", (1, 0), (-1, -1), 20),
#                 ("TOPPADDING", (1, 0), (-1, -1), 20),
#                 ("LEFTPADDING", (0, 0), (-1, -1), 15),
#                 # ("FONTNAME", (0,0), (-1, -1), "Times-Roman"), # header font
#                 # ("FONTSIZE", (0,0), (-1, -1), 5),
#                 # ("BACKGROUND", (0,0), (-1, -1), colors.yellow),
#             ]
#         )
#         cur_adr_table.setStyle(cur_adr_table_style)
#         return cur_adr_table
#
#     def photo_address(self):
#         pht_img_tbl = def_table(
#             [[self.image(), self.cur_adr_table()]],
#             colWidths=[(PAGE_FRAME_SIZE * 0.35), (PAGE_FRAME_SIZE * 0.65)],
#         )
#         pht_img_style = TableStyle(
#             [
#                 ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
#                 ("ALIGN", (0, 0), (-1, -2), "CENTER"),  # -2 for only for address column and not for img col
#                 ("BOTTOMPADDING", (1, 0), (-1, -1), 0),
#                 ("TOPPADDING", (1, 0), (-1, -1), 0),
#                 ("LEFTPADDING", (0, 0), (-1, -1), 0),
#                 # ("FONTNAME", (0,0), (-1, -1), "Times-Roman"), # header font
#                 # ("FONTSIZE", (0,0), (-1, -1), 5),
#                 # ("BACKGROUND", (1,0), (-1, -1), colors.Color(0.2,0.2,0.3)),
#             ]
#         )
#         pht_img_tbl.setStyle(pht_img_style)
#
#         return pht_img_tbl
#
#     def generate(self):
#         box = def_table([
#             [self.header()],
#             [self.photo_address()],
#             # [self.native_parish_table()],
#             [self.table()],
#         ])
#         box_style = TableStyle(
#             [
#                 # ("BACKGROUND", (0,0), (-1, -1), colors.Color(0.9,0.9,0.3)),
#                 ("TOPPADDING", (0, 0), (-1, -1), 0),
#                 ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
#                 ("LEFTPADDING", (0, 0), (-1, -1), 0),
#                 ("RIGHTPADDING", (0, 0), (-1, -1), 0),
#                 # ("TEXTCOLOR", (0,0), (-1, -1), colors.white),
#             ]
#         )
#         box.setStyle(box_style)
#         return box
#
#     # return [self.image(),
#     # 			Spacer(width = 1, height = 4),
#     # 			self.table()]
#
# # table = def_table([[self.image()]])