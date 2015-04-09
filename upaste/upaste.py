from os import path
import xattr

from random import getrandbits
from hashlib import sha256
from base64 import b64encode

import pygments
import pygments.lexers
import pygments.formatters

import config
from flask import Flask, abort, redirect, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/repaste/<id>', endpoint='repaste')
def index(id=None):
	if id:
		id = sanitize_id(id)
		if not id_taken(id):
			abort(404)
		contents, language, _ = get_file(id)
	else:
		language = contents = None

	languages = sorted(config.LANGUAGES.items(), key=normalize_language_description)
	top_languages = [(language, config.LANGUAGES[language]) for language in config.TOP_LANGUAGES]
	password = request.cookies.get('password', '')
	return render_template('home.html', languages=languages, top_languages=top_languages, password=password, original=id, original_language=language, contents=contents)

@app.route('/', methods=['POST'])
def paste():
	if request.form['pw'] != config.PASSWORD:
		abort(403)
	if request.form['type'] not in config.LANGUAGES:
		abort(400)

	id = generate_free_id()
	if 'original' in request.form:
		original = sanitize_id(request.form['original'])
	else:
		original = None

	paste_file(id, request.form['txt'], request.form['type'], original)
	return redirect(url_for('show_paste', id=id))

@app.route('/<id>')
def show_paste(id):
	id = sanitize_id(id)
	raw_file = raw_from_id(id)
	if not id_taken(id):
		abort(404)

	source, language, original_id = get_file(id)
	full_language = config.LANGUAGES.get(language, 'Unknown')

	try:
		lexer = pygments.lexers.get_lexer_by_name(language, **config.LEXER_OPTIONS)
	except:
		lexer = pygments.lexers.get_lexer_by_name(config.DEFAULT_LANGUAGE, **config.LEXER_OPTIONS)
	formatter = pygments.formatters.HtmlFormatter(**config.FORMATTER_OPTIONS)
	stylesheet = formatter.get_style_defs('.highlight')
	highlighted = pygments.highlight(source, lexer, formatter)
	return render_template('paste.html', id=id, language=language, full_language=full_language, stylesheet=stylesheet, code=highlighted, raw=raw_file, original=original_id)



def normalize_language_description(x):
	key, val = x
	return val.lstrip('. /#').lower()

def sanitize_id(id):
	return path.basename(id)

def id_taken(id):
	return path.exists(file_from_id(id))

def generate_free_id():
	while True:
		rand = getrandbits(config.ID_RAND_BITS)
		randbytes = rand.to_bytes(int(config.ID_RAND_BITS / 8), 'little')
		hash = sha256(randbytes).hexdigest().encode('utf-8')

		id = b64encode(hash)[:config.ID_LENGTH].decode('ascii')
		if not id_taken(id):
			break

	return id

def file_from_id(id):
	if id == 'self':
		return __file__
	return path.join(config.DATADIR, id + '.txt')

def raw_from_id(id):
	return path.join(config.EXTDATADIR, id + '.txt')



def get_file(id):
	source_file = file_from_id(id)

	with open(source_file, 'r') as f:
		source = f.read()

	try:
		language = xattr.getxattr(source_file, 'user.upaste.language').decode('utf-8')
	except:
		language = config.DEFAULT_LANGUAGE
	try:
		original_id = xattr.getxattr(source_file, 'user.upaste.original_id').decode('utf-8')
	except:
		original_id = None

	return source, language, original_id

def paste_file(id, contents, language=None, original_id=None):
	target_file = file_from_id(id)
	with open(target_file, 'w') as f:
		f.write(contents)

	xattr.setxattr(target_file, 'user.upaste.language', language.encode('utf-8'))
	if original_id:
		xattr.setxattr(target_file, 'user.upaste.original_id', original_id.encode('utf-8'))
