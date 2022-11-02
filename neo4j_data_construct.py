from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
from neo4j import GraphDatabase
import random as rand

graphpd = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "neo4j_test"))

session = graphpd.session()


# for node in nodes:
#     print(node)

attibute_names = ['jenney', 'mike', 'Tony', 'Ice', 'Monica', 'Ross', 'Fibee', 'chanderler', 'roe']
favorate_colors = ['red', 'blue', 'green', 'purple', 'orange']
relationships = ['study_at']
schools = ['BU', 'southampton']


q = ["create (n:Person{name: 'honey', favoratecolor:'red'})", "create (n:Person{name: 'lili', favoratecolor:'blue'})"]

# for index in q:
#     session.run(index)


cmds = []
for index in attibute_names:
    temp_cmds = "create (n:Person{name:"+ str(index) +", favoratecolor: " + str(favorate_colors[rand.randint(0,len(favorate_colors)-1)]) + "})"
    session.run(temp_cmds)
    cmds.append(temp_cmds)



print(cmds)


# q2 = "MATCH (n) where n.name='dads' return n"
#
# node2 = session.run(q2)
#
# # for node in node2:
# #     print(node)
#
#
# q3 = "create (n:Team{name:'shivam'})"
#
# node3 = session.run(q3)
# q4 = "match (n:Team) return (n)"
#
#
# q1 = "MATCH (n) return n LIMIT 10"
# nodes = session.run(q1)
#
# for node in nodes:
#     print(node)




