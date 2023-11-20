#!/bin/bash

################
# Stage 1 logic
################

echo "Executing Stage 1: Setting up environment..."

################
# FRONTEND
# compose dev container
echo "Starting Stage 1.1-frontend: Composing frontend dev container..."
docker-compose -f frontend/docker/docker-compose-dev.yaml up --build -d

# Check the exit code of the last command
if [ $? -eq 0 ]; then
    echo "Stage 1.1-frontend: Docker-compose command succeeded."
else
    echo "Stage 1.1-frontend: Docker-compose command failed."
    echo "Stopping the script..."
    exit 1
fi
# FRONTEND
################

echo "Finished all sub-stages from Stage 1. Waiting 10s for environments to startup fully..."

################
# Stage 1 logic completed
# wait for a few seconds to ensure all containers are up and running
sleep 10
################

################
echo "All stages executed successfully"