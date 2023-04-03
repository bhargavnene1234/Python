import PyPDF2

input_pdf=PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(input_pdf.getNumPages()):
    page=input_pdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_pdf.pdf','wb') as file:
        output.write(file)