from os import path

## General.

PASSWORD = 'replaceme'
BASEDIR = path.dirname(__file__)
DATADIR = path.join(BASEDIR, 'plain')
EXTDATADIR = '/'


## Highlighting.

LEXER_OPTIONS = { 'tabsize': 4 }
FORMATTER_OPTIONS = { 'linenos': 'table', 'lineanchors': 'l', 'anchorlinenos': True, 'style': 'github' }


## ID configuration.

ID_RAND_BITS = 32
ID_LENGTH = 10


## Opiniated language lists.

DEFAULT_LANGUAGE = 'text'
LANGUAGES = {
	'ada': 'Ada',
	'actionscript3': 'Actionscript',
	'awk': 'awk',
	'bash': 'bash',
	'bat': 'Batch file',
	'brainfuck': 'Brainfuck',
	'c': 'C',
	'cpp': 'C++',
	'csharp': 'C#',
	'clojure': 'Clojure',
	'cmake': 'CMake',
	'common-lisp': 'Common Lisp',
	'css': 'CSS',
	'cython': 'Cython',
	'd': 'D',
	'dart': 'Dart',
	'diff': 'diff',
	'elixir': 'Elixir',
	'erlang': 'Erlang',
	'fsharp': 'F#',
	'fortran': 'Fortran',
	'glsl': 'GLSL',
	'go': 'Go',
	'haskell': 'Haskell',
	'html': 'HTML',
	'ini': '.ini file',
	'irc': 'IRC log',
	'java': 'Java',
	'js': 'Javascript',
	'json': 'JSON',
	'kconfig': 'Kconfig',
	'lua': 'Lua',
	'make': 'Makefile',
	'matlab': 'MATLAB',
	'nasm': 'NASM x86 assembly',
	'nginx': 'nginx configuration',
	'nsis': 'NSIS',
	'objective-c': 'Objective-C',
	'objective-c++': 'Objective-C++',
	'ocaml': 'OCaml',
	'perl': 'Perl',
	'php': 'PHP',
	'text': 'plaintext',
	'powershell': 'PowerShell',
	'prolog': 'Prolog',
	'python': 'Python 2',
	'python3': 'Python 3',
	'racket': 'Racket',
	'rb': 'Ruby',
	'rst': 'reStructuredText',
	'rust': 'Rust',
	'scala': 'Scala',
	'scheme': 'Scheme',
	'smalltalk': 'Smalltalk',
	'sml': 'Standard ML',
	'sql': 'SQL',
	'tcl': 'Tcl',
	'tex': 'TeX',
	'vala': 'Vala',
	'vb.net': 'Visual Basic .NET',
	'verilog': 'Verilog',
	'vhdl': 'VHDL',
	'xml': 'XML',
	'yaml': 'YAML'
}

TOP_LANGUAGES = [
	'text',
	'bash',
	'c',
	'cpp',
	'html',
	'java',
	'js',
	'lua',
	'perl',
	'php',
	'python',
	'python3',
	'rb',
	'rust',
	'xml'
]
