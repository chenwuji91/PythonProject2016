#-*- coding: UTF-8 -*-
'''
@author: chenwuji
'''
#将移动序列预处理
rootDir = '/Users/chenwuji/Documents/RoadMatch/zyc/'


import tools
from datetime import datetime
def readData():
    initdate = 20202020
    inittime = 100000
    allDataDict = {}
    f = open(rootDir + 'JiuHuaMidRoadWithHuangShanMidRoad_20160531_1730_1830.txt')
    for eachline in f:
        initdate = initdate + 1
        eachline = eachline.split('\n')[0]
        list = eachline.split('\t')
        dataOneLine = []
        if len(list)>4:
            time1 = tools.timetranslate(list[2])
            time2 = tools.timetranslate(list[3])
            pointList = list[1].split(',')
            timeinterval = (time2-time1)/len(pointList)
            for eachP in pointList:
                thisJizhan = eachP
                inittime = inittime + timeinterval
                tools.makeDir(rootDir + 'resultData/')
                tools.writeToFile(rootDir + 'resultData/' + str(initdate), thisJizhan +','+str(initdate) + str(inittime))
                dataOneLine.append((thisJizhan,str(initdate) + str(inittime)))
            print list
        allDataDict.setdefault(str(initdate),dataOneLine)
    f.close()
    tools.toFileWithPickle(rootDir + 'result', allDataDict)




if __name__ == '__main__':
    readData()