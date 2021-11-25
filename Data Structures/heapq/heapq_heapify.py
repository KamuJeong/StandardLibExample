import heapq
from heapq_heapdata import data
from heapq_showtree import show_tree


print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)