from py2neo import Graph, Node, Relationship

# Connect to the Neo4j database
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
username = "neo4j"             #
password = "your_password"     
graph = Graph(uri, auth=(username, password))

# Sample data to send to Neo4j
sample_data = [
    {"name": "Jehangir", "age": 30},
    {"name": "Alisson", "age": 25},
    {"name": "Bobby", "age": 28}
]

# Create nodes in Neo4j
for data in sample_data:
    node = Node("Person", name=data["name"], age=data["age"])
    graph.create(node)

# Create relationships between nodes
john = graph.nodes.match("Person", name="John").first()
alice = graph.nodes.match("Person", name="Alice").first()
bob = graph.nodes.match("Person", name="Bob").first()

relationship1 = Relationship(john, "FRIENDS_WITH", alice)
relationship2 = Relationship(john, "FRIENDS_WITH", bob)
graph.create(relationship1)
graph.create(relationship2)

# Retrieve data from Neo4j and print it
result = graph.run("MATCH (person:Person) RETURN person.name, person.age")
print("People in the database:")
for record in result:
    print(record["person.name"], record["person.age"])
