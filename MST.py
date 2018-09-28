#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:16:28 2018

@author: abdallah
"""
from heapq import heappush as push, heappop as pop
from math import inf

def MST(graph):
    cost = 0
    sub_graph = {list(graph.keys())[0] : graph[list(graph.keys())[0]]}
    added = { list(graph.keys())[0] }
    heap = []
    counter = {}
    for vertex in graph.keys():
        push( heap, (inf , vertex) )
        counter[vertex] = inf
    while (len(sub_graph) != len(graph)):
        for edges in sub_graph.values():
            for edge in edges:
                if  edge[0] not in added:
                    heap.remove( (counter[edge[0]] , edge[0] ) )
                    new_val = min(edge[1] , counter[edge[0]] )
                    push(heap, (new_val , edge[0]))
                    counter[edge[0]] = new_val
        vertex = pop(heap)
        cost += vertex[0]
        try:
            sub_graph[vertex[1]] = graph[vertex[1]]
        except KeyError:
            pass
        added.add(vertex[1])
        
    return cost       
                    








graph = {}
with open('edges.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(int,line[:-1].split(" ")))
        first_ver = elements[0]
        second_ver = elements[1]
        weight = elements[2]
        try:
            (graph[first_ver]).append([second_ver , weight])
        except KeyError:
            graph[first_ver] = [[second_ver , weight]]
        try:
            (graph[second_ver]).append([first_ver , weight])
        except KeyError:
            graph[second_ver] = [[first_ver , weight]]    
            

print(MST(graph) )