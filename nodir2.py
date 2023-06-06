from collections import defaultdict
import time

class Grafff:
    def __init__(self):
        self.graf = defaultdict(list)

    def addEdge(self, u, v):
        self.graf[u].append(v)

    def BFS(self, s):
        visiteddd = [False] * (max(self.graf) + 1)
        qwerty = []

        qwerty.append(s)
        visiteddd[s] = True

        while qwerty:
            s = qwerty.pop(0)
            print(s, end=" ")

            for i in self.graf[s]:
                if visiteddd[i] == False:
                    qwerty.append(i)
                    visiteddd[i] = True

g = Grafff()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("BFS yordamida qidiruv:")
start_time = time.time()
g.BFS(2)
end_time = time.time()
print("n vaqt sarfi:", end_time - start_time, "sekund")
