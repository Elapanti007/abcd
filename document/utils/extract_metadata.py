import PyPDF2

def extract_pdf_metadata(file_path):
    default_info = {
        'Title': 'Not available',
        'Author': 'Not available',
        'Subject': 'Not available',
        'Keywords': 'Not available',
        'Creator': 'Not available',
        'Producer': 'Not available',
        'CreationDate': 'Not available',
        'ModDate': 'Not available',
        'Trapped': 'Not available'
    }

    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            metadata = reader.metadata
            document_info = {key: metadata.get(key, default_info[key]) for key in default_info}
            return document_info
    except Exception as e:
        return default_info  # Return default info in case of an error
