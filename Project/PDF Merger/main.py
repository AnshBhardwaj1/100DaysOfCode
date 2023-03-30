from PyPDF2 import PdfWriter
import os
from click import clear

merger=PdfWriter()
files=os.listdir("All PDFs")
files.sort()
notdone=[]
for file in files:
    if file.endswith(".pdf"): 
        try:
            merger.append(f"All PDFs/{file}")
            print (f"Currently merging {file}")
            os.remove(f"All PDFs/{file}")
        except:
            print (f"{file} has an error")
            #os.rename(f"All PDFs/{file}",f"All PDFs/Not merged/{file}")
            notdone.append(f"{file} becuase of encryption")
    else:
        print (f"The {file} is not a pdf")
        notdone.append(f"{file} because its not a pdf")
        os.system(file)
merger.write("All PDFs/Final/Merged file.pdf")
merger.close()
print ("Merged PDF is present at All PDFs -> Final")
print ("The following files were not merged")
for ind,fil in enumerate(notdone):
    print (f"{ind+1}. {fil}")