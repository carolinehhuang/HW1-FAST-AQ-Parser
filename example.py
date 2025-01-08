from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fasta_parse = FastaParser('/Users/carolinehuang/HW1-FAST-AQ-Parser/data/test.fa')
    # Create instance of FastqParser
    fastq_parse = FastqParser('/Users/carolinehuang/HW1-FAST-AQ-Parser/data/test.fq')
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    # For each record of FastqParser, Transcribe the sequence

    for record in fasta_parse:
        print(record[0] + " " + transcribe(record[1]))

    for recordq in fastq_parse:
        print(recordq[0] + " " + transcribe(recordq[1]))

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for reverse in fasta_parse:
        print(reverse[0] + " " + reverse_transcribe(reverse[1]))

    for reverseq in fastq_parse:
        print(reverseq[0] + " " + reverse_transcribe(reverseq[1]))



"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
