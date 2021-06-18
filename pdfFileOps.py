import PyPDF2
# reading a pdf
# Notice we read it as a binary with 'rb'
with open('test_files/test.pdf','rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    print(pdf_reader.numPages)
    page_one = pdf_reader.getPage(0)
    print(page_one.extractText(), end='')
    #f.close() # context manager is handling it
print()
# writing to a pdf
with open('test_files/test.pdf','rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    page_one = pdf_reader.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)
    pdf_output = open("test_files/test_res.pdf", "wb")
    pdf_writer.write(pdf_output)
    pdf_output.close()
    #f.close() # context manager is handling it
print()
# trying to grab all text from a file
with open('test_files/test_res.pdf','rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    # List of every page's text.
    # The index will correspond to the page number.
    # zero is a placehoder to make page 1 = index 1
    pdf_text = [0]
    for p in range(pdf_reader.numPages):
        page = pdf_reader.getPage(p)
        pdf_text.append(page.extractText())
    #f.close() # context manager is handling it
print(pdf_text)