from BSTree import BS_tree
from directedgraph import DirectedGraph
from scc import SCC
from apsp_floyd_warshall import FLOYD_WARSHALL,AnalysisFloydWarshall
from bfs import BFS,showBfsPath,showBfsPathLength
import random
import queue
import cProfile
import math
inf = math.inf

def find(lst,key) -> bool:
    node, prev = lst.finds(lst.root, None, key)
    if node == None:
        return False
    return True

def test(): # many level ver.
    peopleNum = 10000
    node_to_who = 10
    affectlevel = 1
    p = 0.1

    G = DirectedGraph()
    for i in range(peopleNum):
        G.addNode(i)
    for i in range(peopleNum):
        app = set()
        while True:
            tmp = random.randint(0,peopleNum-1)
            if tmp != i:
                app.add(tmp)
            if len(app) >= node_to_who:
                break
        for x in app:
            G.addEdge(i,x)
    print(G)
    q = queue.Queue()
    lst = BS_tree()
    startNode = random.randint(0,peopleNum-1)
    q.put(random.randint(0,peopleNum-1))
    lst.insert(startNode)
    first = True
    while True:
        while True:
            startNode = None
            if first:
                startNode = q.get()
                first = False
                break
            if q.qsize()!= 0:
                next = q.get()
                if p >= random.random():
                    if not find(lst,next):
                        lst.insert(next)
                        startNode = next
                        break
            else:
                break
        if startNode == None:
            break
        
        BFS(G,startNode)
        count = 0
        for i in range(peopleNum):
            if G.getNodeValue(i)['color'] == 'black' and G.getNodeValue(i)['d'] <= affectlevel and G.getNodeValue(i)['d'] != 0:
                q.put(i)
    print('people+ {}(1 is origin)'.format(lst.size))

def test2(num,initCovidNum=5): # one level ver. (BST)
    peopleNum = num
    node_to_who = 10
    p = 0.1
    initPeopleLst = set()
    while True:
        if len(initPeopleLst) >= initCovidNum:
            initPeopleLst = list(initPeopleLst)
            break
        initPeopleLst.add(random.randint(0,num-1))
    G = DirectedGraph()
    for i in range(peopleNum):
        G.addNode(i)
    for i in range(peopleNum):
        app = set()
        while True:
            tmp = random.randint(0,peopleNum-1)
            if tmp != i:
                app.add(tmp)
            if len(app) >= node_to_who:
                break
        for x in app:
            G.addEdge(i,x)
    print(G)
    q = queue.Queue()
    for x in initPeopleLst:
        q.put(x)
    lst = BS_tree()
    for x in initPeopleLst:
        lst.insert(x)
    first = True
    affectPeoInit = 0
    while True:
        while True:
            startNode = None
            if first:
                startNode = q.get()
                affectPeoInit += 1
                if affectPeoInit >= initCovidNum:
                    first = False
                break
            if not first and q.qsize()!= 0:
                next = q.get()
                if p >= random.random():
                    if not find(lst,next):
                        lst.insert(next)
                        startNode = next
                        break
            else:
                break
        if startNode == None:
            break
        count = 0
        for i in G.getNodeOutNeighbors(i):
            q.put(i)
    print('people+ {}(1 is origin)'.format(lst.size))

def test3(day,peopleNum,node_to_who,rapidTestLimit,dayToPeople1,people1,people3,people4,people5,q,graphDay): # one level ver. (Hashmap) 
    # initialize
    dayToPeople1[day] = {}
    if day != 0:
        node_to_who = node_to_who if len(people1.keys()) < peopleNum/25 else max(0,int(node_to_who/10))  # 超過4%人確診就開始不太社交
        node_to_who = node_to_who if node_to_who <= ( peopleNum - len(people1.keys()) )  else max(0,int(node_to_who/10))  # 極度恐懼
    else:
        node_to_who = node_to_who if node_to_who <= ( peopleNum - len(people1.keys()) )  else ( peopleNum - len(people1.keys()) )
    p = 0.05
    # graphDay = {}
    # people1 = {}  # 染疫人
    # people2 = {}  # 完全健康人 (目前沒用到)
    # people3 = {}  # 排隊人
    # people4 = {}  # 目前健康人(完全健康人+排隊人)
    # people5 = {}  # 編號 to 完全健康人idx or 目前健康人idx
    # q = queue.Queue()

    # make the graph
    G = DirectedGraph()
    if day == 0:
        for i in range(peopleNum):
            G.addNode(i)
    else:
        for i in people5.keys():
            G.addNode(people5[i])
    graphNodeNum = G.getNodeNumber()
    if node_to_who != 0:
        for node in G.getAllNodes():
            app = {}
            while True:
                if day == 0:
                    tmp = random.randint(0,graphNodeNum-1)
                else:
                    tmp = people5[random.randint(0,graphNodeNum-1)]
                if tmp != node:
                    app[tmp] = True
                if len(app.keys()) >= node_to_who:
                    break
            for x in app.keys():
                G.addEdge(node,x)
    graphDay[day] = G
    print(G)
    startNode = None
    first = False
    if day == 0:
        first = True
        startNode = []
        for x in people1.keys():
            startNode.append(x)
    # infect
    countRapidTest = 0
    while True:
        while True:
            if first:
                first = False
                break
            startNode = None
            if q.qsize() != 0:
                next = q.get()
                timeDelta = people3[next] - day
                people3.pop(next,None)
                countRapidTest += 1
                if p >= random.random():  # prob
                    if people1.get(next) == None:  # 確診
                        people1[next] = day
                        dayToPeople1[day][next] = True
                        people4.pop(next,None)
                        startNode = next
                        break
                if countRapidTest >= rapidTestLimit:
                    break
            else:
                break
        if startNode == None:
            break
        if type(startNode) == list and day == 0:
            for x in startNode:
                for y in G.getNodeOutNeighbors(x):
                    if people1.get(y) == None and people3.get(y) == None:
                        q.put(y)
                        people3[y] = day
        else:
            initDay = max(0,day-13)
            for i in range(initDay,day+1):
                tmpG = graphDay[i]
                for y in tmpG.getNodeOutNeighbors(startNode):
                    if people1.get(y) == None and people3.get(y) == None:
                        q.put(y)
                        people3[y] = day
    dayStr = str(day+1)
    if day%10 == 0:
        dayStr += 'st'
    elif day%10 == 1:
        dayStr += 'nd'
    elif day%10 == 2:
        dayStr += 'rd'
    else:
        dayStr += 'th'
    print('{} Day_report:  Total_People+ {}p  Day_People+ {}p queueSize {}p\n'.format(dayStr,len(people1.keys()),len(dayToPeople1[day].keys()),q.qsize()) )


def hello(peopleNum,node_to_who,initCovidNum,rapidTestLimit):
    day = 0
    dayToPeople1 = {}
    dayToPeople1[day] = {}
    people1 = {}  # 染疫人
    people2 = {}  # 完全健康人
    people3 = {}  # 排隊人
    people4 = {}  # 目前健康人(完全健康人+排隊人)
    people5 = {}  # 建立graph用
    graphDay = {}
    rapidTestLimit = 1000 if rapidTestLimit < 1000 else rapidTestLimit
    rapidTestLimit = int(peopleNum*0.02)*150 if rapidTestLimit > int(peopleNum*0.02)*150 else rapidTestLimit
    q = queue.Queue()
    for i in range(peopleNum):
        people2[i] = day
        people4[i] = day
    while True:
        who = random.randint(0,peopleNum-1)
        if people1.get(who) == None:
            dayToPeople1[day][who] = True
            people1[who] = day
            people2.pop(who,None)
            people4.pop(who,None)
        if len(people1.keys()) >= initCovidNum:
            break
    x,_ = zip(*people4.items())
    for i in range(peopleNum-initCovidNum):
        people5[i] = x
    rapidTestLimitTmp = rapidTestLimit
    while True:
        test3(day,peopleNum,node_to_who,rapidTestLimit,dayToPeople1,people1,people3,people4,people5,q,graphDay)
        if q.qsize() <= 0:
            break
        day += 1
        x,_ = zip(*people4.items())
        if q.qsize() > peopleNum/20:
            rapidTestLimit = int(len(people4.keys())*0.02)*150
        else:
            rapidTestLimit = rapidTestLimitTmp
        for i in range(len(x)):
            people5[i] = x[i]
        deleteGraphDayTmp = max(-1,day-14)
        if deleteGraphDayTmp != -1:
            graphDay.pop(deleteGraphDayTmp,None)



def test4():
    print(1/10)
    print(int(1/10))

if __name__ == '__main__':
    # cProfile.run('test4()')
    cProfile.run('hello(100000,10,400,3000)')
    #cProfile.run('test3(100,1)')
    # cProfile.run('test3(1000,3)')
    # cProfile.run('test3(10000,10)')
    # cProfile.run('test3(100000,100)')
    # cProfile.run('test3(1000000,3000)')