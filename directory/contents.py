from . import section_ids
from .settings import PAGE_FRAME_WIDTH, PAGE_FRAME_HEIGHT
from .settings import db_url

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate, FrameBreak




Elements = []
Elements.append(NextPageTemplate(section_ids.dual_row_family_id))  # marking section id to identify master page and style



# going to each family data and constructing elements
from .pages.family_pages.family_box import generate_box_elements
from .database.get import basic_query
sql = basic_query(db_url).sql_dataframe
order_of_families = sql(
    '''select * from members where rltshp = "Self" order by member_name'''
    ).famid.to_dict().values()

for order_id, fam_id in enumerate(order_of_families, start=1):
    Elements += generate_box_elements(fam_id, order_id)