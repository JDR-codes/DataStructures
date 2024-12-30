'''Directed graph'''
# class Diected_graph:
#     def __init__(self):
#         self.graph={}
#     def add_vertices(self,source,dest):
#         if source not in self.graph:
#             self.graph[source]=[]
#         self.graph[source].append(dest)
#     def Print(self):
#         for vertice in self.graph:
#             print(f'{vertice} --> {self.graph[vertice]}')

#     def Delete_vertice(self,val):
#         if val in self.graph:
#             self.graph.pop(val)
#         for vertice in self.graph:
#             for data in self.graph[vertice]:
#                 if data==val:
#                     self.graph[vertice].remove(data)

# o1=Diected_graph()
# o1.add_vertices(10,20)
# o1.add_vertices(20,30)
# o1.add_vertices(10,30)
# o1.add_vertices(30,10)
# o1.Print()
# o1.Delete_vertice(30)
# o1.Print()

'''Undirected Graph'''

# class Undirected_graph:
#     def __init__(self):
#         self.graph={}
#     def Add_vertice(self,data1,data2):
#         if data1 not in self.graph:
#             self.graph[data1]=[]
#         if data2 not in self.graph:
#             self.graph[data2]=[]
#         self.graph[data1].append(data2)
#         self.graph[data2].append(data1)
#     def Print(self):
#         for vertice in self.graph:
#             print(f'{vertice} --> {self.graph[vertice]}')

#     def Delete_vertice(self,val):
#         if val in self.graph:
#             self.graph.pop(val)
#         for vertice in self.graph:
#             for data in self.graph[vertice]:
#                 if data==val:
#                     self.graph[vertice].remove(data)


# o1=Undirected_graph()
# o1.Add_vertice(1,2)
# # o1.Add_vertice(2,1)
# o1.Add_vertice(1,3)
# # o1.Add_vertice(3,1)
# o1.Print()


'''Weighted graph'''

class Weighted_graph:
    def __init__(self):
        self.graph={}
    def Add_vertice(self,loc1,loc2,dst):
        if loc1 not in self.graph:
            self.graph[loc1]=[]
        if loc2 not in self.graph:
            self.graph[loc2]=[]
        for i in self.graph[loc1]:
            if loc2 in i:
                i[0]=dst
                break
        else:
            self.graph[loc1].append([dst,loc2])
        for i in self.graph[loc2]:
            if loc1 in i:
                i[0]=dst
                break
        else:
            self.graph[loc2].append([dst,loc1])

    def Print(self):
        for vertice in self.graph:
            print(f'{vertice} --> {self.graph[vertice]}')

    def Delete_vertice(self,val):
        if val in self.graph:
            self.graph.pop(val)
        for vertice in self.graph:
            for data in self.graph[vertice]:
                if data==val:
                    self.graph[vertice].remove(data)


o1=Weighted_graph()
o1.Add_vertice('bangalore','erode',200)
o1.Print()
o1.Add_vertice('bangalore','erode',250)
o1.Add_vertice('bangalore','mysore',350)
o1.Print()
o1.Delete_vertice('erode')
o1.Print()


