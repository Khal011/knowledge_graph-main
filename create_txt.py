import os
import fitz  # PyMuPDF
import docx2txt

def extract_text(file_path: str) -> str:
    """Extract text from a file.
    Args:
        file_path (str): Path to the file.
    Returns:
        str: Extracted text from the file.
    """
    text = ""
    if str(file_path).lower().endswith(".pdf"):
        pdf_document = fitz.open(file_path)
        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            page_text = page.get_text()
            text += page_text
        # Close the PDF file
        pdf_document.close()
    elif str(file_path).lower().endswith(".doc") or file_path.lower().endswith(".docx"):
        text = docx2txt.process(file_path)
    return text

def save_text_to_file(text: str, output_dir: str, file_name: str):
    """Save the extracted text to a new text file in the specified directory.
    Args:
        text (str): The text to save.
        output_dir (str): The directory where the text file will be saved.
        file_name (str): The name of the text file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, f"{file_name}.txt")
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

def process_files(input_dir: str, output_dir: str):
    """Process all PDF and DOC/DOCX files in the input directory and save the extracted text to the output directory.
    Args:
        input_dir (str): The directory containing the input files.
        output_dir (str): The directory where the output text files will be saved.
    """
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if file_name.lower().endswith(('.pdf', '.doc', '.docx')):
            print(f"Processing file: {file_name}")
            extracted_text = extract_text(file_path)
            save_text_to_file(extracted_text, output_dir, os.path.splitext(file_name)[0])

# Example usage
input_directory = "C:/Users/medkh/Desktop/Python/knowledge_graph-main/data_input/"
output_directory = "C:/Users/medkh/Desktop/Python/knowledge_graph-main/data_input/cureus/"
process_files(input_directory, output_directory)
