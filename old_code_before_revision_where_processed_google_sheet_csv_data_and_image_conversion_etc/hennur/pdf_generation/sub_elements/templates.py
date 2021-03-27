import os

from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
styles = getSampleStyleSheet()

common_paragraph_standard = ParagraphStyle(name='normal',
                                             alignment=TA_JUSTIFY,
                                             fontSize=9,
                                             textColor=colors.black,
                                             firstLineIndent=30,
                                             spaceShrinkage=0.05,
                                             leading=12,
                                             splitLongWords=1,
                                             uriWasteReduce=0.3,   # ?
                                             wordWrap=None
                                           )


def vicar_message():
    after_heading_space = Spacer(1, 0.3*inch)
    paragraph_space = Spacer(1, 0.1*inch)
    paragraphs = [after_heading_space, ]
    message_heading_style = ParagraphStyle(name='normal',
                                           alignment=1,
                                           fontSize=18,
                                           textColor=colors.deepskyblue
                                           )
    heading_of_message = Paragraph("From Vicar's Desk", message_heading_style)
    paragraphs.append(heading_of_message)
    paragraphs.append(after_heading_space)
    assets_folder = os.path.join('pdf_generation', 'assets')
    vicar_xt_file = os.path.join(assets_folder, 'message_vicar.txt')
    with open(vicar_xt_file, 'r') as txt_file_message_of_vicar:
        message_of_vicar = txt_file_message_of_vicar.readlines()
    message_paragraph_style = common_paragraph_standard
    message_paragraph_style.firstLineIndent = 24  # rewriting the firstLineIndent
    for line_of_message in message_of_vicar:
        p = Paragraph(line_of_message, message_paragraph_style)
        paragraphs.append(p)
        paragraphs.append(paragraph_space)
    return paragraphs


def history_of_parish():
    after_heading_space = Spacer(1, 0.3*inch)
    paragraph_space = Spacer(1, 0.025*inch)
    paragraphs = [after_heading_space, ]
    message_heading_style = ParagraphStyle(name='normal',
                                           alignment=1,
                                           fontSize=18,
                                           textColor=colors.deepskyblue
                                           )
    heading_of_message = Paragraph("History of the Parish", message_heading_style)
    paragraphs.append(heading_of_message)
    paragraphs.append(after_heading_space)
    assets_folder = os.path.join('pdf_generation', 'assets')
    vicar_xt_file = os.path.join(assets_folder, 'history.txt')
    with open(vicar_xt_file, 'r') as txt_file_message_of_vicar:
        message_of_vicar = txt_file_message_of_vicar.readlines()
    message_paragraph_style = common_paragraph_standard
    message_paragraph_style.firstLineIndent = 24  # rewriting the firstLineIndent
    for line_of_message in message_of_vicar:
        p = Paragraph(line_of_message, message_paragraph_style)
        paragraphs.append(p)
        paragraphs.append(paragraph_space)
    return paragraphs
