section_id = 'Birthdays'

from directory import master
from directory import doc
page_object = master.single_frame(doc, section_id)
# (doc, ["box_top", "box_bottom"])
# page_frame = page_object.generate()
page_frame = page_object

from reportlab.platypus import PageTemplate
# from directory import section_ids
page_template = PageTemplate(
        id=section_id, 
        frames=page_frame,
        onPage=master.default_master,
    )

from .elements import title_section



def generate():
    Elements = []
    from reportlab.platypus import NextPageTemplate
    Elements.append(NextPageTemplate(section_id))
    from reportlab.platypus import FrameBreak
    Elements.append(FrameBreak())
    Elements.append(title_section('Birthdays'))

    from .table import generate as table_generate
    Elements += table_generate()

    return Elements
