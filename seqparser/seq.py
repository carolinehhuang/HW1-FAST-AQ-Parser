# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    all_allowed = all(x in ALLOWED_NUC for x in seq)
    if not all_allowed:
        raise ValueError("Sequence contains invalid nucleotides")
    rna_seq = seq.translate(str.maketrans(TRANSCRIPTION_MAPPING))
    return rna_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    rna_seq = transcribe(seq)  # replace U
    rna_reverse = rna_seq[::-1]
    # Hey this is my comment
    # Again!
    return rna_reverse