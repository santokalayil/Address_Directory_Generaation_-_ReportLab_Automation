from reportlab.platypus.flowables import Flowable
from reportlab.lib import colors

class HorizontalRule(Flowable):
    def __init__(self, width=1, strokecolor=colors.Color(0.2, 0.3, 0.4)):
        self.width = width
        self.strokecolor = strokecolor
    def wrap(self, availWidth, availHeight):
        self.availWidth = availWidth
        return (availWidth, self.width + 2)
    def draw(self):
        canvas = self.canv
        canvas.setLineWidth(self.width)
        canvas.setStrokeColor(self.strokecolor)
        p = canvas.beginPath()
        p.moveTo(0, 1)
        p.lineTo(self.availWidth, 1)
        p.close()
        canvas.drawPath(p)