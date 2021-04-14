import io
import os
import cv2
import glob
import fitz
import pytesseract
from PIL import Image

'''
FotoIncolla prende un .PDF come input,
ne estrae le immagini come .jpeg,
e ne interpreta il testo in formato txt.
'''

if not os.path.isdir("input"):
    os.makedirs("input")
elif not os.path.isdir("scans"):
    os.makedirs("scans")
elif not os.path.isdir("output"):
    os.makedirs("output")
else:
    pass

def fi(file,output):
    pdf_file = fitz.open(file)
    output = open(output, 'w')

    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.getImageList()

        for image_index, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(open(f"./scans/{page_index}.{image_ext}", "wb"))
            img = cv2.imread("./scans/"+str((page_index))+".jpeg")
            text = pytesseract.image_to_string(img)
            output.write("%s\n" % text)
            print("pagina "+str(page_index+1)+"..")
            
    print("\nFinito")

print("Files disponibili:\n"+str(glob.glob("./input/*.pdf")))
file = input("\nInserire numero ordinanza: (es.41-1404...)\n")
print("Conversione in corso..\n")
fi('./input/Ordinanza-'+file+'.pdf','./output/Ordinanza-'+file+'.txt')
