import pytesseract
from PIL import Image
import nltk
from nltk.corpus import stopwords
from collections import Counter

##image_path = '/content/c.png'
##img = Image.open('/content/c.png')


extracted_text = pytesseract.image_to_string(img)
print("Extracted Text:\n", extracted_text)


nltk.download('stopwords')


def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words =extracted_text.split()
    keywords = [word for word in words if word.lower() not in stop_words]
    keyword_freq = Counter(keywords)
    return keyword_freq.most_common(10)

keywords = extract_keywords(extracted_text)
print("Top Keywords:\n", keywords)
img.show()