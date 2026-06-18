Let's start the db:

```
docker run -d --name ai-db \
-e POSTGRES_PASSWORD=password \
-e POSTGRES_DB=ai-db \
-p 5455:5432 \
pgvector/pgvector:pg18
```

Run SQL

```
docker exec -i ai-db psql -U postgres -d ai-db < ai/schema.sql
```
