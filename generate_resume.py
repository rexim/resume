#!/usr/bin/env python

import codecs
import locale
import sys
import json
from jinja2 import Environment, PackageLoader, Template

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

env = Environment(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='<<',
    variable_end_string='>>',
    comment_start_string='<#',
    comment_end_string='#>',
    loader = PackageLoader(__name__, '')
)

def match_tags(tags, filter_tags):
    return [t for t in filter_tags if t in tags] == filter_tags

def filter_entries_by_tags(entries, tags):
    return [entry for entry in entries if not entry.has_key('tags') or match_tags(entry['tags'], tags)]

def filter_sections_by_tags(sections, tags):
    for section in sections:
        section['entries'] = filter_entries_by_tags(section['entries'], tags)

def filter_resume_by_tags(resume, tags):
    filter_sections_by_tags(resume['sections'], tags)

if __name__ == "__main__":
    with open('resume.json') as resume_json_file:
        resume = json.load(resume_json_file)
        filter_resume_by_tags(resume, sys.argv[1:])
        resume_template = env.get_template('resume.jinja2')
        print resume_template.render(resume=resume)
