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
