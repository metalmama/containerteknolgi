docker compose up

Add Person
curl -d '{"name": "Sofie", "age": '40' }' -H 'content-type: application/json' http://127.0.0.1:5000/persons

View Persons
curl http://127.0.0.1:5000/persons
