from .pages.family_pages.family_box import generate_box_elements
from .database.get import basic_query

def generate():
    Elements = []
    sql = basic_query(db_url).sql_dataframe
    order_of_families = sql(
        '''select * from members where rltshp = "Self" order by member_name'''
        ).famid.to_dict().values()

    for order_id, fam_id in enumerate(order_of_families, start=1):
    Elements += generate_box_elements(fam_id, order_id)
    return Elements
