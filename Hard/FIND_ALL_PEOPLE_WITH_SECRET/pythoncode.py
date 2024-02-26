class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))
        graph = UnionFind(n)
        graph.unite(firstPerson, 0)
        for t in same_time_meetings:
            for x, y in same_time_meetings[t]:
                graph.unite(x, y)
            for x, y in same_time_meetings[t]:
                if not graph.connected(x, 0):
                    graph.reset(x)
                    graph.reset(y)
        return [i for i in range(n) if graph.connected(i, 0)]
class UnionFind:
    def __init__(self, nodes: int):
        self.parent = [i for i in range(nodes)]
        self.rank = [0] * nodes
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def unite(self, x: int, y: int) -> None:
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    def reset(self, x: int) -> None:
        self.parent[x] = x
        self.rank[x] = 0