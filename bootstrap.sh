#!/bin/bash

echo "[BOOTSTRAP.SH] Building the application ..."

docker-compose build --no-cache

echo ""

echo "[BOOTSTRAP.SH] Finished Building"

echo "[BOOTSTRAP.SH] Now starting the applications"

echo ""

docker-compose up -d

until curl -s -f "http://localhost:9000/api/v1"
do
  sleep 1
done

echo ""

echo "[BOOTSTRAP.SH] Please visit http://localhost:5000 now"

echo "[BOOTSTRAP.SH] You can also visit http://localhost:9000/api/v1 to view the api"

echo "[BOOTSTRAP.SH] Visit http://localhost:9000/api/v1/yt-api-key to add a new youtube api key"