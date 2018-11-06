// limpa a base de dados
MATCH (n)
DETACH DELETE (n)

// carrega tabela de relacoes presente na pasta import
LOAD CSV WITH HEADERS FROM "file:///relations.csv" AS row
MERGE (domain:Entity {category: row.domain})
MERGE (range:Entity {category: row.range})
WITH domain, range, row
CALL apoc.create.relationship(domain, row.relation, {}, range) YIELD rel
RETURN rel

// mostra o grafo das relacoes entre as entidades
MATCH (n)
RETURN (n)

// mostra a caminhada (de no maximo 5 relacoes) feita pela caminhada aleatória no grafo
MATCH (entity:Entity)
CALL algo.randomWalk.stream(id(entity), 10, 1)
YIELD nodeIds
UNWIND nodeIds AS nodeId
MATCH ((n)-[r*..5]->(m)) WHERE id(n) = nodeId
WITH n.category AS start_node, extract(rel IN r| type(rel)) AS path, m.category AS end_node
RETURN start_node, path, end_node, COUNT(path) AS frequency
ORDER BY frequency DESC

// mostra a categoria e o seu pagerank
MATCH (p:Entity)
CALL algo.pageRank.stream(null, null, {direction: "BOTH", sourceNodes: [p], dampingFactor:0.90})
YIELD nodeId, score
MATCH (n) WHERE id(n) = nodeId AND n <> p
RETURN coalesce(n.category) AS node, sum(score)
ORDER BY sum(score) DESC