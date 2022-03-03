import pytesseract
from PIL import Image
import os



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    PATH = input("Please enter the path to your screenshot WITH its extension: ")
    if os.path.isfile('./' + PATH) == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        img = Image.open(PATH)
        
        result = pytesseract.image_to_string(img, lang='deu')
        print("".join([s for s in result.strip().splitlines(True) if s.strip()]))
    else:
        print("Please enter a valid path.")
    
if __name__== "__main__":
    main()