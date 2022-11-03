from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher, NodeMatch
import neo4jupyter


neo4jupyter.init_notebook_mode()

graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4j_test"))

options = {"Movie": "Happy", "Person": "mike"}

neo4jupyter.draw(graph, options, physics=True, limit=10)


## node and relationship
a = Node("Person", name="Alice")
b = Node("Person", name="Bob")
r = Relationship(a, "KNOWS", b)
graph.create(r)

data = {
    'name': 'Amy',
    'age': 21
}
a.update(data)


a['age'] = 20
b['age'] = 21
r['time'] = '2017/08/31'
print(a, b, r)

a.setdefault('location', '北京')
print(a)


## subgraph


s = a | b | r
print(s)


c = Node('Person', name='Mike')
ab = Relationship(a, "KNOWS", b)
ac = Relationship(a, "KNOWS", c)
w = ab + Relationship(b, "LIKES", c) + ac
print(w)

