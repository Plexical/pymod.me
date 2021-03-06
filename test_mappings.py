import csv
import pytest

from pymod.mappings import url

def fixtures():
    with open('fixture.csv') as fp:
        return [row for row in csv.reader(fp) if row[0] != '-']

@pytest.mark.parametrize("version,term,expected", fixtures())
def test_mappings(version, term, expected):
    assert url(version, term) == expected, "Can't find {}".format(term)

def test_term_not_found():
    assert url('3', 'dontexist') == None
