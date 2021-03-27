from reportlab.lib import colors
from pdf_generation.page_settings import *
from reportlab.platypus import Image, Table


class family_image:
    def __init__(self, img_path):
        self.img_path = img_path

    def generate(self):
        # pct = 0.9
        img_width = (320 * 0.35)  # * pct
        img_height = (249 * 0.35)  # * pct
        img = Image(filename=self.img_path, width=img_width, height=img_height, )
        img_table = Table(
            data=[[img]],
            colWidths=img_width,
            rowHeights=img_height,
            style=[
                # The two (0, 0) in each attribute represent the range
                # # of table cells that the style applies to. Since there's only one cell at (0, 0),
                # it's used for both start and end of the range
                ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                # ('BOX', (0, 0), (0, 0), 2, colors.HexColor('#eeeeee')),
                # The fourth argument to this style attribute is the border width
                ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),

            ]
        )
        return img_table


