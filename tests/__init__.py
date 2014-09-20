import doctest

def test_suite():
    import pytrapal
    import pytrapal.selectors
    suite = doctest.DocTestSuite(pytrapal)
    suite.addTests(doctest.DocTestSuite(pytrapal.selectors))
    return suite
