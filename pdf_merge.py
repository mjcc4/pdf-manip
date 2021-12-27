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


def print_help():
    print('pdf_merge fusionne la liste de fichiers PDF fournie en un fichier PDF unique.')
    print('Usage : py pdf_merge.py pdf1.pdf pdf2.pdf ... [-o mergedpdf.pdf]')
    print('   OU : py pdf_merge.py -s pdf*.pdf 1 10 [-o mergedpdf.pdf]')
    print('Options')
    print('-o/-output : Nom du fichier de sortie souhaité. Si non spécifié, ce sera merged.pdf')
    print('-s/-sequence : Définit une séquence de fichiers.', 
    'La commande mypdfseq**.pdf 1 100 va générer la liste mypdfseq01.pdf jusqu\'à mypdfseq100.pdf')


def lire_sysargs():
    nb_args = len(sys.argv)
    if (nb_args <= 1):
        print('Pas assez d\'arguments fournis')
        print_help()
        return {"demarrerTraitement": False}
    if (sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h"):
        print_help()
        return {"demarrerTraitement": False}
    fichiers_a_fusionner = []
    nom_fichier_fusionne = "merged.pdf"
    # Lecture des arguments
    numArgLu = 1
    optionsLues = {"liste": False, "output": False, "sequence": False}
    while (numArgLu < nb_args):
        if (sys.argv[numArgLu] == "-output" or sys.argv[numArgLu] == "-o"):
            if (optionsLues["output"]):
                print("L'option -output/-o ne doit être utilisée qu'1 fois")
                return {"demarrerTraitement": False}
            numArgLu += 1
            if (numArgLu >= nb_args):
                print("Veuillez spécifier un nom de fichier après -output")
                return {"demarrerTraitement": False}
            nom_fichier_fusionne = sys.argv[numArgLu]
            optionsLues["output"] = True
            print("fichier de sortie custom qui vaut : ", nom_fichier_fusionne)
        elif (sys.argv[numArgLu] == "-sequence" or sys.argv[numArgLu] == "-s"):
            if (optionsLues["sequence"]):
                print("L'option -sequence/-s ne doit être utilisée qu'1 fois")
                return {"demarrerTraitement": False}
            numArgLu += 1
            if (numArgLu >= nb_args):
                print("Veuillez spécifier un nom de fichier après -sequence")
                return {"demarrerTraitement": False}
            print("todo")
            optionsLues["sequence"] = True
        else:
            if (optionsLues["liste"]):
                print("La liste des fichiers ne doit être spécifiée qu'1 fois")
                return {"demarrerTraitement": False}
            numArgListeLu = numArgLu
            while (numArgListeLu < nb_args
                   and sys.argv[numArgListeLu] != "-output" and sys.argv[numArgListeLu] != "-o"
                   and sys.argv[numArgListeLu] != "-sequence" and sys.argv[numArgListeLu] != "-s"):
                fichiers_a_fusionner.append(sys.argv[numArgListeLu])
                numArgListeLu += 1
            numArgLu = numArgListeLu-1
            optionsLues["liste"] = True
        numArgLu += 1
    if (len(fichiers_a_fusionner) == 0):
        print("Veuillez spécifier au moins 1 fichier à fusionner")
        return {"demarrerTraitement": False}
    return {"demarrerTraitement": True,
            "nom_fichier_fusionne": nom_fichier_fusionne,
            "fichiers_a_fusionner": fichiers_a_fusionner}


if __name__ == '__main__':
    args = lire_sysargs()
    if (args["demarrerTraitement"]):
        print('Fusion...')
        fichiers_a_fusionner = args["fichiers_a_fusionner"]
        nom_fichier_fusionne = args["nom_fichier_fusionne"]
        merge_pdfs(fichiers_a_fusionner, nom_fichier_fusionne)
        print('Les fichiers ', str(fichiers_a_fusionner),
              'ont étés fusionnés dans ', str(nom_fichier_fusionne))
