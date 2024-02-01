from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_docx_to_pdf(docx_path, pdf_path):
    # Read the DOCX file
    doc = Document(docx_path)

    # Create a PDF file
    pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)

    # Loop through paragraphs in the DOCX file and write them to the PDF
    for paragraph in doc.paragraphs:
        pdf_canvas.drawString(100, 800, paragraph.text)  # Adjust coordinates as needed

    # Save the PDF file
    pdf_canvas.save()

if __name__ == "__main__":
    # Specify the paths to the input DOCX file and the output PDF file
    input_docx_path = "TrevorCV.docx"
    output_pdf_path = "trevorCV.pdf"

    # Convert DOCX to PDF
    convert_docx_to_pdf(input_docx_path, output_pdf_path)
