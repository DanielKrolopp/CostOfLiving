#!/usr/bin/env python

__author__ = 'Daniel Krolopp'
__version__ = '1.0'

import sys
import os
from time import sleep
from openpyxl import Workbook

sys.path.insert(0, 'lib/wolfram/Python_Binding_1_1')
import wap

wolfram_key = appid = os.environ['WOLFRAM_KEY']
query_url = 'http://api.wolframalpha.com/v2/query.jsp'

job_name = raw_input("What type of job are you looking for (singular)? ")
job_location_name = raw_input("Where would you like to work? ")

engine = wap.WolframAlphaEngine(wolfram_key, query_url)
query = engine.CreateQuery('Average salary for ' + job_name + ' in ' + job_location_name)
wap.WolframAlphaQuery(query, query_url)
engine_query = engine.PerformQuery(query)
result = wap.WolframAlphaQueryResult(engine_query)

if result.IsSuccess():
	print('Success!')
else:
	print('Failure!')
	exit(1)

for pod in result.Pods():
	waPod = wap.Pod(pod)
	title = waPod.Title()[0]
	print title
	if title == 'Result':
		for subpod in waPod.Subpods():
			waSubpod = wap.Subpod(subpod)
			plaintext = waSubpod.Plaintext()[0]
			img = waSubpod.Img()
			src = wap.scanbranches(img[0], 'src')[0]
			alt = wap.scanbranches(img[0], 'alt')[0]
			print "-------------"
			print "img.src: " + src
			print "img.alt: " + alt
		print "\n"
