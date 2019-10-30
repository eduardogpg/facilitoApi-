curl -i -H "Content-Type: application/json" -X POST -d '{"title": "Demo", "description": "Esta es una simple descripcion", "user_id": "1", "deadline": "2019-12-12 12:00:00"}' http://localhost:5000/api/v1/tasks


curl -i -H "Content-Type: application/json" -X PUT -d '{"title": "Cambio de nombre", "description": "Esta es una simple descripcion"}' http://localhost:5000/api/v1/tasks/1