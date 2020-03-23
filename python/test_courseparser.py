from unittest import TestCase
import courseparser
import rmpparser


class Test_get_links(TestCase):

    def setUp(self):
        self.base_link = "http://info.sjsu.edu/cgi-bin/search.info?target=pub&sarea=schedules&sletter=Z"
        self.table_index = 2

    def test_(self):
        self.assertEqual(len(courseparser.get_links(self.base_link, self.table_index)), 6)


class Test_extract_info(TestCase):

    def setUp(self):
        self.url_correct = "http://info.sjsu.edu/web-dbgen/schedules-spring/c4746772.html"
        self.url_incorrect = "http://info.sjsu.edu/static/artic/assoc-degree-transfer.html"

    def test_correct_url(self):
        self.assertEqual(courseparser.extract_info(self.url_correct),
                         "ZOOL 113\nScheduleSpring 2020\nTitleComp Taxonomy\nGE Designator\nFootnotes06,13,"
                         "75\nSection01\nCode29496\nUnits3\nTypeLEC\nModeIn Person\nEnrollment3/40 spaces "
                         "filled\n\nDaysTR\nTime0830 0920\nDates01/23/20 05/11/20\nLocationDH 344\nInstructorB "
                         "Dawson\n")

    def test_incorrect_url(self):
        self.assertEqual(courseparser.extract_info(self.url_incorrect), None)


class Test_rmpparser(TestCase):

    def setUp(self):
        self.parser = rmpparser.RMP_parser()

    def test_get_info(self):
        self.assertEqual(self.parser.professors[0].name, "Debbie Abbott")
