from openpyxl import Workbook, workbook
from openpyxl.drawing.image import Image


wb = Workbook()
ws = wb.active

img = Image('a.png')

ws.add_image(img,'A1')

wb.save('d.xlsx')
wb.close()