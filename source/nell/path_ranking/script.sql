-- limpa a base de dados
MATCH (n)
DETACH DELETE n

-- carrega tabela de relacoes
LOAD CSV WITH HEADERS FROM "file:///relations.csv" AS row
MERGE (domain:Entity {category: row.domain})
MERGE (range:Entity {category: row.range})
WITH domain, range, row
CALL apoc.create.relationship(domain, row.relation, {}, range) YIELD rel
RETURN rel

-- mostra o grafo das relacoes entre as entidades
MATCH (n)
RETURN (n)

-- mostra a caminhada feita pelo pagerank pelo grafo
MATCH (person:Entity)
CALL algo.randomWalk.stream(id(person), 10, 1, {path: true})
YIELD path
RETURN path

-- mostra o valor da categoria e o seu pagerank
MATCH (p:Entity)
CALL algo.pageRank.stream(null, null, {direction: "BOTH", sourceNodes: [p], dampingFactor:0.90})
YIELD nodeId, score
MATCH (n) WHERE id(n) = nodeId AND n <> p
RETURN coalesce(n.category) AS node, 
       sum(score)
ORDER BY sum(score) DESC