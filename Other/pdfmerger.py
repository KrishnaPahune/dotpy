import PyPDF2
merger = PyPDF2.PdfMerger()
pdf_files=[r"c:/Users/krish/OneDrive/Desktop/DA/Tableau/Tableau-Charts-_-Cheat-Sheet.pdf",r"c:/Users/krish/OneDrive/Desktop/DA/Tableau/Tableau-Concepts_-Cheat-Sheet.pdf",r"c:/Users/krish/OneDrive/Desktop/DA/Tableau/Tableau-Functions-_-Cheat-Sheet.pdf",r"c:/Users/krish/OneDrive/Desktop/DA/Tableau/Tableau-Sketchnotes-1.pdf"]
for pdf in pdf_files:
    merger.append(pdf)

merger.write(r"c:/Users/krish/OneDrive/Desktop/DA/Tableau/merged_pdfs.pdf")
merger.close()

print("pdf Merged Successfully")