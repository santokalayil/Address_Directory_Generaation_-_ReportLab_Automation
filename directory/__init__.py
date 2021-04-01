from . import master
from .settings import *

from reportlab.platypus import (Paragraph, Spacer, CondPageBreak, FrameBreak, PageBegin,
                                NextPageTemplate, PageBreak, PageTemplate)
from . import fonts

fonts.register()

# initializing document
doc = master.document()

from .pages.family_pages import page_template as family_page_template
from .pages.birthdays import page_template as birthday_page_template

# setting master page templates
doc.addPageTemplates([
  family_page_template,
  birthday_page_template,
  ])

# Adding elements
from .contents import Elements
# Elements.append(Spacer(1, PAGE_HEIGHT * 0.3))



Elements.append(PageBreak())  # skipping the box frame

# start the construction of the pdf
doc.build(Elements)
