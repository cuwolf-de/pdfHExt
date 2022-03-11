# pdfHExt
Usage:
    python pdfHExt.py input output [template]


Parameters:
    input
       being the path/filename to the source pdf
    output
       being the path/filename to write the new generated pdf
    template (optional)
       being the path/filename for the background


What it does:
    This program will paste each page of the pdf-file 'input'
    onto a larger sized page called template.
    If no template is given, then a default tempalte is used.
    The input pages are pasted on the left, vertically centered
    side of each page, so you have enough space on the right to
    annotate each page with your desired hand writing program
    like Xournal, Xournal++, GoodNotes, etc.
