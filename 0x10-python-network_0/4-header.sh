#!/usr/bin/env bash

# Check if a URL was provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# URL provided as the first argument
URL="$1"

# Send a GET request with the header X-School-User-Id: 98
curl -s -H "X-School-User-Id: 98" "$URL"
