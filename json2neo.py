import json
import pandas as pd
from py2neo import Graph,Node
from collections import Iterable

graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4j_test"))

with open("./data/AMBOSS_diseases_data.json") as data:
    json_file = json.load(data)

## save to the csv

# amboss_csv = pd.read_json("./data/AMBOSS_diseases_data.json")
# amboss_csv.head()
# amboss_csv.to_csv("./data/amboss_csv.csv", index=False)


relationship_set = ['belongs_to']


nodes_set = []


items = json_file[0]






def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x


def loop_find_dict(input_list):
    if len(input_list)>1:
        for index in input_list:
            pass



for x in flatten(items):
    print(x)

# for jsonitem in json_file:
#     node_list = list(jsonitem.keys())
#     for indexI in node_list:
#         if len(jsonitem[indexI])>1:
#             for subitem in
#
#         else:
#             a = Node(indexI, name=jsonitem[indexI])
#         # graph.create(a)



# for indexI in nodes_set:
#     for indexJ in indexI:
#         a = Node(indexJ, )
#
#
#
#
# a = Node("Person", name="Alice")




print('test')


