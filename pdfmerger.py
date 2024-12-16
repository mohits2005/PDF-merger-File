import PyPDF2


pdfiles = [r"D:\Python related\Pythonnn\1.pdf", r"D:\Python related\Pythonnn\2.pdf"]
output_file = r"D:\Python related\Pythonnn\Merged.pdf"
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
  
    merger.append(filename)
    

merger.write(output_file)
merger.close()

print("Pdf merged succesfully")