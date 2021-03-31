from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, Spacer,
                                NextPageTemplate, PageBreak, PageTemplate)

# from pdf_generation.page_settings import *
from .settings import *


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


def default_master(canvas, doc):  # master_1
    canvas.saveState()
    # canvas.setFont('Times-Roman', 9)
    # canvas.drawString(0.5 * inch, 0.3 * inch, f"Messages / {doc.page} | {page_info}")
    canvas.restoreState()



# -------------------- FRAMES -------------------------

def single_frame(doc, id):
    # normal frame as for SimpleFlowDocument
    frame = Frame(x1=doc.leftMargin, y1=doc.bottomMargin, width=doc.width, height=doc.height, id=id)
    return frame


# def double_column_frame_template(doc, ids):
#     frame1 = Frame(x1=doc.leftMargin, y1=doc.bottomMargin, width=doc.width / 2 - 6, height=doc.height, id=ids[0])
#     frame2 = Frame(x1=doc.leftMargin + doc.width / 2 + 6, y1=doc.bottomMargin, width=doc.width / 2 - 6,
#                    height=doc.height, id=ids[1])
#     return [frame1, frame2]



# top_frame.height

# def double_row_frame(doc, ids):
#     return [top_frame, bottom_frame] # bottom_frame

from .settings import frame_boundary as boundary

class double_row_frame():
    def __init__(self, doc, ids):
        self.doc = doc
        self.ids = ids
        self.top_frame = self.top_frame_generate
        self.bottom_frame = self.bottom_frame_generate

    
    @property
    def top_frame_generate(self):
        doc = self.doc
        ids = self.ids
        frame = Frame(x1=doc.leftMargin, y1=doc.height/2,  #  + (PAGE_FRAME_HEIGHT/2)
                        width=PAGE_FRAME_WIDTH, height=(PAGE_FRAME_HEIGHT/2),
                        id=ids[0], showBoundary=boundary)

        return frame

    @property
    def bottom_frame_generate(self):
        doc = self.doc
        ids = self.ids
        frame = Frame(x1=doc.leftMargin, y1=doc.bottomMargin,  # if y1 increase bottom frame goes up
                    width=PAGE_FRAME_WIDTH, height=PAGE_FRAME_HEIGHT/2,   # width=doc.width
                    id=ids[1], showBoundary=boundary)
        return frame

    def generate(self):
        return [self.top_frame, self.bottom_frame]

