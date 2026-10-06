from src import selam


def test_selam_regular_name():
    assert selam.selam("Ahmet") == "Selam, Ahmet!"


def test_selam_strips_whitespace():
    assert selam.selam("  Ayse  ") == "Selam, Ayse!"


def test_selam_empty_string():
    assert selam.selam("") == "Selam"


def test_selam_whitespace_only():
    assert selam.selam("   \t \n ") == "Selam"


def test_selam_non_string():
    assert selam.selam(123) == "Selam, 123!"


def test_selam_none():
    assert selam.selam(None) == "Selam"


def test_selam_unicode():
    assert selam.selam("你好") == "Selam, 你好!"
