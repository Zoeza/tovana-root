import subprocess
import sys

def docx_to_pdf(doc_path, path):
    subprocess.call(['/usr/bin/soffice',
                     # '--headless',
                     '--convert-to',
                     'pdf',
                     '--outdir',
                     path,
                     doc_path])
    return doc_path

if __name__ == "__main__":
    doc_path = "/tovana-root/site/public/media/reports/3OFJ7PXY5U_Wellness.docx"
    path = "/tovana-root/site/public/media/reports/"
    docx_to_pdf(doc_path, path)