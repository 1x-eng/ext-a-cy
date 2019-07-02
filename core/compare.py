import difflib
import sys

__author__='Pruthvi Kumar'
# 01 July 2019.
# pruthvikumar.123@gmail.com
# Compare 2 files line by line and report difference.


class ComparePages:

    def __init__(self, file1, file2):
        super(ComparePages, self).__init__()
        self.file1 = file1
        self.file2 = file2

    def compare(self):
        try:
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

        except Exception as e:
            print('Unable to complete comparing {} and {}. Stack trace to follow.'.format(self.file1, self.file2))
            print(str(e))

