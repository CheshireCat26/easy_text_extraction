from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image_path = "alt text.jpg"

img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
print(text)
