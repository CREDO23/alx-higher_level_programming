#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
curl -so "$1" | wc -c