"""Test contains selectors."""
from .. import util


class TestContains(util.TestCase):
    """Test contains selectors."""

    MARKUP = """
    <body>
    <div id="1">
    Testing
    <span id="2"> that </span>
    contains works.
    </div>
    </body>
    """

    def test_contains(self):
        """Test contains."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains(that)',
            ['2'],
            flags=util.HTML
        )

    def test_contains_quoted_with_space(self):
        """Test contains quoted with spaces."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains(" that ")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_quoted_without_space(self):
        """Test contains quoted with spaces."""

        self.assert_selector(
            self.MARKUP,
            'body :contains( "Testing" )',
            ['1'],
            flags=util.HTML
        )

    def test_contains_quoted_with_escaped_newline(self):
        """Test contains quoted with escaped newline."""

        self.assert_selector(
            self.MARKUP,
            'body :contains("Test\\\ning")',
            ['1'],
            flags=util.HTML
        )

    def test_contains_quoted_with_escaped_newline_with_carriage_return(self):
        """Test contains quoted with escaped newline with carriage return."""

        self.assert_selector(
            self.MARKUP,
            'body :contains("Test\\\r\ning")',
            ['1'],
            flags=util.HTML
        )

    def test_contains_list(self):
        """Test contains list."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains("does not exist", "that")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_multiple(self):
        """Test contains multiple."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains("th"):contains("at")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_multiple_not_match(self):
        """Test contains multiple with "not" and with a match."""

        self.assert_selector(
            self.MARKUP,
            'body span:not(:contains("does not exist")):contains("that")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_multiple_not_no_match(self):
        """Test contains multiple with "not" and no match."""

        self.assert_selector(
            self.MARKUP,
            'body span:not(:contains("that")):contains("that")',
            [],
            flags=util.HTML
        )

    def test_contains_with_descendants(self):
        """Test that contains returns descendants as well as the top level that contain."""

        self.assert_selector(
            self.MARKUP,
            'body :contains(" that ")',
            ['1', '2'],
            flags=util.HTML
        )

    def test_contains_bad(self):
        """Test contains when it finds no text."""

        self.assert_selector(
            self.MARKUP,
            'body :contains(bad)',
            [],
            flags=util.HTML
        )

    def test_contains_escapes(self):
        """Test contains with escape characters."""

        markup = """
        <body>
        <div id="1">Testing<span id="2">
        that</span>contains works.</div>
        </body>
        """

        self.assert_selector(
            markup,
            r'body span:contains("\0a that")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_cdata_html(self):
        """Test contains CDATA in HTML5."""

        markup = """
        <body><div id="1">Testing that <span id="2"><![CDATA[that]]></span>contains works.</div></body>
        """

        self.assert_selector(
            markup,
            'body *:contains("that")',
            ['1'],
            flags=util.HTML
        )

    def test_contains_cdata_xhtml(self):
        """Test contains CDATA in XHTML."""

        markup = """
        <div id="1">Testing that <span id="2"><![CDATA[that]]></span>contains works.</div>
        """

        self.assert_selector(
            self.wrap_xhtml(markup),
            'body *:contains("that")',
            ['1', '2'],
            flags=util.XHTML
        )

    def test_contains_cdata_xml(self):
        """Test contains CDATA in XML."""

        markup = """
        <div id="1">Testing that <span id="2"><![CDATA[that]]></span>contains works.</div>
        """

        self.assert_selector(
            markup,
            '*:contains("that")',
            ['1', '2'],
            flags=util.XML
        )

    def test_contains_iframe(self):
        """Test contains with `iframe`."""

        markup = """
        <div id="1">
        <p>Testing text</p>
        <iframe>
        <html><body>
        <span id="2">iframe</span>
        </body></html>
        </iframe>
        </div>
        """

        self.assert_selector(
            markup,
            'div:contains("iframe")',
            [],
            flags=util.PYHTML
        )

        self.assert_selector(
            markup,
            'div:contains("text")',
            ['1'],
            flags=util.PYHTML
        )

        self.assert_selector(
            markup,
            'span:contains("iframe")',
            ['2'],
            flags=util.PYHTML
        )

    def test_contains_iframe_xml(self):
        """Test contains with `iframe` which shouldn't matter in XML."""

        markup = """
        <div id="1">
        <p>Testing text</p>
        <iframe>
        <html><body>
        <span id="2">iframe</span>
        </body></html>
        </iframe>
        </div>
        """

        self.assert_selector(
            markup,
            'div:contains("iframe")',
            ['1'],
            flags=util.XML
        )

        self.assert_selector(
            markup,
            'div:contains("text")',
            ['1'],
            flags=util.XML
        )

        self.assert_selector(
            markup,
            'span:contains("iframe")',
            ['2'],
            flags=util.XML
        )

    def test_contains_with_same_tag_name(self):
        """Test contains to show the necessity of contains-own."""
        markup = """
        <body>
        <div id="1">
        A simple test
        <div id="2"> to </div>
        show the necessity of contains-own.
        </div>
        </body>
        """
        self.assert_selector(
            markup,
            'body div:contains(to)',
            ['1', '2'],
            flags=util.HTML
        )

    def test_contains_own(self):
        """Test contains-own."""

        self.assert_selector(
            self.MARKUP,
            'body div:contains-own(that)',
            [],
            flags=util.HTML
        )

    def test_contains_own_quoted_with_space(self):
        """Test contains-own quoted with spaces."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains-own(" that ")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_own_quoted_without_space(self):
        """Test contains-own quoted with spaces."""

        self.assert_selector(
            self.MARKUP,
            'body :contains-own( "Testing" )',
            ['1'],
            flags=util.HTML
        )

    def test_contains_own_quoted_with_escaped_newline(self):
        """Test contains-own quoted with escaped newline."""

        self.assert_selector(
            self.MARKUP,
            'body :contains-own("Test\\\ning")',
            ['1'],
            flags=util.HTML
        )

    def test_contains_own_quoted_with_escaped_newline_with_carriage_return(self):
        """Test contains-own quoted with escaped newline with carriage return."""

        self.assert_selector(
            self.MARKUP,
            'body :contains-own("Test\\\r\ning")',
            ['1'],
            flags=util.HTML
        )

    def test_contains_own_list(self):
        """Test contains-own list."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains-own("does not exist", "that")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_own_multiple(self):
        """Test contains-own multiple."""

        self.assert_selector(
            self.MARKUP,
            'body span:contains-own("th"):contains-own("at")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_own_multiple_not_match(self):
        """Test contains-own multiple with "not" and with a match."""

        self.assert_selector(
            self.MARKUP,
            'body span:not(:contains-own("does not exist")):contains-own("that")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_own_multiple_not_no_match(self):
        """Test contains-own multiple with "not" and no match."""

        self.assert_selector(
            self.MARKUP,
            'body span:not(:contains-own("that")):contains-own("that")',
            [],
            flags=util.HTML
        )

    def test_contains_own_bad(self):
        """Test contains-own when it finds no text."""

        self.assert_selector(
            self.MARKUP,
            'body :contains-own(bad)',
            [],
            flags=util.HTML
        )

    def test_contains_own_escapes(self):
        """Test contains-own with escape characters."""

        markup = """
        <body>
        <div id="1">Testing<span id="2">
        that</span>contains works.</div>
        </body>
        """

        self.assert_selector(
            markup,
            r'body span:contains-own("\0a that")',
            ['2'],
            flags=util.HTML
        )

    def test_contains_own_cdata_html(self):
        """Test contains-own CDATA in HTML5."""

        markup = """
        <body><div id="1">Testing that <span id="2"><![CDATA[that]]></span>contains works.</div></body>
        """

        self.assert_selector(
            markup,
            'body *:contains-own("that")',
            ['1'],
            flags=util.HTML
        )

    def test_contains_own_cdata_xhtml(self):
        """Test contains-own CDATA in XHTML."""

        markup = """
        <div id="1">Testing that <span id="2"><![CDATA[that]]></span>contains works.</div>
        """

        self.assert_selector(
            self.wrap_xhtml(markup),
            'body *:contains-own("that")',
            ['1', '2'],
            flags=util.XHTML
        )

    def test_contains_own_cdata_xml(self):
        """Test contains-own CDATA in XML."""

        markup = """
        <div id="1">Testing that <span id="2"><![CDATA[that]]></span>contains works.</div>
        """

        self.assert_selector(
            markup,
            '*:contains-own("that")',
            ['1', '2'],
            flags=util.XML
        )

    def test_contains_own_iframe(self):
        """Test contains-own with `iframe`."""

        markup = """
        <div id="1">
        <p>Testing text</p>
        <iframe>
        <html><body>
        <span id="2">iframe</span>
        </body></html>
        </iframe>
        </div>
        """

        self.assert_selector(
            markup,
            'div:contains-own("iframe")',
            [],
            flags=util.PYHTML
        )

        self.assert_selector(
            markup,
            'div:contains-own("text")',
            [],
            flags=util.PYHTML
        )

        self.assert_selector(
            markup,
            'span:contains-own("iframe")',
            ['2'],
            flags=util.PYHTML
        )

    def test_contains_own_iframe_xml(self):
        """Test contains-own with `iframe` which shouldn't matter in XML."""

        markup = """
        <div id="1">
        <p>Testing text</p>
        <iframe>
        <html><body>
        <span id="2">iframe</span>
        </body></html>
        </iframe>
        </div>
        """

        self.assert_selector(
            markup,
            'div:contains-own("iframe")',
            [],
            flags=util.XML
        )

        self.assert_selector(
            markup,
            'div:contains-own("text")',
            [],
            flags=util.XML
        )

        self.assert_selector(
            markup,
            'span:contains-own("iframe")',
            ['2'],
            flags=util.XML
        )

    def test_contains_own_with_same_tag_name(self):
        """Test contains-own to show the difference."""
        markup = """
        <body>
        <div id="1">
        A simple test
        <div id="2"> to </div>
        show the necessity of contains-own.
        </div>
        </body>
        """
        self.assert_selector(
            markup,
            'body div:contains-own(to)',
            ['2'],
            flags=util.HTML
        )

    def test_contains_own_with_broken_text(self):
        """Test contains-own to see how it matches a broken text."""
        markup = """
        <body>
        <div id="1"> A simple test <div id="2"> to </div> show the broken text case. </div>
        </body>
        """
        self.assert_selector(
            markup,
            'body div:contains-own("test  show")',
            [],
            flags=util.HTML
        )
