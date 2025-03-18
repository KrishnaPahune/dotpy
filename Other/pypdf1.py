import PyPDF2
a = PyPDF2.PdfReader('C:/Users/krish/Downloads/Third_Year_Information-Technology_Syllabus.pdf')
str = ""
for i in range(1,11):
    str += a.pages[i].extract_text()

with open("pypdf.txt","w",encoding="utf-8") as f:
    f.write(str)