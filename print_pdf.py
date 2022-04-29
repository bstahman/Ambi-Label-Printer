#import tempfile
import win32print
import locale
import ghostscript
import os

def print_pdf(file_name, printer_name):

    f=os.path.join(os.getcwd(), file_name).replace('\\', '\\\\')

    args = [
        "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
        "-q",
        "-dNumCopies#1",
        "-dPDFFitPage",
        "-dAutoRotatePages=/All",
        "-sDEVICE#mswinpr2",
        f"-dDEVICEWIDTHPOINTS=166.5",
        f"-dDEVICEHEIGHTPOINTS=288",
        f'-sOutputFile#"%printer%{printer_name}"',
        f'"{f}"'
    ]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)
