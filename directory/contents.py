from . import section_ids
from .settings import PAGE_FRAME_WIDTH, PAGE_FRAME_HEIGHT
from .settings import db_url

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate, FrameBreak, PageBreak, PageBreakIfNotEmpty




Elements = []
Elements.append(NextPageTemplate(section_ids.dual_row_family_id))  # marking section id to identify master page and style


from .pages.family_pages import generate as generate_family_pages
Elements += generate_family_pages()

Elements.append(PageBreakIfNotEmpty())
Elements.append(NextPageTemplate(section_ids.birthday_pages_id))