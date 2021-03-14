Outil pour diviser un fichier PDF multi-page en plusieurs PDFs d'une page ou pour fusionner plusieurs fichiers PDF en un.

*Sources récupérées à partir de cet article de blog : https://realpython.com/pdf-python/ (auteur : Mike Driscoll)*

# PDF Merge

Fusionne une liste de fichiers PDF en un seul fichier. Utilisation :
```py pdf_merge.py myfirstpdf.pdf [secondpdf.pdf ...] merged.pdf```
Exemple :
```py pdf_merge.py myfirstpdf.pdf secondpdf.pdf merged.pdf```

# PDF Extract

Extrait chacune des pages d'un fichier PDF en un fichier distinct. Les fichiers seront de la forme output1.pdf, output2.pdf, etc. Utilisation :
```py pdf_extract.py pdftosplit.pdf```
On peut également spécifier le format de sortie du fichier (par défaut output\*.pdf). Les étoiles seront remplacées par le numéro de la page extraite (si plusieurs étoiles sont à la suite, ceci indique la longueur minimale du nombre souhaité, et des zéros non significatifs seront ajoutés).

Exemple :
```'py pdf_extract.py pdftosplit.pdf pdf_extrait_numero**.pdf'```
Afichera les fichiers pdf_extrait_numero01.pdf, pdf_extrait_numero02.pdf, etc.