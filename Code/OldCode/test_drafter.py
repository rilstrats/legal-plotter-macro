import pytest
import legal_drafting

def test_define_line():
    pass

def test_define_curve():
    assert legal_drafting.define_curve("OF 125.00 FT RAD CUR CNCV SELY NELY RT ALG ARC OF SD CUR 95.42 FT THRU CTL ANG OF 43*44'06\" (LNG CHD BEARING N17*26'17\" E 93.12 FT)") == ["curve", "r", "125.00", "l", "95.42"]


pytest.main(["-v", "--tb=no", "test_drafter.py"])