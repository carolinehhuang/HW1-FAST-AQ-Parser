# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    assert transcribe('ATGCTTTA') == 'UACGAAAU'

    with pytest.raises(ValueError):
        transcribe('ATT GCATTA')

    with pytest.raises(ValueError):
        transcribe('HELLOTONYANDTAS')



def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert reverse_transcribe('ATGCTTTA') == 'UAAAGCAU'

    with pytest.raises(ValueError): #space
        reverse_transcribe('ATT GCATTA')

    with pytest.raises(ValueError): #invalid chars
        reverse_transcribe('BMI203ISSOFUN')
