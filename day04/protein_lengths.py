from pathlib import Path

from openpyxl import Workbook


# Use the FASTA file and save the Excel file in this script's folder.
folder = Path(__file__).parent
fasta_file = folder / "best-rhod_complete_seq.fasta"
excel_file = folder / "best-rhod_protein_lengths.xlsx"

# Read each FASTA record, joining its sequence lines before counting residues.
proteins = []
protein_name = None
sequence_parts = []

with fasta_file.open() as fasta:
    for line in fasta:
        line = line.strip()
        if not line:
            continue

        if line.startswith(">"):
            if protein_name is not None:
                proteins.append((protein_name, len("".join(sequence_parts))))
            protein_name = line[1:].strip()
            sequence_parts = []
        else:
            sequence_parts.append(line)

# Add the last protein after reaching the end of the file.
if protein_name is not None:
    proteins.append((protein_name, len("".join(sequence_parts))))

# Write the protein names and lengths to an Excel workbook.
workbook = Workbook()
sheet = workbook.active
sheet.append(["protein name", "protein length"])

for name, length in proteins:
    sheet.append([name, length])
    print(f"{name}: {length} amino acids")

workbook.save(excel_file)
print(f"Excel file saved: {excel_file}")