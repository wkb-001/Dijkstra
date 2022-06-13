# -*- coding : utf-8 -*-
# @Time      : 2022/6/13 21:01
# @Author    : wkb

class Dijkstra:
    def __init__(self):
        self.big_m = 10**6
    def dijkstra(self, graph, startvertex):
        length = len(graph)
        # 初始化path
        path_result = [-1 for _ in range(length)]
        path_result[startvertex] = 0
        # print(path_result)

        # 初始化没有被探索的点到起始点的距离
        not_explore = []
        for i in range(length):
            not_explore.append(graph[startvertex][i])
        not_explore[startvertex] = -1

        # 开始dijkstra
        for i in range(1,length):
            min = self.big_m
            min_index = 0
            for j in range(length):
                if(not_explore[j] > 0 and not_explore[j] < min):
                    min = not_explore[j]
                    min_index = j
            path_result[min_index] = min
            not_explore[min_index] = -1

            for j in range(length):
                if(graph[min_index][j] > 0 and path_result[j] == -1):
                    new_distance = path_result[min_index] + graph[min_index][j]
                    if(new_distance < not_explore[j] or not_explore[j] == -1):
                        not_explore[j] = new_distance
        return path_result


if __name__ == '__main__':
    vertex = ['A', 'B', 'C', 'D']
    #建立邻接矩阵，-1表示不连通
    # graph = [[0, 2, -1, 6],
    #          [2, 0, 3, 2],
    #          [-1, 3, 0, 2],
    #          [6, 2, 2, 0]]
    graph = [[0,1,12,-1,-1,-1],
             [1,0,9,3,-1,-6],
             [12,9,0,4,5,-1],
             [-1,3,4,0,13,15],
             [-1,-1,5,13,0,4],
             [-1,-1,-1,15,5,0]]
    P = Dijkstra()
    result= P.dijkstra(graph,0)
    print(result)
