from . import section_ids
from .settings import PAGE_FRAME_WIDTH, PAGE_FRAME_HEIGHT

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate, FrameBreak




Elements = []
Elements.append(NextPageTemplate(section_ids.dual_row_family_id))  # marking section id to identify master page and style



from reportlab.platypus import Table as RLTable
from reportlab.platypus import Spacer
from reportlab.platypus import TableStyle
from reportlab.lib import colors

from .text import data
color_yellow = colors.Color(0.9, 0.9, 0.5)
color_light = colors.Color(0.7, 0.8, 0.9)
color_general = colors.Color(0.2, 0.3, 0.4)
# color_dark = 
color_deep_dark = colors.Color(0.2, 0.2, 0.3)
color_extra_light = colors.Color(0.9, 0.94, 0.98)
# color_extra_light = colors.Color(1, 1, 1)
color_white = colors.Color(1, 1, 1)

def produce_heading(text):
    heading_title_table = RLTable([[text.upper(),]], colWidths=[PAGE_FRAME_WIDTH])
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color_general),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.whitesmoke),
        ])
    )
    return [Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), heading_title_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]

def horizontal_row(height=3, width=PAGE_FRAME_WIDTH, color=colors.Color(0.2, 0.3, 0.4)):
    row_table = RLTable([["",]], colWidths=[width], rowHeights=[height])
    row_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color),
        ])
    )
    return [Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), row_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]

def ribbon(height=10, width=PAGE_FRAME_WIDTH, color=color_light, space_before=0):
    row_table = RLTable([["",]], colWidths=[width], rowHeights=[height])
    row_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), color),
        ])
    )
    return [row_table]
    # return [Spacer(width=PAGE_FRAME_WIDTH, height=space_before, isGlue=True), row_table, Spacer(width=PAGE_FRAME_WIDTH, height=2, isGlue=True)]


family_title_background = colors.Color(0.5, 0.1, 0.6)
family_title_text_color = colors.white # colors.whitesmoke

def family_title_section(fam_id, family_head):
    text = f'''{fam_id}. {family_head}'''
    heading_title_table = RLTable([[text.upper(),]], colWidths=[PAGE_FRAME_WIDTH], rowHeights=[PAGE_FRAME_HEIGHT/25])
    heading_title_table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), family_title_background),
            ("TEXTCOLOR", (0, 0), (-1, -1), family_title_text_color),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 7),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ])
    )
    return [heading_title_table] # Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True), 

def address_section(fam_id):
    para_table = RLTable([
        [common_data['text']['current_address']],
            #[common_data['text']['email']],
            [common_data['text']['native_address']],
            [common_data['text']['native_parish']],
            [common_data['text']['diocese']],
            ])
    return para_table

Elements += family_title_section(fam_id=12, family_head="Thomas K J")
Elements += ribbon(color=color_light)
Elements.append(FrameBreak())
Elements += ribbon(height=200, width=PAGE_FRAME_WIDTH, color=color_yellow)
Elements += ribbon(height=200, width=PAGE_FRAME_WIDTH, color=color_yellow)
# # =========================== Header Resume =================================

# # adding white space above everything to move the content towards bottom so as to reduce the space in the bottom
# # Elements += ribbon(height=20, width=PAGE_FRAME_WIDTH, color=color_white)
# Elements += ribbon(height=1, width=PAGE_FRAME_WIDTH, color=color_extra_light, space_before=0) # the line

# title = data['title']
# full_name=title['full_name']
# job_title=title['job_title']
# contact = data['contact']
# contact_text = f'''{contact['email']}\n{contact['phone']}\n{contact['address']}\n{contact['website']}'''

# title_table = RLTable(
#     [
#         [full_name.upper(), contact_text],
#         [job_title.title(), ''],
#     ],
#     colWidths=[PAGE_FRAME_WIDTH/2 for i in range(2)],
#     rowHeights=[60,20]
# ) 
# title_table.setStyle(
#     TableStyle([
#         ('BACKGROUND', (0, 0), (-1, -1), color_white),
#         ("ALIGN", (0,0), (-1, -1), "LEFT"), # align only the header row.. if not end cell shoudl be (-1,-1)
#         ("VALIGN", (0,0), (-1, -1), "MIDDLE"),
#         ("VALIGN", (0,0), (0, 0), "BOTTOM"),
#         ('BOTTOMPADDING', (0,0), (0, 0), 10), # adding padding after name before job title
#         ("FONTNAME", (0,0), (-1, -1), "oswald_semibold"),  # header font
#         ("FONTSIZE", (0,0), (-1, -1), 10),  # header font size
#         ("FONTSIZE", (0,0), (-1, 0), 20),  # header font size
#         ("TEXTCOLOR", (0, 0), (-1, 0), color_deep_dark),
#         # ===== address section in title ========
#         ("FONTNAME", (1,0), (-1, -1), "oswald_extralight"),
#         ("FONTSIZE", (1,0), (-1, -1), 10),
#         ("VALIGN", (1,0), (-1, -1), 'TOP'),
#         ("ALIGN", (1,0), (-1, -1), "RIGHT"),
#     ])
# )


# Elements.append(title_table)
# Elements += ribbon(height=2, width=PAGE_FRAME_WIDTH, color=color_deep_dark, space_before=0)
# Elements += ribbon(height=15, width=PAGE_FRAME_WIDTH, color=color_white, space_before=0)

# # ============================================================================

# # ===========================  Summary =======================================
# summ = data['summary']
# head = summ['heading']
# expl = summ['text']
# Elements += produce_heading(head)
# style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=10,)
# Elements.append(Paragraph(expl, style))
# Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # before links

# from reportlab.platypus import ListFlowable, ListItem
# style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=10,)
# links = [ListItem(Paragraph(link, style), value="diamond") for link in summ['links']]
# list_links = ListFlowable(links, bulletType='bullet', start='diamond')
# Elements.append(list_links)
# Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # after links

# # ============================================================================

# # ===========================  Skills =======================================
# skills = data['keyskills']
# head = skills['heading']
# skills_list = skills['skills']
# Elements += produce_heading(head)
# # Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # before links

# from reportlab.platypus import ListFlowable, ListItem
# style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=10,)
# skills_items = [ListItem(Paragraph(skill, style), value="circle") for skill in skills_list]
# list_skills = ListFlowable(skills_items, bulletType='bullet', start='circle')
# Elements.append(list_skills)
# Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # after links

# # ============================================================================

# # ===========================  Proffesial summary =======================================
# prof = data['professional_summary']
# head = prof['heading']
# experiences_list = prof['experiences']
# Elements += produce_heading(head)
# # Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # before links

# from reportlab.platypus import ListFlowable, ListItem
# style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=10,)
# experience_items = [ListItem(Paragraph(experience, style), value="square") for experience in experiences_list]
# list_experiences = ListFlowable(experience_items, bulletType='bullet', start='square')
# Elements.append(list_experiences)
# Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # after links

# # ============================================================================

# # ===========================  Rrojects =======================================
# proj = data['projects']
# head = proj['heading']
# projects_list = proj['projects']
# Elements += produce_heading(head)
# # Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # before links

# from reportlab.platypus import ListFlowable, ListItem
# style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=10,)
# project_items = [ListItem(Paragraph(project, style), value="circle") for project in projects_list]
# list_projects = ListFlowable(project_items, bulletType='bullet', start='disk')
# Elements.append(list_projects)
# Elements += ribbon(height=8, width=PAGE_FRAME_WIDTH, color=color_white) # after links

# # ============================================================================
# # switching to next page
# from reportlab.platypus import PageBreak, FrameBreak
# Elements.append(FrameBreak())
# Elements += ribbon(height=10, width=PAGE_FRAME_WIDTH, color=color_white)

# # ===========================  Education table ===============================

# edu = data['education']
# head = edu['heading']
# Elements += produce_heading(head)

# tab=edu['table']
# education_table_data = [tab['columns']] + tab['data']

# no_cols = len(tab['columns'])
# col_widths = [PAGE_FRAME_WIDTH / no_cols for i in range(1,no_cols+1)]  ## now manually changing down >
# col_widths = [130.8188976377953, 190.8188976377953, 60.8188976377953, 140.8188976377953]
# # print(col_widths)
# education_table = RLTable(
#     education_table_data,
#     colWidths=col_widths,
# )  
# education_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), color_deep_dark),
#                             ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
#                             ("ALIGN", (0,0), (-1, 0), "CENTER"), # align only the header row.. if not end cell shoudl be (-1,-1)
#                             ("VALIGN", (0,0), (-1, -1), "MIDDLE"),
#                             ("FONTNAME", (0,0), (-1, 0), "yanone"),  # header font
#                             ("FONTSIZE", (0,0), (-1, 0), 11),  # header font size
#                             ("FONTNAME", (0, 1), (-1, -1), "oswald_extralight"),  # other row fonts
#                             ("FONTSIZE", (0, 1), (-1, -1), 10),  # font size of other rows
#                             ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
#                             ("ALIGN", (1, 0), (-1, -1), "CENTER"),  # all columns except name center align
#                             ]))

# # further customizing
# internal_border_color = colors.white
# start = 1

# # adding horizontal lines as borders and alighning left Institution column of each row
# for i in range(start, len(education_table_data)): # 1 because don't want header row to have horizontal line
#     table_style = TableStyle([
#         # ("LINEABOVE", (0,i), (-1, i), 0.1, internal_border_color),
#         ("ALIGN", (1, i), (1, i), "LEFT") ,  # adding left align to institution column
#     ])
#     education_table.setStyle(table_style)

# Elements.append(education_table)
# # ===========================================================================

# # ===================== other certifications ================================
# oth_cert = data['other_certifications']
# head = oth_cert['heading']
# Elements += produce_heading(head)
# from reportlab.platypus import ListFlowable, ListItem
# style = ParagraphStyle(name='Normal', fontName='oswald_light', fontSize=10,)

# certificates = [ListItem(Paragraph(cert, style), value="square") for cert in oth_cert['certificates']]
# list_cert = ListFlowable(certificates, bulletType='bullet', start='square')

# Elements.append(list_cert)

# # ===========================================================================

# # ============================= END SECTION =================================
# from .new_flowable import HorizontalRule
# Elements.append(HorizontalRule())
# Elements.append(Spacer(width=PAGE_FRAME_WIDTH, height=4, isGlue=True))

# Elements += ribbon(height=2, width=PAGE_FRAME_WIDTH, color=color_general, space_before=0)

# Elements += ribbon(color=color_light)

# ===========================================================================



