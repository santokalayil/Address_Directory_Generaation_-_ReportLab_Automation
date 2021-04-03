from . import section_ids
from .settings import PAGE_FRAME_WIDTH, PAGE_FRAME_HEIGHT
from .settings import db_url

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, NextPageTemplate, FrameBreak, PageBreak, PageBreakIfNotEmpty

Elements = []

from .pages.family_pages import generate as generate_family_pages
Elements += generate_family_pages()

from .pages.birthdays import generate as generate_birthday_pages
Elements += generate_birthday_pages()

from .pages.anniversaries import generate as generate_anniversary_pages
Elements += generate_anniversary_pages()