import json
import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher


## first open the neo4j project in the browser
graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4j_test"))
graph.run("Match (n) detach delete n")  ## clean the exist graph in the project
node_matcher = NodeMatcher(graph)  ## to find the exist node in the graph to avoid creating duplicate nodes

## load the symptom_disease data
with open("./data/symp_diagnosis_relation_training.json") as data:
    json_file = json.load(data)

## save to the csv
# amboss_csv = pd.read_json("./data/AMBOSS_diseases_data.json")
# amboss_csv.head()
# amboss_csv.to_csv("./data/amboss_csv.csv", index=False)


## define the relation between symptoms and diseases
relationship_set = ['belongs_to']


## define the format of data
whole_pic = {'G40':[], 'R51':[], 'M54':[], 'I63':[]}

## the purpose of this step is to make the json file into a set
for index in json_file:
    temp = index['symptoms'].split('.')
    temp = [indexI[1:] if indexI[0] ==' ' else indexI for indexI in temp]  ## delete the space string in the head of the string
    new_temp = []
    for indexJ in temp:
        if '@' not in indexJ:   ## delete the symptoms with special characters
            new_temp.append(indexJ)

    whole_pic[index['diagnosis']] += new_temp
    
     ## avoid the duplicate items
    temp, new_temp = [], []


## put all symptoms into a list
all_symp_list = []
for index in whole_pic:
    all_symp_list += whole_pic[index]

all_symp_list = list(set(all_symp_list))



## generate the nodes and the graph, and create their relationship
already_created_nodes = []
for indexI in whole_pic:
    disease_node = Node('Disease', name=indexI)
    for indexJ in whole_pic[indexI]:
        if indexJ not in already_created_nodes:
            already_created_nodes.append(indexJ)
            symptoms_node = Node('Symptoms', name=indexJ)
            dis_symp_rela = Relationship(symptoms_node, relationship_set[0], disease_node)
            graph.create(dis_symp_rela)
            already_created_nodes = list(set(already_created_nodes))

        else:
            stored_node = node_matcher.match("Symptoms").where(name=indexJ).first()   ## it is very necessary to add .first() to get the id of nodes
            dis_symp_rela = Relationship(stored_node, relationship_set[0], disease_node)
            graph.create(dis_symp_rela)





