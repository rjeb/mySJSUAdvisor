import course_structures
import numpy as np
import pandas as pd
from itertools import combinations, product
import json
import re
import matplotlib.pyplot as plt
import six

def getSections(df, dept, classNum):
    """
    :return dataframe with classes matching the specified dept + classNum
    """
    dept_df = df[df['Dept'] == dept]
    rslt_df = dept_df[dept_df['ClassNum'] == classNum]
    return rslt_df

def genSchedules(df, pathIn):
    """
    :param pathIn: a path to dept and classNum arguments
    :return: collection of all iterations schedules matching given parameters
    """
    classTargs = getClassTargets(pathIn) #convert path to a list of tuples (Dept, classNum) which we should generate schedules with
    sectionsList = []
    sectionsIndecies = []
    sectionsIndex = 0
    for classTarg in classTargs: #populate relevant lists
        x, y = classTarg
        sectionsList.append(getSections(df, x, y))

    startDF, *remainingDf = sectionsList # seperate first dataframe from rest
    sectionsIndex += len(startDF.index)
    sectionsIndecies.append(sectionsIndex)

    for secDF in remainingDf: #merge all the classes sections that match the arguments into startDF, in the end, it will contain all sections we will gen schedules from
        startDF = pd.merge(startDF, secDF, how='outer')
        sectionsIndex += len(secDF.index)
        sectionsIndecies.append(sectionsIndex) #track which indecies a class belongs to (ex. 5 sections of CS 151 holds indecies 4 - 9 in startDF)

    generatorIndex = 0
    generatorList = []


    for index in sectionsIndecies:
        generatorList.append([*range(generatorIndex, index)])
        generatorIndex = index

    scheduleIndecies = list(product(*generatorList)) #generate all indecies of possible schedules (ex (1, 4, 8) means make a schedule using the classes at indecies 1, 4, 8 of startDF)

    schedules = []

    for index in scheduleIndecies: #from indecies list, generate dataframes actually holding the data from startDF
        schedules.append(startDF.loc[index, :])
    schedules = [x for x in schedules if noConflicts(x)] #remove conflicts
    return schedules

def parseJson(jsonInput):
    with open(jsonInput) as f:
        data = json.load(f)
    return data

def getClassTargets(jsonPath):
    """
    :param jsonPath: path for arguments for the clients preferred classes (dept, classnum)
    :return:
    """
    classDict = parseJson(jsonPath)
    values = (classDict['className1'], classDict['classNumber1'],
              classDict['className2'], classDict['classNumber2'],
              classDict['className3'], classDict['classNumber3'],
              classDict['className4'], classDict['classNumber4'],
              classDict['className5'], classDict['classNumber5'],
             )
    #values = list(classDict.values())
    values = [x.strip(' ') for x in values if x != '']
    it = iter(values)
    rtn = list(zip(it, it))
    return(rtn)

def noConflicts(scheduleDF): #function for finding whether a schedule has conflicts
    """
    :param scheduleDF: schedule we are checking for conflicts
    :return: boolean confirming whether the schedule is valid
    """
    dayVals = {'M': 0, 'T': 2400, 'W': 4800, 'R': 7200, 'F': 9600}
    times = []
    for index, row in scheduleDF.iterrows():
        if (dayVals.__contains__(row["Days"][0:1]) is True): #check if class is not online
            times.append((int(row["StartTime"]) + dayVals.get(row["Days"][0:1]), int(row["EndTime"]) + dayVals.get(row["Days"][0:1])))
            if (dayVals.__contains__(row["Days"][1:2]) is True): #check if class has multiple days
                times.append((int(row["StartTime"]) + dayVals.get(row["Days"][1:2]), int(row["EndTime"]) + dayVals.get(row["Days"][1:2])))
    checkTimes = combinations(times, 2)
    for checks in checkTimes: #for all combinations of classes (class1, class2), (class1, class3) etc, check for any scheduling overlaps
        (s1, e1), (s2, e2) = checks
        if isConflict(s1, e1, s2, e2): #if one exists, then the whole schedule is invalid
            return False
    return True

def isConflict(startTime1, endTime1, startTime2, endTime2): #check for an individual conflict between two classes
    """
    :return: boolean indicating conflict
    """
    if (startTime1 < startTime2):
        if (endTime1 > startTime2):
            return True
    else:
        if (endTime2 > startTime1):
            return True
    return False

def getCloseness(scheduleDF):
    """
    :param scheduleDF: schedule we want rating for
    :return: normalized score for closeness of given schedule
    """
    dayVals = {'M': 0, 'T': 2400, 'W': 4800, 'R': 7200, 'F': 9600}
    times = []
    rtn = 0.0
    classCount = 0 #tracks how many instances of in-person classes we have
    for index, row in scheduleDF.iterrows():
        if (dayVals.__contains__(row["Days"][0:1]) is True): #check if class is not online
            times.append((int(row["StartTime"]) + dayVals.get(row["Days"][0:1]), int(row["EndTime"]) + dayVals.get(row["Days"][0:1])))
            classCount += 1
            if (dayVals.__contains__(row["Days"][1:2]) is True): #check if class has multiple days
                times.append((int(row["StartTime"]) + dayVals.get(row["Days"][1:2]), int(row["EndTime"]) + dayVals.get(row["Days"][1:2])))
                classCount += 1
    times = sorted(times, key = lambda x: x[0])
    maxindex = len(times) - 1
    for x in range(len(times)):
        if x != maxindex:
            diff = times[maxindex - x][0] - times[maxindex - (x + 1)][1] #difference from start time and end time of 2 conseq classes
            if diff < 1200: #ignoring different days, how close are the classes in the schedule generally?
                rtn += diff
    #diff contains a sumed value for how 'far' classes on the same day are from one another
    rtn = 1.0 - ((rtn / classCount) / 250) #normalize the value
    return rtn


def rankPng(dfList, length, alg = None, path = 'solutions.png', pweight = 1, cweight = 1):
    """
    :param dfList: list containing a # of schedules we want to rank
    :param length: the # of solutions(top via ranking method) we return
    :param alg: how do we want it ranked? (none: no method 1: profscore only, 2: closeness only, 3:weighted ranking by profscore and closeness)
    :param pweight: only necessary for alg 3, how much weight to put into prof rating?
    :param cweight: only necessary for alg 3, how much weight to put into closeness?
    :return: the top <length> schedules ranked by <alg> saved to <path>[index].png
    """
    if len(dfList) < length:
        print("invalid arguments")
        return
    # dfList = list of schedules, len = length of returned 'top' schedules
    if alg is None:
        #no sorting algorithm is applied
        pathComponents = re.split('.png', path, 1)
        for index in range(length):
            render_mpl_table(dfList[index], header_columns=0, col_width=2.0)
            plt.savefig(pathComponents[0] + index.__str__() + ".png")
    elif alg is 1:
        #algorithm uses profscore only
        dfList = sorted(dfList, key = lambda x: -x['Rating'].sum())
        pathComponents = re.split('.png', path, 1)
        for index in range(length):
            render_mpl_table(dfList[index], header_columns=0, col_width=2.0)
            plt.savefig(pathComponents[0] + index.__str__() + ".png")
    elif alg is 2:
        #algorithm uses closeness only
        dfList = sorted(dfList, key = lambda x: -getCloseness(x))
        pathComponents = re.split('.png', path, 1)
        for index in range(length):
            render_mpl_table(dfList[index], header_columns=0, col_width=2.0)
            plt.savefig(pathComponents[0] + index.__str__() + ".png")
    elif alg is 3:
        #algorithm uses normalized profscore and closeness ranking and given weights of attributes
        dfList = sorted(dfList, key = lambda x: -((x['Rating'].sum()/ (len(x.index) * 5)) * pweight + getCloseness(x) * cweight))
        pathComponents = re.split('.png', path, 1)
        for index in range(length):
            del dfList[index]['SeatsTaken']
            del dfList[index]['SeatsTotal']
            del dfList[index]['ClassCode']
            del dfList[index]['ClassMode']
            render_mpl_table(dfList[index], header_columns=0, col_width=2.0)
            plt.savefig(pathComponents[0] + index.__str__() + ".png")

#basic table display used in rankPng obtained via: https://stackoverflow.com/questions/19726663/how-to-save-the-pandas-dataframe-series-data-as-a-figure
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
    semester = course_structures.Semester(True) #working with the Spring semester
    targets = genSchedules(semester.df1, 'classargs.json') #generate all possible iterations of class schedules
    rankPng(targets, 3, alg = 3, pweight = 3, cweight = 1) #rank the schedules based on weighted algorithm, with prof weight 3 and closeness weight 1

if __name__ == "__main__":
    main()
