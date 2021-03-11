# pdf_extract.py

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		print ('Pas assez d\'arguments fournis')
		print ('Veuillez fournir le nom du fichier pdf a diviser. Exemple :')
		print ('py pdf_extract.py pdftosplit.pdf')
	else:
		fichier_a_diviser = sys.argv[1]
		print ('Séparation des pages de ', fichier_a_diviser)
		split(fichier_a_diviser, 'output')
		print ('Les fichiers ont étés générés et s\'appellent output1.pdf, output2.pdf, ...')