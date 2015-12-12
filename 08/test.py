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
    assert es.unescape() == "test ' ok"


def test_double_escape_quotes():
    # "" encodes to "\"\"", an increase from 2 characters to 6.
    es = EscapedString('""')
    assert '"\\"\\""' == es.escape()

    # "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
    es = EscapedString('"abc"')
    assert '"\\"abc\\""' == es.escape()


def test_double_escape_slashes():
    # "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
    es = EscapedString('"aaa\\"aaa"')
    assert '"\\"aaa\\\\\\"aaa\\""' == es.escape()

    # "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
    es = EscapedString('"\\x27"')
    assert '"\\"\\\\x27\\""' == es.escape()
