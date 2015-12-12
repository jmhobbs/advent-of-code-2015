from escapestring import EscapedString


def test_no_escapes():
    es = EscapedString('"no escapes here"')
    assert es.string_length == 15
    assert es.code_length == 17


def test_basic_escape():
    es = EscapedString('"basic \\""')
    assert es.unescape() == 'basic "'


def test_hex_escape():
    es = EscapedString('"test \\x27 ok"')
    print es.unescape()
    assert es.unescape() == "test ' ok"
