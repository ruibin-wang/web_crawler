from neo4j import GraphDatabase
import random as rand


## connect to the graph
graphpd = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "neo4j_test"))
session = graphpd.session()

## clear the data for each run
session.run("match (n) detach delete n")


## define the entities and nodes
attibute_names = ['jenney', 'mike', 'Tony', 'Ice', 'Monica', 'Ross', 'Fibee', 'chanderler', 'roe']
favorate_colors = ['red', 'blue', 'green', 'purple', 'orange']
relationships = ['study_at']
schools = ['BU', 'southampton']


## an example of the neo4j command
q = ["create (n:Person{name: 'honey', favoratecolor:'red'})", "create (n:Person{name: 'lili', favoratecolor:'blue'})"]




## create different entities in the graph
q1_set = []
for index in attibute_names:
    temp_q1 = "create (n:Person{name:"+ "\'" + index + "\'" + ", favoratecolor: "+ "\'" + str(favorate_colors[rand.randint(0,len(favorate_colors)-1)]) + "\'" + "})"
    session.run(temp_q1)
    q1_set.append(temp_q1)


q2_set = []
for school in schools:
    q2 = "create (n:School{name:" + "\'" + school + "\'" +"})"
    session.run(q2)
    q2_set.append(q2)

output = session.run("MATCH (n) return n LIMIT 5")
print(output)




## conditional match
cmds1 = "match (s:School), (p:Person) where s.name ='BU' and p.name='jenney' return s,p"
out1 = session.run(cmds1)
print(out1)


## relationship
# cmds2 = "match (s:School), (p:Person) where s.name ='BU' and p.name='jenney' create (p)-[stu:studied_at]->(s)"
# out2 = session.run(cmds2)
# print(out2)

cmds3_set = []
for index in attibute_names:
    temp_cmd = "match (s:School), (p:Person) where p.name = " + "\'" + index + "\'" + " and s.name=" + "\'" + str(schools[rand.randint(0,len(schools)-1)]) + "\'" + " create (p)-[stu:studied_at]->(s)"
    session.run(temp_cmd)
    cmds3_set.append(temp_cmd)

print(cmds3_set)

cmds4 = "match (p1:Person), (p2:Person) where p1.name ='jenney' and p2.name='mike' create (p1)-[soc:friend]->(p2)"
session.run(cmds4)

cmds5 = "match (p1:Person), (p2:Person) where p1.name ='jenney' and p2.name='mike' create (p2)-[soc:friend]->(p1)"
session.run(cmds5)



