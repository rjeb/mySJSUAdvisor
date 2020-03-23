"""
A web crawler that finds courses avalaiable at SJSU for a given semester

The user enters a SJSU semester to which the crawler will search through
to create data objects for all classes
"""
# The seed/tip url is declared as a constant.
SEED = 'http://info.sjsu.edu/home/schedules.html'

import urllib.request
import bs4
import course_structures
import re
import pandas as pd
import rmpparser
from pandas import DataFrame
import pathlib

def get_links(base_url, table_index):
    """
    Get all the course links
    :param base_url:
    :param table_index:
    :param top_url:  (string) base url(seed) that used
    :return all_links:  (list) all the links
    """

    # href="/web-dbgen/schedules-spring/all-departments.html"
    # href="/web-dbgen/schedules-fall/all-departments.html"

    # Extract list of relevant (absolute) links referenced in top_url
    soup = make_soup(base_url)
    table = soup.find_all('table')

    while len(table) <= table_index:
        table_index -= 1

    table = table[table_index]

    all_links = [urllib.parse.urljoin(base_url, anchor.get('href', None))
                 for anchor in table.find_all('a')]
    return all_links


def extract_info(url):
    """
    Get the correct school and course
    from course-course equivalency table.
    :param url:  (string) the url responding to the college
    :param course_regex: (string) the regex of the course
    :return school_name: course_info: (string) the matched course based
    on the url and course
    """

    # edgecase url = search table
    if not bool(re.match("http://info.sjsu.edu/web-dbgen/schedules", url)):
        return None

    else:
        soup = make_soup(url)
        header = soup.find_all('h3')[0].get_text()
        table = soup.find_all('table')[2].get_text()

        #print("table:" + soup.find_all('h3')[0].get_text())
        #print(table + header)

        return header + table


def report(info, course_name):
    """
     Write all requested information to a file
     :param info:  (list) all the information we harvest
     :param course_name: (string) the name of course
    """
    file = '.'.join([course_name, 'txt'])
    with open(file, 'w', encoding='utf-8') as output_file:
        output_file.write(info)

    print(f'Your output has been saved in the file: {file}')


def make_soup(url):
    """
    Get all the course links
    :param url:  (string) url that used
    :return soup:  a BeautifulSoup object
    """

    try:
        with urllib.request.urlopen(url) as url_file:
            bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    else:
        return bs4.BeautifulSoup(bytes, 'html.parser')


def report(course_links):
    """
     Write all requested information to a file
     :param info:  (list) all the information we harvest
     :param course_name: (string) the name of course
    """
    file = '.'.join(["courses", 'txt'])
    with open(file, 'w', encoding='utf-8') as output_file:
        for dept in course_links:
            for course in dept:
                output_file.write(extract_info(course))

def writeToDeptFile(isSpring = True):
    """
    :param isSpring: True if in Spring, False if in Fall
    :return: written csv files for each department
    """

    fall = 'http://info.sjsu.edu/web-dbgen/schedules-fall/all-departments.html'
    spring = 'http://info.sjsu.edu/web-dbgen/schedules-spring/all-departments.html'

    if isSpring:
        dept_links = get_links(fall, 2)
    elif not isSpring:
        dept_links = get_links(spring, 2)

    # Go through each department link and returns a list of links for each course from the respective department
    course_links = [get_links(link, 2) for link in dept_links]

    # Get course info
    courses = set()
    indexStop = 0;
    for dept_list in course_links:
        for link in dept_list:
            # print(extract_info(link))
            tmp_coursestring = extract_info(link)
            if tmp_coursestring is not None:
                """ iterate through the raw parsed data
                course_strings = tmp_coursestring.splitlines()
                index1 = 0
                for index in range(len(course_strings)):
                    print(index1.__str__() + ": " + course_strings[index1])
                    index1 +=1;
                """
                tmp_course = course_structures.Course(tmp_coursestring)
                courses.add(tmp_course)

    # print(courses)

    courseAttr = {'Dept': [], 'ClassNum': [], 'SectionNum': [], 'Units': [], 'StartTime': [], 'EndTime': [], 'Days': [],
                  'SeatsTaken': [], 'SeatsTotal': [], 'Professor': [], 'ClassCode': [], 'ClassMode': [], 'Desc': []}

    for courseIndex in courses:
        # courseIndex.to_string()
        courseAttr['Dept'].insert(0, courseIndex.department_name)
        courseAttr['ClassNum'].insert(0, courseIndex.class_num)
        courseAttr['SectionNum'].insert(0, courseIndex.section_num)
        courseAttr['Units'].insert(0, courseIndex.units)
        courseAttr['StartTime'].insert(0, courseIndex.start_time)
        courseAttr['EndTime'].insert(0, courseIndex.end_time)
        courseAttr['Days'].insert(0, courseIndex.class_days)
        courseAttr['SeatsTaken'].insert(0, courseIndex.seats_taken)
        courseAttr['SeatsTotal'].insert(0, courseIndex.seats_total)
        courseAttr['Professor'].insert(0, courseIndex.professor_name)
        courseAttr['ClassCode'].insert(0, courseIndex.class_code)
        courseAttr['ClassMode'].insert(0, courseIndex.class_mode)
        courseAttr['Desc'].insert(0, courseIndex.course_desc)
    df = DataFrame(data=courseAttr)
    pathlib.Path
    if isSpring:
        df.to_csv("classesSpring.csv", index=False, header=True)
    else:
        df.to_csv("classesFall.csv", index=False, header=True)

def writeToProfFile():
    # The init already parses everything, no extra calls needed here
    rate_my_pp = rmpparser.RMP_parser()

    profAttr = {'Name': [], 'Rating': [], 'Department': [], 'ProfID': []}

    # rate_my_pp.professors returns a list of Professor Objects of which
    # currently have no to_string method, so get on that Jason.
    for prof in rate_my_pp.professors:
        profAttr['Name'].insert(0, prof.name)
        profAttr['Rating'].insert(0, prof.rating)
        profAttr['Department'].insert(0, prof.dept)
        profAttr['ProfID'].insert(0, prof.profID)
    df = DataFrame(data = profAttr)
    pathlib.Path
    df.to_csv("Professors.csv", index=False, header=True)

def main():

    # Get all the relevant links referenced from the seed SEED (top_url)
    fall = 'http://info.sjsu.edu/web-dbgen/schedules-fall/all-departments.html'
    spring = 'http://info.sjsu.edu/web-dbgen/schedules-spring/all-departments.html'

    # Get the semester to parse from the user and returns a list of
    # departments from that semester
    # semester = input('Which semester would you like to view? ')
    semester = 'spring'
    if semester == 'fall':
        dept_links = get_links(fall, 2)
    elif semester == 'spring':
        dept_links = get_links(spring, 2)
    else:
        print("no")

    # Go through each department link and returns a list of links for each course from the respective department
    course_links = [get_links(link, 2) for link in dept_links]


    #writeToDeptFile(False) #writes all classes to classes.csv
    #writeToProfFile()
    #print(courses)


    """
    # Prompt the user for a course name
    course_name = input("Please enter a course name: ")
    # Build a regex corresponding to the course name specified
    course_regex = build_regex(course_name)
    # Harvest information from all the links
    all_info = harvest(all_links, course_regex)
    # Write the harvested information to the output file
    report(all_info, course_name)
    """


if __name__ == "__main__":
    main()
