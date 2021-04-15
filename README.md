# fotoincolla
Un fotoincolla è l'inverso di una fotocopia, legge un documento PDF fotocopiato, ne estrae le immagini in jpeg, e converte il testo rilevato come file di testo.


Requisiti:
```
pip install opencv-python pytesseract Pillow pymupdf
```
Uso:
```
python3 FI.py
```
Demo:
```
Files disponibili:
['./input/Ordinanza-41-14042021.pdf']

Inserire numero ordinanza: (es.41-1404...)
41-14042021
Conversione in corso..
```
Demo Output:
```
Ordinanza-41-14042021.txt
```
# Accuratezza
Qualora si stia cercando di leggere un'ordinanza scritta in Italiano, sarebbe meglio utilizzare un trained model per questo linguaggio.
Per farlo, scaricare il file [ita.traineddata](https://github.com/tesseract-ocr/tessdata/blob/master/ita.traineddata), spostarlo in una cartella, ad esempio: "/home/user/lib/tessdata/languages", e associare la cartella tessdata alla variabile di sistema TESSDATA_PREFIX
```
export TESSDATA_PREFIX=/home/user/lib/tessdata
```
A quel punto è possibile utilizzare l'argomento lang nella funzione di pytesseract, ad esempio:
```
text = pytesseract.image_to_string(img, lang="ita")
```
