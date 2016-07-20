# Simple Flask API 

This application is here to debug client request to an API.

This API will always return "OK", but will print some request informations in the console:

- path
- HTTP method (verb)
- Header key-value
- Query parameter (?name=Jon)
- Raw body    
- Parser body like a form
- Parser body like a JSON


## Simple to run

```
python api.py
```


## Examples

### GET request with query parameters and custom header

```
curl -X GET 'http://localhost:8989?name=Jon' -H "X-Tag: 89"

New request:
	-path: /
	-verb: GET
	-headers: 
		Content-Length = 
		User-Agent = curl/7.43.0
		X-Tag = 89
		Host = localhost:8989
		Accept = */*
		Content-Type = 
	-query parameters: 
		name = Jon
	-raw body: 
		
	-form body: 
	-json body: 
		None
```

### POST request with query parameters, body key/value and custom header

```
curl -X POST 'http://localhost:8989/users?name=Jon&age=25' -H "X-Tag: 89" -d "password=toto1234" -d "firstname=Snow&sister=Aria"

New request:
	-path: /users
	-verb: POST
	-headers: 
		Content-Length = 44
		User-Agent = curl/7.43.0
		X-Tag = 89
		Host = localhost:8989
		Accept = */*
		Content-Type = application/x-www-form-urlencoded
	-query parameters: 
		age = 25
		name = Jon
	-raw body: 
		
	-form body: 
		sister = Aria
		password = toto1234
		firstname = Snow
	-json body: 
		None
```

### PUT request with json body (custom Content-Type header) and custom header

```
curl -X PUT 'http://localhost:8989/users/Jon' -H "X-Tag: 89" -H "Content-type: application/json" -d '{ "age": 26 }'

New request:
	-path: /users/Jon
	-verb: PUT
	-headers: 
		Content-Length = 13
		User-Agent = curl/7.43.0
		X-Tag = 89
		Host = localhost:8989
		Accept = */*
		Content-Type = application/json
	-query parameters: 
	-raw body: 
		{ "age": 26 }
	-form body: 
	-json body: 
		{u'age': 26}
```

