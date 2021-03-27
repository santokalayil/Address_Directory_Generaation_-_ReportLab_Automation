from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase import pdfmetrics


# register a new font
def register_font():
    pdfmetrics.registerFont(TTFont('merriweather','fonts/merriweather/Merriweather-Black.ttf'))
    pdfmetrics.registerFont(TTFont('yanone','fonts/yanone/YanoneKaffeesatz-Light.ttf'))
    pdfmetrics.registerFont(TTFont('oswald_regular', 'fonts/oswald/Oswald-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('oswald_semibold', 'fonts/oswald/Oswald-SemiBold.ttf'))
    pdfmetrics.registerFont(TTFont('oswald_medium', 'fonts/oswald/Oswald-Medium.ttf'))
    pdfmetrics.registerFont(TTFont('oswald_light', 'fonts/oswald/Oswald-Light.ttf'))
    pdfmetrics.registerFont(TTFont('oswald_extralight', 'fonts/oswald/Oswald-ExtraLight.ttf'))

