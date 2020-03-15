"""
A web crawler that finds Professors and their corresponding ratings on
Rate My Professor.

The crawler will search through to find ratings corresponding with the
respective professor.
"""
# The seed/tip url is declared as a constant.
SEED = 'http://info.sjsu.edu/home/schedules.html'

import urllib.request
import json
import course_structures


class RMP_parser:
    def __init__(self):
        self.professors = self.get_professors()

    def get_professors(self):
        """
        Create Professor Objects from data scraped from Rate My Professor

        :return professors:  (list) list of Professor Objects
        """
        professors = []
        # There are 190 pages of professors, 881 is SJSU's ID
        for n in range(1, 191):
            page_url = 'http://www.ratemyprofessors.com/filter/professor/?&page=' + str(n) \
                       + f'&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=' + \
                       str(881)
            prof_info = self.get_info(page_url)

            '''
            print(prof_info[0])
            print(prof_info[0]['tFname'])
            print(prof_info[0]['tMiddlename'])
            print(prof_info[0]['tLname'])
            print(prof_info[0]['overall_rating'])
            print(prof_info[0]['tid'])
            print(prof_info[0]['tDept'])
            '''

            for prof in prof_info:
                if prof['tMiddlename'] is not "":
                    full_name = " ".join((prof['tFname'], prof['tMiddlename'], prof['tLname']))
                else:
                    full_name = " ".join((prof['tFname'], prof['tLname']))
                rating = prof['overall_rating']
                teacher_id = prof['tid']
                dept = prof['tDept']
                professors.append(course_structures.Professor(full_name, rating, teacher_id, dept))

        return professors

    def get_info(self, url):
        """
        Get data about professors from the url

        :param url: url to be parsed
        :return professors:  (list) list of professor data
        """
        try:
            with urllib.request.urlopen(url) as url_file:
                json_page = json.loads(url_file.read().decode())
                professors = json_page['professors']
        except urllib.error.URLError as url_err:
            print(f'Error opening url: {url}\n{url_err}')
        else:
            return professors
