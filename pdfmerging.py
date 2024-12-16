from PyPDF2 import PdfMerger
import os


def merger_pdf(inp_pdf, output_name):
    merger = PdfMerger()
    
    inp_pdf = [file for file in os.listdir() if file.endswith(".pdf")]
    for pdf in inp_pdf:
        merger.append(pdf)
        
    merger.write(output_name)
    merger.close()
    
pdf_files = [r"D:\Python related\Pythonnn\PDFmerger\1.pdf", r"D:\Python related\Pythonnn\PDFmerger\2.pdf"]
merger_pdf(pdf_files, r"D:\Python related\Pythonnn\PDFmerger\merrrggee_output.pdf")