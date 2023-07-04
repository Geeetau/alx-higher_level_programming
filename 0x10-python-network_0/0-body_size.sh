#!/bin/bash
#get bytte size fot HTTP response header for a given url
curl -s "$1" | wc -c
