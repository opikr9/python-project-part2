from pdf2docx import Converter

old_pdf = "Aljabar Linear.pdf"
new_doc = "aljabarLinear.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()

from docx2pdf import convert

convert("aljabarLinear.docx","Aljabarl.pdf")