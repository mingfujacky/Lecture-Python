from pathlib import Path
from shutil import copy2
from fpdf import FPDF
from datetime import datetime


# Set environment
operation_dir = Path.cwd() / 'restricted' / 'assets' / 'mission'
data_dir = operation_dir / 'data'
log_file = operation_dir / 'log.txt'

def abs_to_rel(path):
    return path.relative_to(Path.cwd())

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S - ")
    with log_file.open('a') as f:
        f.write(f"{timestamp}{action}\n")

def ensure_data_dir():
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        log_action(f"Created folder: {abs_to_rel(data_dir)}")
    else:
        log_action(f"Folder already exists: {abs_to_rel(data_dir)}")

def copy_images():
    for img_file in operation_dir.glob('*.[jp][pn]g'):
        dest = data_dir / img_file.name
        copy2(img_file, dest)
        log_action(f"Copied {abs_to_rel(img_file)} to {abs_to_rel(dest)}")

def copy_briefing():
    briefing_src = operation_dir / 'briefing.txt'
    briefing_dest = data_dir / 'briefing.txt'
    if briefing_src.exists():
        copy2(briefing_src, briefing_dest)
        log_action(f"Copied {abs_to_rel(briefing_src)} to {abs_to_rel(briefing_dest)}")
    else:
        log_action(f"briefing.txt not found in {abs_to_rel(operation_dir)}")
    return briefing_dest

def append_notes(briefing_dest):
    note_files = sorted(operation_dir.glob('note*.txt'))
    with briefing_dest.open('a') as briefing_f:
        for note_file in note_files:
            with note_file.open('r') as nf:
                briefing_f.write(f"\n--- {note_file.name} ---\n")
                briefing_f.write(nf.read())
    log_action(f"Appended contents of {len(note_files)} note*.txt files to {abs_to_rel(briefing_dest)}")

def txt_to_pdf(briefing_txt):
    briefing_pdf = data_dir / 'briefing.pdf'
    if briefing_txt.exists():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        with briefing_txt.open('r') as f:
            for line in f:
                pdf.cell(0, 10, txt=line.rstrip(), ln=1)
        pdf.output(str(briefing_pdf))
        log_action(f"Converted {abs_to_rel(briefing_txt)} to {abs_to_rel(briefing_pdf)}")
    else:
        log_action(f"{abs_to_rel(briefing_txt)} not found, PDF not created")

def delete_briefing_txt(briefing_txt):
    if briefing_txt.exists():
        briefing_txt.unlink()
        log_action(f"Deleted {abs_to_rel(briefing_txt)}")
    else:
        log_action(f"{abs_to_rel(briefing_txt)} not found, nothing deleted")

def main():
    with open(log_file, 'w') as f:
        f.write("Mission Log:\n")
    ensure_data_dir()
    copy_images()
    briefing_dest = copy_briefing()
    append_notes(briefing_dest)
    txt_to_pdf(briefing_dest)
    delete_briefing_txt(briefing_dest)

if __name__ == "__main__":
    main()