from blabel import LabelWriter
import os
import PyPDF2

BIN_TEMPLATE=           'label_templates/bin-template.html'
BIN_STYLE=              'label_templates/bin-style.css'
KANBAN_TEMPLATE=        'label_templates/kanban-template.html'
KANBAN_STYLE=           'label_templates/kanban-style.css'
PART_TEMPLATE=          'label_templates/part-template.html'
PART_STYLE=             'label_templates/part-style.css'
BAG_TEMPLATE=           'label_templates/bag-template.html'
BAG_STYLE=              'label_templates/bag-style.css'
SITE_KANBAN_TEMPLATE=   'label_templates/site-kanban.html'
SITE_KANBAN_STYLE=      'label_templates/site-kanban.css'


def generate_labels(request):

    style = ''
    template = ''

    match request["Label Type"]:
        case "Bin":
            style = BIN_STYLE
            template = BIN_TEMPLATE

        case "Part":
            style = PART_STYLE
            template = PART_TEMPLATE

        case "Bag":
            style = BAG_STYLE
            template = BAG_TEMPLATE

        case "Kanban":
            style = KANBAN_STYLE
            template = KANBAN_TEMPLATE

        case "SiteKanban":
            style = SITE_KANBAN_STYLE
            template = SITE_KANBAN_TEMPLATE

    label_writer = LabelWriter(template, default_stylesheets=(style,))

    label_writer.write_labels(request["Rows"], target='unrotated_labels.pdf')

    if request["Label Type"] != "SiteKanban":
        rotate()


def rotate():

    pdf_in = open('unrotated_labels.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):

        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(90)
        pdf_writer.addPage(page)

    pdf_out = open('labels.pdf', 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

def test():

    label_writer = LabelWriter(SITE_KANBAN_TEMPLATE, default_stylesheets=(SITE_KANBAN_STYLE,))

    label_writer.write_labels([dict(url="gdofjknkfjb")], target='unrotated_labels.pdf')

test()