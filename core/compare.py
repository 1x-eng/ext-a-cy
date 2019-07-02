import difflib
import sys

__author__='Pruthvi Kumar'
# 30 June 2019.
# pruthvikumar.123@gmail.com
# Compare 2 files line by line and report difference.


class Compare:

    def __init__(self, file1, file2):
        super(Compare, self).__init__()
        self.file1 = file1
        self.file2 = file2

    def compare(self):
        with open(self.file1, 'r') as f0:
            with open(self.file2, 'r') as f1:
                diff = difflib.unified_diff(
                    f0.readlines(),
                    f1.readlines(),
                    fromfile='f0',
                    tofile='f1',
                )
                for line in diff:
                    sys.stdout.write(line)
