import PyPDF2
import sys
from pathlib import Path

def pdf_merger():
    if len(sys.argv) > 2:
        try:
            output_file_name = sys.argv[1] + '.pdf'
            input_files = sys.argv[2:]
            merger = PyPDF2.PdfMerger()
            for pdf in input_files:
                merger.append(pdf)
            if Path(output_file_name).exists():
                overwrite = input(f'File: {output_file_name} already exists. Overwrite? (y/n): ')
                if overwrite.lower() == 'y':
                    merger.write(output_file_name)
                    print(f'Your new pdf has been written to {output_file_name}.pdf successfully.')
                else:
                    print('Aborting.')
        except Exception as err:
            print(f'Error: {err}')
    else:
        print('You should execute PDF_merger output_file_name your_first.pdf your_second.pdf')

if __name__ == '__main__':
    pdf_merger()