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

def is_filtered(node, tags):
    return type(node) is dict and node.has_key('tags') and not match_tags(node['tags'], tags)

def filter_by_tags(node, tags):
    if type(node) is dict:
        return dict((k, filter_by_tags(v, tags)) for k, v in node.iteritems() if not is_filtered(v, tags))
    elif type(node) is list:
        return [filter_by_tags(v, tags) for v in node if not is_filtered(v, tags)]
    else:
        return node

if __name__ == "__main__":
    with open('resume.json') as resume_json_file:
        resume = filter_by_tags(json.load(resume_json_file), sys.argv[1:])
        resume_template = env.get_template('resume.jinja2')
        print resume_template.render(resume=resume)
