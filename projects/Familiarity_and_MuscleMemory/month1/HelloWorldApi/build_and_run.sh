#!/bin/bash

image="hello-world"
container="hello-container"

# build the image
docker build -t $image .

# Run the container
docker run -d -p 8000:8000 --name $container $image

echo "All set now"
