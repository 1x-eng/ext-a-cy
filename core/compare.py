import difflib
import os
import sys

__author__ = 'Pruthvi Kumar'


# 01 July 2019.
# pruthvikumar.123@gmail.com
# Compare 2 files line by line and report difference.


class ComparePages:

    def __init__(self, file1, file2, report_name):
        super(ComparePages, self).__init__()
        self.file1 = file1
        self.file2 = file2
        self.report_name = report_name

    def compare(self):
        try:
            # create a difference_report if not already existing
            os.makedirs('{}/../difference_report'.format(os.path.dirname(__file__)), exist_ok=True)

            with open(self.file1, 'r') as f0:
                with open(self.file2, 'r') as f1:
                    diff = difflib.unified_diff(
                        f0.readlines(),
                        f1.readlines(),
                        fromfile='f0',
                        tofile='f1',
                    )

                    for line in diff:
                        # sys.stdout.write(line)
                        sys.stdout = open(
                            '{}/../difference_report/{}_overall_changes.html'.format(os.path.dirname(__file__),
                                                                                     self.report_name), 'a')
                        print(line)

                        if line.startswith('+'):
                            sys.stdout = open(
                                '{}/../difference_report/{}_changed_contents.html'.format(os.path.dirname(__file__),
                                                                                          self.report_name), 'a')
                            if '+ f1' not in line and '+ f2' not in line and '- f1' not in line and '- f2' not in line and '!--' not in line and '-->' not in line:
                                print(line[1:])
                        else:
                            pass

        except Exception as e:
            sys.stdout.write(
                'Unable to complete comparing {} and {}. Stack trace to follow.'.format(self.file1, self.file2))
            sys.stdout.write(str(e))
