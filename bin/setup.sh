#!/bin/bash

echo "🔨 Building the Docker image..."

docker build -t auth-service:latest .

docker run -d -p 5000:5000 -e FLASK_ENV=testing auth-service

echo "🚀 The auth-service Flask app is now running."
echo "🌐 You can access it by opening a web browser and entering:"
echo "   🌍 http://localhost:8080"
echo "   or"
echo "   🌐 http://YOUR_SERVER_IP:8080 (if accessing remotely)"