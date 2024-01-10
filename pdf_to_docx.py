# pip install pdf2docx

from pdf2docx import Converter
pdf_file = '2023j.pdf'
docx_file = '2023j.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()