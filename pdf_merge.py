# pdf_merging.py

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
	if (len(sys.argv) <= 2):
		print ('Pas assez d\'arguments fournis')
		print ('Veuillez fournir le nom des fichiers pdf a fusionner et terminer par le nom du PDF en sortie. Exemple :')
		print ('py pdf_merge.py myfirstpdf.pdf secondpdf.pdf merged.pdf')
	else:
		print ('Fusion')
		nb_args = len(sys.argv)
		fichiers_a_fusionner = []
		for arg in range(1,nb_args-1):
			fichiers_a_fusionner.append(sys.argv[arg])
		merge_pdfs(fichiers_a_fusionner, sys.argv[nb_args-1])
		print ('Les fichiers ', str(fichiers_a_fusionner), 'ont étés fusionnés dans ', str(sys.argv[nb_args-1]))
