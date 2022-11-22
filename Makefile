image-inference-server:
	docker build -f ./docker/inference/Dockerfile --tag inference-server:latest .
container-inference-server:
	docker run -it -p 80:80 inference-server:latest
sak:
	docker stop $(docker ps -a -q)
	docker container rm $(docker ps -a -q)