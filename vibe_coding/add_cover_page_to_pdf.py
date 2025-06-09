from pathlib import Path
from PyPDF2 import PdfMerger
import re

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(str(pdf))
    merger.write(str(output_path))
    merger.close()

if __name__ == "__main__":
    covers_dir = Path("./restricted/assets/covers")
    reports_dir = Path("./restricted/assets/reports")
    finals_dir = Path("./restricted/assets/finals")

    finals_dir.mkdir(parents=True, exist_ok=True)

    # Find all cover*.pdf files and extract their numbers
    for cover_pdf in covers_dir.glob("cover*.pdf"):
        match = re.match(r"cover(\d+)\.pdf", cover_pdf.name)
        if match:
            num = match.group(1)
            report_pdf = reports_dir / f"{num}.pdf"
            output_file = finals_dir / f"final{num}.pdf"
            if report_pdf.exists():
                merge_pdfs([cover_pdf, report_pdf], output_file)
                print(f"Merged {[cover_pdf, report_pdf]} into {output_file}")
            else:
                print(f"Missing file: {report_pdf}")