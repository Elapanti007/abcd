import streamlit as st
import os
import io
import hashlib

from utils.document_hash import calculate_hash
from utils.document_upload import upload_document
from utils.extract_gstin import extract_gstin
from utils.extract_text import extract_text_from_pdf
from utils.extract_metadata import extract_pdf_metadata
from utils.metadata_checker import check_metadata
from utils.qr_code_extractor import extract_images_and_decode_qr

# Set the upload folder and maximum content length
UPLOAD_FOLDER = 'uploads/'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB upload limit
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Custom navigation bar
nav_bar_html = """
<div style="background-color:#D41C2C;padding:10px;">
    <img src='data:image/png;base64,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' style='height:50px;float:left;margin-right:10px;' />
    <h2 style='color:white;text-align:center;margin:0;'>PDF Upload and Analysis</h2>
</div>
"""

st.markdown(nav_bar_html, unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()  # Read bytes directly
    hash_of_uploaded_file = hashlib.sha256(bytes_data).hexdigest()

    # Check if file with the same hash exists
    is_duplicate = any(
        hash_of_uploaded_file == calculate_hash(os.path.join(UPLOAD_FOLDER, existing_filename))
        for existing_filename in os.listdir(UPLOAD_FOLDER)
    )

    if is_duplicate:
        st.error("This document already exists.")
    else:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

        # Save the uploaded PDF if it's not a duplicate
        with open(file_path, 'wb') as f:
            f.write(bytes_data)

        # Continue processing the PDF
        metadata = extract_pdf_metadata(file_path)

        # Check if metadata is available
        if all(value == 'Not available' for value in metadata.values()):
            st.write("No metadata available for this document.")
        else:
            st.json(metadata)
        is_good = check_metadata(metadata)
        qr_contents = extract_images_and_decode_qr(file_path, UPLOAD_FOLDER)
        pdf_text = extract_text_from_pdf(file_path)
        gstin = extract_gstin(pdf_text)

        # Display results
        st.success("Document uploaded successfully.")
        st.json(metadata)

        if is_good:
            st.success("Metadata is good.")
        else:
            st.warning("Metadata check failed.")

        st.write("QR Contents:")
        st.write(qr_contents)

        st.write("Extracted Text:")
        st.write(pdf_text)

        if gstin:
            st.write("Extracted GSTIN:")
            st.write(gstin)
