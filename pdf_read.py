from pdfminer.high_level import extract_text


def get_text(path):
    pdf_read = extract_text(path)

    return pdf_read
