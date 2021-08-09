##### DOCKER

image:
	docker build -t ml_server .

container:
	docker run -d --name ml_server_container -p 8000:80 ml_server

docker: image container

clean:
	docker rm --force ml_server

######### CLIENT

send:
	python send_data.py

######### DATA MODEL

data_model:
	datamodel-codegen --input sample_data.json --input-file-type json --output ./app/data_model.py


######### LOCAL SERVER

server:
	uvicorn app.main:app