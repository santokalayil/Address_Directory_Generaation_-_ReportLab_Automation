

from directory import master
from directory import doc
page_object = master.double_row_frame(doc, ["box_top", "box_bottom"])
page_frame = page_object.generate()

from reportlab.platypus import PageTemplate
from directory import section_ids
page_template = PageTemplate(
        id="Families", 
        frames=page_frame,
        onPage=master.default_master,
    )


from .family_box import generate_box_elements
from directory.database.get import basic_query
from directory.settings import db_url




def generate():
    Elements = []
    sql = basic_query(db_url).sql_dataframe
    order_of_families = sql(
        '''select * from members where rltshp = "Self" order by member_name'''
        ).famid.to_dict().values()

    for order_id, fam_id in enumerate(order_of_families, start=1):
        Elements += generate_box_elements(fam_id, order_id)
    return Elements
