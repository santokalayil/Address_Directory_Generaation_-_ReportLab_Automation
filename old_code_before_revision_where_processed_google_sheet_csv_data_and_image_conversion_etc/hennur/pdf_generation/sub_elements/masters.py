from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, Spacer,
                                NextPageTemplate, PageBreak, PageTemplate)

from pdf_generation.page_settings import *


def document():
    doc = BaseDocTemplate(export_name_url,
                          showBoundary=0,  # if one frame will be shown with boundary line thickness
                          pagesize=page_size,
                          topMargin=TOP_MARGIN,
                          bottomMargin=BOTTOM_MARGIN,
                          leftMargin=LEFT_MARGIN,
                          rightMargin=RIGHT_MARGIN
                          )
    return doc


def master_1(canvas, doc):
    canvas.saveState()
    canvas.restoreState()


def master_2(canvas, doc):
    canvas.saveState()
    # canvas.setFont('Times-Roman', 9)
    # canvas.drawString(0.5 * inch, 0.3 * inch, f"Messages / {doc.page} | {page_info}")
    canvas.restoreState()


def master_3(canvas, doc):
    canvas.saveState()
    # canvas.setFont('Times-Roman', 9)
    # canvas.drawString(0.5 * inch, 0.3 * inch, f"History {doc.page} {page_info}")
    canvas.restoreState()


def master_4(canvas, doc):
    canvas.saveState()
    # canvas.setFont('Times-Roman', 9)
    # canvas.drawString(0.5 * inch, 0.3 * inch, f"Addresses {doc.page} {page_info}")
    canvas.restoreState()


# -------------------- FRAMES -------------------------

def single_column_frame_template(doc, id):
    # normal frame as for SimpleFlowDocument
    frame = Frame(x1=doc.leftMargin, y1=doc.bottomMargin, width=doc.width, height=doc.height, id=id)
    return frame


def double_column_frame_template(doc, ids):
    frame1 = Frame(x1=doc.leftMargin, y1=doc.bottomMargin, width=doc.width / 2 - 6, height=doc.height, id=ids[0])
    frame2 = Frame(x1=doc.leftMargin + doc.width / 2 + 6, y1=doc.bottomMargin, width=doc.width / 2 - 6,
                   height=doc.height, id=ids[1])
    return [frame1, frame2]


def double_row_frame_template(doc, ids):
    # row_space = 0
    top_frame = Frame(x1=doc.leftMargin, y1=doc.bottomMargin + (doc.height/2),
                      width=PAGE_FRAME_WIDTH, height=doc.height/2,
                      id=ids[0])
    bottom_frame = Frame(x1=doc.leftMargin, y1=doc.bottomMargin + 10,  # if y1 increase bottom frame goes up
                         width=PAGE_FRAME_WIDTH, height=doc.height/2 + 10,   # width=doc.width
                         id=ids[1])
    return [top_frame, bottom_frame]

