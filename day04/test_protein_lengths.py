import pytest

from app import parse_fasta


def test_single_protein_length():
    # One protein with six amino acids should have length 6.
    result = parse_fasta(">protein_one\nACDEFG")

    assert result == [{"name": "protein_one", "length": 6}]


def test_multiple_protein_lengths():
    # Each FASTA record should be returned with its own name and length.
    result = parse_fasta(">first\nACD\n>second\nWYKL")

    assert result == [
        {"name": "first", "length": 3},
        {"name": "second", "length": 4},
    ]


def test_sequence_split_across_lines():
    # Sequence lines in one FASTA record should be joined before counting.
    result = parse_fasta(">protein_one\nACD\nEFG")

    assert result == [{"name": "protein_one", "length": 6}]


@pytest.mark.parametrize("fasta_text", ["", "ACDEFG"])
def test_empty_or_invalid_fasta(fasta_text):
    # Empty input and sequence text without a FASTA header should be rejected.
    with pytest.raises(ValueError):
        parse_fasta(fasta_text)