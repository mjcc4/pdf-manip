# pdf_extract.py

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def transformer_expression_fichier(expr_nom_fichiers_extraits):
	expr_transformee = ""
	expr_a_traiter = expr_nom_fichiers_extraits
	nbstar=1
	while expr_a_traiter != "":
		x,y,expr_a_traiter = expr_a_traiter.partition("*")
		expr_transformee += x
		if expr_a_traiter != "" and expr_a_traiter[0] != '*':
			expr_transformee += '{n:0'+'{0}'.format(nbstar)+'d}'
			nbstar=1
		elif expr_a_traiter != "":
			nbstar+=1
		elif  y != "":
			expr_transformee += '{n:0'+'{0}'.format(nbstar)+'d}'
	return expr_transformee

def split(path, expr_nom_fichiers_extraits):
	expr_transformee = transformer_expression_fichier(expr_nom_fichiers_extraits)
	pdf = PdfFileReader(path)
	for page in range(pdf.getNumPages()):
		pdf_writer = PdfFileWriter()
		pdf_writer.addPage(pdf.getPage(page))

		output = expr_transformee.format(n=page)
		with open(output, 'wb') as output_pdf:
			pdf_writer.write(output_pdf)

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		print ('Pas assez d\'arguments fournis')
		print ('Veuillez fournir le nom du fichier pdf a diviser. Exemple :')
		print ('py pdf_extract.py pdftosplit.pdf')
		print ('Vous pouvez aussi spécifier le format de sortie du fichier (par défaut output*.pdf). Exemple :')
		print ('py pdf_extract.py pdftosplit.pdf pdf_extrait_numero**.pdf')
		print ('Le nombre d\'étoiles indique le nombre de zéros non significatif souhaité')
	else:
		fichier_a_diviser = sys.argv[1]
		if (len(sys.argv) == 3):
			expr_nom_fichiers_extraits = sys.argv[2]
		else:
			expr_nom_fichiers_extraits = 'output*.pdf'
		print ('Séparation des pages de ', fichier_a_diviser)
		split(fichier_a_diviser, expr_nom_fichiers_extraits)
		print ('Les fichiers ont étés générés sous la forme',expr_nom_fichiers_extraits)