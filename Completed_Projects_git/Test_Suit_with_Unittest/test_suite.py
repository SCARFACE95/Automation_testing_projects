import unittest

import HtmlTestRunner

from test_js_alerts_practice import TestJsAlertsPractice
from test_key_library_practice import TestKeyLibraryPractice
from test_register_page_practice import TestRegisterPagePractice
from test_wait_for_elem_presence_practice import TestWaitForElemPresencePractice
from test_wait_for_elem_visibility_practice import TestWaitForElemVisibilityPractice


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_for_run = unittest.TestSuite()

        #add tests into test suite
        tests_for_run.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(TestJsAlertsPractice),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestKeyLibraryPractice),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestRegisterPagePractice),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestWaitForElemPresencePractice),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestWaitForElemVisibilityPractice),
            ]
        )


        #Create a runner for running all tcs from ts
        #pip install html-testRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test Suite report",
            report_name="Smoke test result"

            )

        #Dam start la teste
        runner.run(tests_for_run)