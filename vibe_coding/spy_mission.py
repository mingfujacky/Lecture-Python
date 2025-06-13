from pathlib import Path
from shutil import copy2
from fpdf import FPDF


# Set environment
operation_dir = Path.cwd() / 'restricted' / 'assets' / 'mission'
data_dir = operation_dir / 'data'
log_file = operation_dir / 'log.txt'
with open(log_file, 'w') as f:
    f.write("Mission Log:\n")

def log_action(action):
    with log_file.open('a') as f:
        f.write(f"{action}\n")

def abs_to_rel(path):
    return path.relative_to(Path.cwd())
  

# Create a 'data' folder under operation_dir
if not data_dir.exists():
    data_dir.mkdir(parents=True, exist_ok=True)
    log_action(f"Created folder: {abs_to_rel(data_dir)}")
else:
    log_action(f"Folder already exists: {abs_to_rel(data_dir)}")

# Copy all image files in operation_dir into data_dir
for img_file in operation_dir.glob('*.[jp][pn]g'):
    dest = data_dir / img_file.name
    copy2(img_file, dest)
    log_action(f"Copied {abs_to_rel(img_file)} to {abs_to_rel(dest)}")

# Copy briefing.txt to data_dir
briefing_src = operation_dir / 'briefing.txt'
briefing_dest = data_dir / 'briefing.txt'
if briefing_src.exists():
    copy2(briefing_src, briefing_dest)
    log_action(f"Copied {abs_to_rel(briefing_src)} to {abs_to_rel(briefing_dest)}")
else:
    log_action(f"briefing.txt not found in {abs_to_rel(operation_dir)}")

# Sort note*.txt files in alphabetic order and append all contents to data_dir/briefing.txt
note_files = sorted(operation_dir.glob('note*.txt'))
briefing_dest = data_dir / 'briefing.txt'
with briefing_dest.open('a') as briefing_f:
    for note_file in note_files:
        with note_file.open('r') as nf:
            briefing_f.write(f"\n--- {note_file.name} ---\n")
            briefing_f.write(nf.read())
log_action(f"Appended contents of {len(note_files)} note*.txt files to {abs_to_rel(briefing_dest)}")

# Convert data folder briefing.txt into PDF format
briefing_txt = data_dir / 'briefing.txt'
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

# Delete data folder briefing.txt if it exists
briefing_txt = data_dir / 'briefing.txt'
if briefing_txt.exists():
    briefing_txt.unlink()
    log_action(f"Deleted {abs_to_rel(briefing_txt)}")
else:
    log_action(f"{abs_to_rel(briefing_txt)} not found, nothing deleted")    