__author__ = "sm4"
__version__ = "0.0.1"

import bz2
import sys
import os
import kanjicounter
import collections


TEXT = "Text"

def main():

    rootdir = sys.argv[1]

    kc = kanjicounter.KanjiCounter()
    c = collections.Counter()

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            f = os.path.join(subdir, file)
            print("Parsing: " + f)
            c += kc.parse(f, TEXT)

    targetJson = open(sys.argv[2] + ".json", 'w', encoding="utf-8")
    targetJson.write(str(c).replace("'", '"').replace("Counter(", "").replace(")", ""))

    targetCsv = open(sys.argv[2] + ".csv", 'w', encoding="utf-8")

    try:
        most_common_limit = int(sys.argv[3])
    except IndexError:
        most_common_limit = None

    most_common = c.most_common(most_common_limit)
    for kanji in most_common:
        targetCsv.write(kanji[0] + ", " + str(kanji[1]))
        targetCsv.write("\n")

if __name__ == "__main__":
    main()