import PyPDF2 as pdf
import os
merge = pdf.PdfMerger()

desired_extension=".pdf"

current_folder_path = os.path.dirname(os.path.abspath(__file__))
list_pdfs=[]

for element in os.listdir():
    full_path = os.path.join(current_folder_path, element)

    if os.path.isfile(full_path) and element.endswith(desired_extension):
        list_pdfs.append(element)

list_pdfs.sort()

print("list of pdfs found: ")
print(list_pdfs)

print(f"merging {len(list_pdfs)} files...")

for file in list_pdfs:
    merge.append(file)

merge.write("merged.pdf")

print("Complete!")
