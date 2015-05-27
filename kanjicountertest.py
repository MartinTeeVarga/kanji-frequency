__author__ = 'sm4'

import unittest
import io
from kanjicounter import *

XML = str("""<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="ja">
    <foo>
        <bar>
            <text xml:space="preserve">日本の日の出</text>
            <something>X</something>
        </bar>
    </foo>
    <foo>
        <bar>
            <text xml:space="preserve">日本の日</text>
        </bar>
    </foo>
    </mediawiki>
""")

class TestKanjiCounter(unittest.TestCase):

    def test_parse(self):
        with io.StringIO() as f:
            f.write(XML)
            f.seek(0)
            kc = KanjiCounter()
            result = kc.parse(f)
            expected = collections.Counter(str("日日日日本本出"))
            self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()