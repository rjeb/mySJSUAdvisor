import courseparser
import course_structures
import numpy as np
import pandas as pd
from itertools import combinations, product
import functools
import matplotlib
import json
import re
import matplotlib.pyplot as plt
from pandas.plotting import table
import six

# binary search and basic scheduler as defined by https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/
# classes are defined in total start time since Monday with Monday 12:00 am being 0 time and Sunday 11:59 pm being the latest time

def binarySearch(job, start_index):
    #
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start_index - 1

    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1
# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(job):
    # Sort jobs according to finish time
    job = sorted(job, key=lambda j: j.finish)

    # Create an array to store solutions of subproblems.  table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]

    table[0] = job[0].profit;

    # Fill entries in table[] using recursive property
    for i in range(1, n):

        # Find profit including the current job
        inclProf = job[i].profit
        l = binarySearch(job, i)
        if (l != -1):
            inclProf += table[l];

            # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])

    return table[n - 1]

def getSections(df, dept, classNum):
    dept_df = df[df['Dept'] == dept]
    rslt_df = dept_df[dept_df['ClassNum'] == classNum]
    return rslt_df

def genSchedules(df, pathIn):
    """
    :param classTargs: list of tuples (Dept, classNum) which we should generate schedules with
    :return: collection of schedules
    """
    classTargs = getClassTargets(pathIn)
    sectionsList = []
    sectionsIndecies = []
    sectionsIndex = 0
    for classTarg in classTargs:
        x, y = classTarg
        sectionsList.append(getSections(df, x, y))

    startDF, *remainingDf = sectionsList # seperate first dataframe from rest
    sectionsIndex += len(startDF.index)
    sectionsIndecies.append(sectionsIndex)

    for secDF in remainingDf:
        startDF = pd.merge(startDF, secDF, how='outer')
        sectionsIndex += len(secDF.index)
        sectionsIndecies.append(sectionsIndex)

    generatorIndex = 0
    generatorList = []


    for index in sectionsIndecies:
        generatorList.append([*range(generatorIndex, index)])
        generatorIndex = index

    scheduleIndecies = list(product(*generatorList))

    schedules = []

    for index in scheduleIndecies:
        schedules.append(startDF.loc[index, :])
        #print(startDF.loc[index, :])
    schedules = [x for x in schedules if noConflicts(x)]
    #print(schedules)
    return schedules


def showSchedules(schedules):
    #todo return a list of schedules as a png
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    colors = ['pink', 'lightgreen', 'lightblue', 'wheat', 'salmon']

def parseJson(jsonInput):
    with open(jsonInput) as f:
        data = json.load(f)
    return data

def getClassTargets(jsonPath):
    classDict = parseJson(jsonPath)
    values = list(classDict.values())
    values = [x for x in values if x != '']
    it = iter(values)
    rtn = list(zip(it, it))
    return(rtn)

def noConflicts(scheduleDF):
    dayVals = {'M': 0, 'T': 2400, 'W': 4800, 'R': 7200, 'F': 9600}
    times = []
    for index, row in scheduleDF.iterrows():
        if (dayVals.__contains__(row["Days"][0:1]) is True): #check if class is not online
            times.append((int(row["StartTime"]) + dayVals.get(row["Days"][0:1]), int(row["EndTime"]) + dayVals.get(row["Days"][0:1])))
            if (dayVals.__contains__(row["Days"][1:2]) is True): #check if class has multiple days
                times.append((int(row["StartTime"]) + dayVals.get(row["Days"][1:2]), int(row["EndTime"]) + dayVals.get(row["Days"][1:2])))
            #print(row["StartTime"], row["EndTime"], dayVals.get(row["Days"][1:2]))
    checkTimes = combinations(times, 2)
    for checks in checkTimes:
        (s1, e1), (s2, e2) = checks
        if isConflict(s1, e1, s2, e2):
            return False
    #print(times)
    return True

def isConflict(startTime1, endTime1, startTime2, endTime2):
    if (startTime1 < startTime2):
        if (endTime1 > startTime2):
            return True
    else:
        if (endTime2 > startTime1):
            return True
    return False

def rank(dfList, len, alg = None, path = 'solutions.json'):
    #dfList = list of schedules, len = length of returned 'top' schedules
    if alg is None:
        pathComponents = re.split('.json', path, 1)
        for index in range(len):
            (dfList[index]).to_json(pathComponents[0] + index.__str__() + ".json", orient = 'split')

def rankPng(dfList, len, alg = None, path = 'solutions.png'):
    # dfList = list of schedules, len = length of returned 'top' schedules
    if alg is None:
        pathComponents = re.split('.png', path, 1)
        for index in range(len):
            render_mpl_table(dfList[index], header_columns=0, col_width=2.0)
            plt.savefig(pathComponents[0] + index.__str__() + ".png")

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(True)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0] % len(row_colors)])
    return ax

def main():
    semester = course_structures.Semester(True)
    targets = genSchedules(semester.df1, 'exampleArgs.json')
    rankPng(targets, 2)
    #noConflicts(targets)

if __name__ == "__main__":
    main()
