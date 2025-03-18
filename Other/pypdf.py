import PyPDF2
a = PyPDF2.PdfReader('C:/Users/krish/Downloads/Third_Year_Information-Technology_Syllabus.pdf')
print(a.metadata)
print(len(a.pages))
print(a.pages[1].extract_text())