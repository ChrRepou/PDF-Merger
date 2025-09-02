PDF Merger
==========

This is a simple command-line tool for merging multiple PDF files into a single PDF document. It uses the PyPDF2 library in Python.

Prerequisites
-------------

Before running the script, make sure you have Python installed. You'll also need to install the PyPDF2 library. You can do this using pip:
```
pip install PyPDF2
```

How to Use
----------

To use the script, run it from your terminal or command prompt with the following syntax:
```
python <script_name>.py <output_file_name> <input_file_1.pdf> <input_file_2.pdf> ...
```

*   `<script_name>.py`: The name of your Python script file (e.g., `pdf_merger.py`).
    
*   `<output_file_name>`: The desired name for the merged output file. The script will automatically add the `.pdf` extension.
    
*   `<input_file_1.pdf> ...`: One or more PDF files to be merged.
    

### Example

Let's say you have three files: `file1.pdf`, `file2.pdf`, and `file3.pdf`. To merge them into a single file named `merged_document.pdf`, you would run:
```
python pdf_merger.py merged_document file1.pdf file2.pdf file3.pdf
```
Features
--------

*   **Multiple File Merging**: Easily merge any number of PDF files.
    
*   **Output Naming**: The output file name is specified as the first argument, making it simple to control the final file name.
    
*   **Overwrite Protection**: If the specified output file already exists, the script will ask for confirmation before overwriting it to prevent data loss.
    
*   **Error Handling**: The script includes basic error handling to catch common issues and provide a helpful error message.
    
*   **Usage Guide**: If you run the script with insufficient arguments, it will display a clear usage example.
