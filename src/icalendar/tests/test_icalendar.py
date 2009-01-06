try:
    from doctest import DocFileSuite # This fails in 2.3
    import doctest
except ImportError:
    # Python 2.3
    import doctest23 as doctest

import unittest, os
from icalendar import cal, caselessdict, parser, prop

def test_suite():
    suite = unittest.TestSuite()

    suite.addTest(doctest.DocTestSuite(caselessdict))
    suite.addTest(doctest.DocTestSuite(parser))
    suite.addTest(doctest.DocTestSuite(prop))
    suite.addTest(doctest.DocTestSuite(cal))
    doc_dir = '../../../doc'
    for docfile in ['example.txt', 'groupscheduled.txt',
                    'small.txt', 'multiple.txt', 'recurrence.txt']:
        suite.addTest(doctest.DocFileSuite(os.path.join(doc_dir, docfile),
                                           optionflags=doctest.ELLIPSIS),)
        return suite

if __name__ == "__main__":
    suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)