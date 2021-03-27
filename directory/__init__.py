from . import master
from .settings import *

from reportlab.platypus import (Paragraph, Spacer, CondPageBreak, FrameBreak, PageBegin,
                                NextPageTemplate, PageBreak, PageTemplate)
from . import fonts

fonts.register()

# initializing document
doc = master.document()

# setting frame
# resume_frame = master.single_frame(doc, id='normal')
families_info_page_object = master.double_row_frame(doc, ["box_top", "box_bottom"])
families_info_page_frame = families_info_page_object.generate()
print("BOTTOM FRAME HEIGHT AND WIDTH:", families_info_page_object.bottom_frame.height, families_info_page_object.bottom_frame.width)
print("TOP FRAME HEIGHT AND WIDTH:", families_info_page_object.top_frame.height, families_info_page_object.top_frame.width)
from . import section_ids

# setting master
doc.addPageTemplates([PageTemplate(id=section_ids.dual_row_family_id, frames=families_info_page_frame, onPage=master.default_master),
                    #   PageTemplate(id=message_section_id, frames=single_frame, onPage=message_master),
                      ])

# Adding elements
from .contents import Elements
# Elements.append(Spacer(1, PAGE_HEIGHT * 0.3))



Elements.append(PageBreak())  # skipping the box frame

# start the construction of the pdf
doc.build(Elements)
