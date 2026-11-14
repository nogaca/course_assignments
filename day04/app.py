from flask import Flask, render_template, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


def parse_fasta(fasta_text):
    """Return protein names and lengths from FASTA-formatted text."""
    proteins = []
    protein_name = None
    sequence_parts = []

    for line in fasta_text.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith(">"):
            if protein_name is not None:
                sequence = "".join(sequence_parts)
                if not sequence:
                    raise ValueError(f"The sequence for '{protein_name}' is empty.")
                proteins.append({"name": protein_name, "length": len(sequence)})

            protein_name = line[1:].strip()
            if not protein_name:
                raise ValueError("Every FASTA header needs a protein name after '>'.")
            sequence_parts = []
        else:
            if protein_name is None:
                raise ValueError("Sequence text must start with a FASTA header beginning with '>'.")
            sequence_parts.append(line)

    if protein_name is None:
        raise ValueError("Enter or upload at least one FASTA sequence.")

    sequence = "".join(sequence_parts)
    if not sequence:
        raise ValueError(f"The sequence for '{protein_name}' is empty.")
    proteins.append({"name": protein_name, "length": len(sequence)})

    return proteins


@app.route("/", methods=["GET", "POST"])
def index():
    """Show the input form and analyze pasted or uploaded FASTA text."""
    results = None
    error = None

    if request.method == "POST":
        input_mode = request.form.get("input_mode", "paste")

        try:
            if input_mode == "upload":
                fasta_file = request.files.get("fasta_file")
                if fasta_file is None or not fasta_file.filename:
                    raise ValueError("Choose a FASTA file to analyze.")
                try:
                    fasta_text = fasta_file.read().decode("utf-8")
                except UnicodeDecodeError as exc:
                    raise ValueError("The uploaded file must be a UTF-8 text file.") from exc
            else:
                fasta_text = request.form.get("fasta_text", "")

            results = parse_fasta(fasta_text)
        except ValueError as exc:
            error = str(exc)

    return render_template("index.html", results=results, error=error)


if __name__ == "__main__":
    app.run(debug=True)