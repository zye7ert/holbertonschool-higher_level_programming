#!/bin/bash
# Write a Bash script takes in a URL and displays all HTTP method
sudo curl -i -s $1 | grep "Allow" | cut -d ':' -f2
