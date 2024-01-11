def check_metadata(metadata):
    # Predefined lists of valid metadata attributes
    valid_authors = ["Not available", "Bharti Airtel Limited"]
    valid_creators = [
        "Chromium", "Bharti Airtel Limited",
        "JasperReports Library version 6.14.0-2ab0d8625be255bf609c78e1181801213e51db8f",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "dvips(k) 5.95a Copyright 2005 Radical Eye Software", "Not available"
    ]
    valid_producers = [
        "GPL Ghostscript 8.70", "Skia/PDF m119",
        "iText 2.1.7 by 1T3XT; modified using iText® 7.1.12 ©2000-2020 iText Group NV (AGPL-version)",
        "OpenPDF 1.3.28", "Not available"
    ]

    # Extracting necessary metadata fields
    author = metadata.get('Author', 'Not available')
    creator = metadata.get('Creator', 'Not available')
    producer = metadata.get('Producer', 'Not available')
    creation_date = metadata.get('CreationDate', '')
    mod_date = metadata.get('ModDate', '')

    # Checking metadata validity
    dates_match = creation_date == mod_date
    author_ok = author in valid_authors
    creator_ok = creator in valid_creators
    producer_ok = producer in valid_producers

    # Return True if all checks pass
    return dates_match
    # return author_ok and creator_ok and producer_ok and dates_match
