#!/bin/sh
nohup sh -c "PORT=8080 node submit.js" &
PORT=8081 node visit.js