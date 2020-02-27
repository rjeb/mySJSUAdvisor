"""
A web crawler that finds courses avalaiable at SJSU for a given semester

The user enters a SJSU semester to which the crawler will search through
to create data objects for all classes
"""
# The seed/tip url is declared as a constant.
SEED = 'http://info.sjsu.edu/home/schedules.html'

import urllib.request
import bs4
import re


def get_links(base_url, table_index):
    """
    Get all the course links
    :param base_url:
    :param table_index:
    :param top_url:  (string) base url(seed) that used
    :return all_links:  (list) all the links that link course-course
    equivalency on all other colleges
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
    soup = make_soup(url)
    header = soup.find_all('h3')[0].get_text()
    table = soup.find_all('table')[2].get_text()

    return header + table

    '''school_name = table('h3')[1].get_text()
    all_site = table.find_all('td', string=course_regex)
    for each_site in all_site:
        eqv_column = each_site.find_next_sibling('td').find_next_sibling('td')
        if eqv_column.get_text() != 'No Current Equivalent':
            course_info = ' '.join(eqv_column.get_text(separator=' ').split())
            return f'{school_name}: {course_info}'
            '''


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


def main():
    # Get all the relevant links referenced from the seed SEED (top_url)
    fall = 'http://info.sjsu.edu/web-dbgen/schedules-fall/all-departments.html'
    spring = 'http://info.sjsu.edu/web-dbgen/schedules-spring/all-departments.html'

    # Get the semester to parse from the user and returns a list of
    # departments from that semester
    # semester = input('Which semester would you like to view? ')
    semester = 'fall'
    if semester == 'fall':
        dept_links = get_links(fall, 2)
    elif semester == 'spring':
        dept_links = get_links(spring, 2)
    else:
        print("no")

    # Go through each department link and returns a list of links for each course from the respective department
    course_links = [get_links(link, 2) for link in dept_links]

    # Print course info to a text file
    report(course_links)

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
