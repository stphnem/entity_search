import ast
import re

def import_entities():
	''' Read the supplied JSON file into a dictionary
	'''

	entities = []
	with open('entities.json') as data_file:
		content = data_file.readlines()
		for line in content:
			entities.append(ast.literal_eval(line))
	return entities

def highlight_links(text, entities):
	''' Parse the input text for entities in entity list
	'''
	edited_text = text.decode('utf-8')
	for entry in entities:
		edited_text = re.sub('(\\b'+entry['title'].decode('utf-8')+'\\b)(?!([^<]+)?>)', 
				      add_anchor(entry),	
				      edited_text, 
				      flags=re.IGNORECASE)

	print 'done'
	return edited_text

def add_anchor(entry):
	new_string = '''<a href="{}" 
					   data-img="{}"
					   rel="popover">{}
					   </a>'''.format(entry['url'].decode('utf-8').encode('ascii', 'ignore'),
								   	  entry['image'].decode('utf-8').encode('ascii', 'ignore'),
									  entry['title'].decode('utf-8').encode('ascii', 'ignore'))
	return new_string

	