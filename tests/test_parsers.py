# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    fasta_file = FastaParser('tests/bad.fa')
    with pytest.raises(ValueError):
        list(fasta_file)

    fasta_file = FastaParser('tests/blank.fa')
    with pytest.raises(ValueError):
        list(fasta_file)

    fasta_file = FastaParser('data/test.fa')
    fasta = list(fasta_file)
    assert fasta[0][0] == "seq0"
    assert fasta[0][1] == "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"




def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. if a fastq file is
    read, the first item is None
    """
    fasta_true = FastaParser('data/test.fa')
    fasta = list(fasta_true)
    assert fasta[0][0] is not None

    fasta_false = FastaParser('data/test.fq')
    fastq = list(fasta_false)
    assert fastq[0][0] is None



def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_file = FastqParser('tests/bad.fq')
    with pytest.raises(ValueError):
        list(fastq_file)

    fastq_file = FastqParser('tests/blank.fq')
    with pytest.raises(ValueError):
        list(fastq_file)

    fastq_file = FastqParser('data/test.fq')
    fastq = list(fastq_file)
    assert fastq[0][0] == "seq0"
    assert fastq[0][1] == "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG"
    assert fastq[0][2] == """*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="""

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_true = FastqParser('data/test.fq')
    fastq = list(fastq_true)
    assert fastq[0][0] is not None

    fastq_false = FastqParser('data/test.fa')
    fasta = list(fastq_false)
    assert fasta[0][0] is None