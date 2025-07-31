# 🔑 Key Generator & Reader  

A simple Python tool for generating and reading product keys from **text** or **images** using OCR (Optical Character Recognition) via **Tesseract**.  

---  
## 📦 Requirements  

### Tesseract OCR  
Download and install from this page:  
https://github.com/UB-Mannheim/tesseract/wiki  

### Python Libraries  
Install required packages with:  
pip install pytesseract Pillow  

📁 Project Structure  
File/Folder Description  
- generator.py - Generates random product keys and appends them to key_list.  
- reader.py - Reads and extracts keys from text (used_keys_trash) or images.  
- key_list - Stores all generated product keys.  
- used_keys - Stores all extracted keys (sorted & deduplicated).  
- used_keys_trash - Temporary file with raw text from which keys are read.  
- image/ - Folder for placing images containing keys to be recognized.  

📌 Usage  
▶️ Generate Keys  
Run the generator script:  
python generator.py  

🧾 Read Keys from Text or Images  
Run the reader script:  

python reader.py  
You’ll be prompted to choose an option:  

1 — Extract keys from text in used_keys_trash  

2 — Extract keys from images in the image/ folder  
