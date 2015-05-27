__author__ = "sm4"
__version__ = "0.0.1"

import bz2
import sys
import collections

import xml.etree.cElementTree as ET
import unicodedata

TEXT = "{http://www.mediawiki.org/xml/export-0.10/}text"

def parse(source):
    counter = collections.Counter()
    index = 0
    context = ET.iterparse(source, events=("start", "end"))
    for event, elem in context:
        if event == "end" and elem.tag == TEXT:
            for x in str(elem.text):
                try:
                    if unicodedata.name(x).startswith("CJK UNIFIED IDEOGRAPH"):
                        counter.update(x)
                except ValueError:
                    pass

            index += 1
            if index % 100 == 0:
                print("Progress: " + str(index))
        elem.clear()
    return counter

def main():
    source = bz2.BZ2File(sys.argv[1], 'r')

    c = parse(source)

    targetJson = open(sys.argv[2] + ".json", 'w', encoding="utf-8")
    targetJson.write(str(c).replace("'", '"').replace("Counter(", "").replace(")", ""))

    targetCsv = open(sys.argv[2] + ".csv", 'w', encoding="utf-8")

    try:
        most_common_limit = int(sys.argv[3])
    except IndexError:
        most_common_limit = None

    most_common = c.most_common(most_common_limit);
    for kanji in most_common:
        targetCsv.write(kanji[0] + ", " + str(kanji[1]))
        targetCsv.write("\n")

if __name__ == "__main__":
    main()