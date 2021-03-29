from . import section_ids
from .settings import PAGE_FRAME_WIDTH, PAGE_FRAME_HEIGHT

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate, FrameBreak




Elements = []
Elements.append(NextPageTemplate(section_ids.dual_row_family_id))  # marking section id to identify master page and style

from .pages.family_pages.family_box import (
    family_title_section,
    photo_and_address_section,
    members_table_section,
)

Elements += [
    family_title_section(fam_id=12, family_head="Thomas K J"),
    photo_and_address_section(),
    members_table_section()
]