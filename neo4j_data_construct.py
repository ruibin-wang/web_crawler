from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
from neo4j import GraphDatabase

graphpd = GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j", "neo4j"))

session = graphpd.session()
q1 = "MATH (n) return n LIMIT 10"
nodes = session.run(q1)

for node in nodes:
    print(node)
