section_id = 'Anniversaries'

from directory import master
from directory import doc
page_object = master.single_frame(doc, section_id)

page_frame = page_object

from reportlab.platypus import PageTemplate

# from directory import section_ids
# import this page_template in init.py of main directory and a
# and add it to doc.addPageTemplate section in the list
page_template = PageTemplate(
        id=section_id, 
        frames=page_frame,
        onPage=master.default_master,
    )


from .elements import title_section

def generate():
    Elements = []
    from reportlab.platypus import NextPageTemplate
    from reportlab.platypus import FrameBreak, PageBreak
    Elements.append(NextPageTemplate(section_id))
    Elements.append(FrameBreak())
    
    Elements.append(title_section('Anniversaries'))

    # Elements.append(FrameBreak())

    from .table import generate as table_generate
    Elements += table_generate()
    return Elements