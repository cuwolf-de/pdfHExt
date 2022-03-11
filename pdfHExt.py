# DEPENDENCYS: You need to install pdfrw via:  pip install pdfrw

# import pdfrw

def print_Dependencies():
    print("Dependencies:")
    print("  This program uses the following python libraries:")
    print("    - sys  (should be installed with python per default)")
    print("    - os   (should be installed with python per default)")
    print("    - pdfrw  (use 'pip install pdfrw' to install this library)")

try:
    import sys
    import os
    from pdfrw import PageMerge, PdfReader, PdfWriter, PdfDict, PdfName
except:
    print("------------------------------------------------------------------")
    print("")
    print("")
    print("ERROR : Please install the required dependencies first!")
    print("")
    print_Dependencies()
    print("")
    print("")
    print("------------------------------------------------------------------")

scripts_path = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("------------------------------------------------------------------")
    print(" Usage:")
    print("    python pdfHExt.py input output [template]")
    print(" Parameters:")
    print("    input")
    print("       being the path/filename to the source pdf")
    print("    output")
    print("       being the path/filename to write the new generated pdf")
    print("    template (optional)")
    print("       being the path/filename for the background")
    print(" What it does:")
    print("    This program will paste each page of the pdf-file 'input'")
    print("    onto a larger sized page called template.")
    print("    If no template is given, then a default tempalte is used.")
    print("    The input pages are pasted on the left, vertically centered")
    print("    side of each page, so you have enough space on the right to")
    print("    annotate each page with your desired hand writing program")
    print("    like Xournal, Xournal++, GoodNotes, etc.")
    print_Dependencies()
    print("------------------------------------------------------------------")
    sys.exit(0)

def blankPage(template):
    x = PdfDict()
    x.Type = PdfName.Page
    x.Contents = PdfDict(stream="")
    x.MediaBox = template.inheritable.MediaBox
    return x

inFilename = sys.argv[1]
outFilename = sys.argv[2]
templateFilename = os.path.join(scripts_path,"3xDinA4.pdf")
if len(sys.argv) == 4:
    templateFilename = sys.argv[3]

background_pages = PdfReader(templateFilename)
background = background_pages.pages[0]
background_PM = PageMerge().add(background)[0]
content = PdfReader(inFilename)

pdfOut = PdfWriter(outFilename)

for i in range(len(content.pages)):
    content_page = content.pages[i]
    content_page_PM = PageMerge().add(content_page)[0]

    outPage = blankPage(background)
    outPage = PageMerge(outPage).add(background_PM, prepend=False).render()
    outPage = PageMerge(outPage).add(content_page_PM, prepend=False).render()
    
    pdfOut.addpage(outPage)

#PdfWriter(outFilename, trailer=content).write()
pdfOut.write()