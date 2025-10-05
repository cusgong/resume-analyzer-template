import sys
import fitz  # PyMuPDF

def pdf_to_text(pdf_path: str) -> str:
    """
    Convert a PDF file to plain text using PyMuPDF.
    Returns the extracted text as a string.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text")
    except Exception as e:
        sys.stderr.write(f"Error reading {pdf_path}: {e}\n")
        sys.exit(1)

    return text.strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_text.py <pdf_file_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    text = pdf_to_text(pdf_path)
    print(text)
