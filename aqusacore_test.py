import os, sys, getopt
import json

from corefiles.wellformed import *
from corefiles.analyzer import *
from corefiles.globals import *
from corefiles.stories import *
from argparse import ArgumentParser

def single_line_eval(raw):
	story = Story(id = 1, title = raw.strip())
	story = story.chunk()
	WellFormedAnalyzer.well_formed(story)
	Analyzer.atomic(story)
	MinimalAnalyzer.minimal(story)

	test = None

	if not defects:
		test = {'no_defects': raw}
	for defect in defects:
		if defect.story_title == raw:
			test = defect.return_dict()
		else:
			test = {'no_defects': raw}

	test = json.dumps(test)
	return(test)

print(single_line_eval(sys.argv[1]))
# print(single_line_eval("As a chicken, the system shall be red"))
# print(single_line_eval("As a collection manager or monkey, yes."))
# print("---------------------------------------")
# print(single_line_eval("As a subhuman, I want to restrict who has edit access to individual records in my collection."))
