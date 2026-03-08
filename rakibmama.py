import pytesseract
from PIL import Image

# এই লাইনটি ঠিক এইভাবেই তোমার কোডে যোগ করো
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


try:
    # তোমার ছবি ওপেন করা
    img = Image.open('img.png')
    # 'lang="ben+eng"' লিখে দাও যাতে সে বাংলা ও ইংরেজি দুটোই বুঝতে পারে
    text = pytesseract.image_to_string(img, lang='ben+eng')
    # ছবি থেকে লেখা বের করা
    text = pytesseract.image_to_string(img)

    # ফলাফল প্রিন্ট করা
    print("ছবিতে লেখা আছে:")
    print(text)
except FileNotFoundError:
    print("ভুল: 'images.png' ফাইলটি খুঁজে পাওয়া যায়নি। নিশ্চিত করো ছবিটি কোডের পাশেই আছে।")
except Exception as e:
    print(f"অন্য একটি সমস্যা হয়েছে: {e}")
