def docx_to_pdf(doc_path, path):
    import subprocess
    subprocess.call(['/usr/bin/soffice',
                     # '--headless',
                     '--convert-to',
                     'pdf',
                     '--outdir',
                     path,
                     doc_path])

if __name__ == "__main__":
    docx_to_pdf(doc_path, path)