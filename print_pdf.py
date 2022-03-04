#import tempfile
import win32print
import locale
import ghostscript
import os

def print_pdf(filename):
    f=os.path.join(os.getcwd(), filename).replace('\\', '\\\\')

    args = [
        "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
        "-q",
        "-dNumCopies#1",
        "-dPDFFitPage",
        "-sDEVICE#mswinpr2",
        f"-dDEVICEWIDTHPOINTS=166.5",
        f"-dDEVICEHEIGHTPOINTS=288",
        f'-sOutputFile#"%printer%{win32print.GetDefaultPrinter()}"',
        f'"{f}"'
    ]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)
