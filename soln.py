
import pdf2image

import json

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        raw_text = ocr_core(img)
    data = {
        "document_Content" : raw_text
        }
    result = json.dumps(data, indent = 4)
    print(result)



if __name__ == "__main__":
    print_pages('/home/syed/Downloads/Sodium_Chloride_SDS.pdf')
    print_pages('/home/syed/Downloads/Acetic_Acid_1N_3-10percent_SDS.pdf')
