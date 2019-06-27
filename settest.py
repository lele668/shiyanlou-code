#!/usr/bin/env python3
import sys

result = sys.argv[1:]
result = list(set(result))
for i in result:
	print(i)
