from . import master
from .settings import *

from reportlab.platypus import (Paragraph, Spacer, CondPageBreak, FrameBreak, PageBegin,
                                NextPageTemplate, PageBreak, PageTemplate)
from . import fonts

fonts.register()

# initializing document
doc = master.document()

# setting frame

# families_info_page_object = master.double_row_frame(doc, ["box_top", "box_bottom"])
# families_info_page_frame = families_info_page_object.generate()
from .pages.family_pages import page_template as family_page_template

birthday_frame = master.single_frame(doc, id='normal')

from . import section_ids

# setting master
doc.addPageTemplates([
  family_page_template,
  PageTemplate(id=section_ids.birthday_pages_id, frames=birthday_frame, onPage=master.default_master),
  ])

# Adding elements
from .contents import Elements
# Elements.append(Spacer(1, PAGE_HEIGHT * 0.3))



Elements.append(PageBreak())  # skipping the box frame

# start the construction of the pdf
doc.build(Elements)
