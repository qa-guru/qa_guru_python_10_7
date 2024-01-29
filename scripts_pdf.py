import os.path

import pypdf

reader = pypdf.PdfReader("resources/Python Testing with Pytest (Brian Okken) (1).pdf")

print(reader.pages)
print(reader.pages[1].extract_text())
print(os.path.getsize("resources/Python Testing with Pytest (Brian Okken) (1).pdf"))