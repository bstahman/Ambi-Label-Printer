#import tempfile
import win32print
import locale
import ghostscript
import os

DYMO_PRINTER_NAME = 'DYMO LabelWriter 4XL'

def print_pdf(filename):

    f=os.path.join(os.getcwd(), filename).replace('\\', '\\\\')

    args = [
        "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
        "-q",
        "-dNumCopies#1",
        "-dPDFFitPage",
        "-dAutoRotatePages=/All",
        "-sDEVICE#mswinpr2",
        f"-dDEVICEWIDTHPOINTS=166.5",
        f"-dDEVICEHEIGHTPOINTS=288",
        f'-sOutputFile#"%printer%{DYMO_PRINTER_NAME}"',
        f'"{f}"'
    ]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)
