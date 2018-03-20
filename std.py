from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl
import string

# If you're used to VC alphabet, use the line below instead
#alpha_alt = 'arch brov char dell etch fomp goof hark ice jinks koop lug mowsh nerb ork pooch quash rosh souk teek unks verge womp trex yang zooch'.split()
alpha_alt = 'ace bat seek die each fomp gone harm ice jinks kate ella emma near odd pit quest rick sun teeth urge vest whale box yang sap'.split()
#alpha_alt = 'air bat cap die each fail gone harm sit jinks crash look mad near odd pit quest red sun trap urge vest whale box yang sap'.split()

alnum = list(zip(alpha_alt, string.ascii_lowercase)) + \
    [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
alpha.update({'ship %s' % word: letter for word,
              letter in zip(alpha_alt, string.ascii_uppercase)})

alpha.update({'troll %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'chom %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'command shift %s' % k: Key('ctrl-shift-%s' % v)
              for k, v in alnum})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in alnum})

mapping = {
    'semicolon': ';',
    r'new-line': '\n',
    r'new-paragraph': '\n\n',
}


def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word


def text(m):
    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)


def word(m):
    tmp = [str(s).lower() for s in m.dgnwords[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)

def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word
    return func


def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder': (True, lambda i, word, _: '__%s__' % word if i == 0 else word),
    'cram':  (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    'pathway':  (True, lambda i, word, _: word if i == 0 else '/'+word),
    'dotsway':  (True, lambda i, word, _: word if i == 0 else '.'+word),
    'snake':  (True, lambda i, word, _: word if i == 0 else '_'+word),
    'yellsmash':  (True, lambda i, word, _: word.upper()),
    'yellsnik':  (True, lambda i, word, _: word.upper() if i == 0 else '_'+word.upper()),
    'smash':  (True, lambda i, word, _: word),
    'dollcram': (True, lambda i, word, _: '$'+word if i == 0 else word.capitalize()),
    'champ': (True, lambda i, word, _: word.capitalize() if i == 0 else " "+word),
    'lowcram': (True, lambda i, word, _: '@'+word if i == 0 else word.capitalize()),
    'criff': (True, lambda i, word, _: word.capitalize()),

    'spine':  (True, lambda i, word, _: word if i == 0 else '-'+word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    'yeller': (False, lambda i, word, _: word.upper()),
    'dub-string': (False, surround('"')),
    'string': (False, surround("'")),
    'glitch': (False, surround("`")),
    'padded': (False, surround(" ")),
    'rot thirteen':  (False, rot13),
}


def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    words = [str(s).lower() for s in m.dgndictation[0]._words]

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

def ShrinkWord(m):
    word = str(m.dgndictation[0]._words[0]).lower()
    if not word in shrink_map:
        raise Exception('%s not in shrink map' % word)
    Str(shrink_map[word])(None)

shrink_map = {
    'address': 'addr',
    'addresses': 'addrs',
    'boolean': 'bool',
    'compare': 'cmp',
    'config': 'cfg',
    'context': 'ctx',
    'delete': 'del',
    'error': 'err',
    'format': 'fmt',
    'message': 'msg',
    'package': 'pkg',
    'parameter': 'param',
    'pointer': 'ptr',
    'private': 'priv',
    'response': 'res',
    'user': 'usr',
    'userid': 'uid',
    'username': 'uname',
    'administrator': "admin",
    'administrators': "admins",
    'allocate': "alloc",
    'alternate': "alt",
    'apartment': "apt",
    'application': "app",
    'applications': "apps",
    'architecture': "arch",
    'argument': "arg",
    'arguments': "args",
    'attribute': "attr",
    'attributes': "attrs",
    'authentic': "auth",
    'authenticate': "auth",
    'author': "auth",
    'binary': "bin",
    'button': "btn",
    'calculate': "calc",
    'call': "col",
    'car': "char",
    'care': "char",
    'certificate': "crt",
    'character': "char",
    'column': "col",
    'command': "cmd",
    'concatenate': "concat",
    'configuration': "config",
    'configure': "config",
    'constant': "const",
    'define': "def",
    'descending': "desc",
    'develop': "dev",
    'developer': "dev",
    'development': "dev",
    'directory': "dir",
    'divider': "div",
    'document': "doc",
    'environment': "env",
    'execute': "exec",
    'extend': "ext",
    'extension': "ext",
    'favorite': "fav",
    'function': "func",
    'image': "img",
    'imager': "int",
    'incorporate': "inc",
    'increment': "inc",
    'initialize': "init",
    'integer': "int",
    'iterate': "iter",
    'jason': "json",
    'language': "lang",
    'large': "lg",
    'latitude': "lat",
    'length': "len",
    'library': "lib",
    'locate': "loc",
    'location': "loc",
    'longitude': "lng",
    'medium': "md",
    'minimum': "min",
    'miscellaneous': "misc",
    'navigate': "nav",
    'navigation': "nav",
    'number': "num",
    'object': "obj",
    'parameter': "param",
    'parameters': "params",
    'position': "pos",
    'previous': "prev",
    'production': "prod",
    'pseudo': "sudo",
    'reference': "ref",
    'references': "refs",
    'repeat': "rep",
    'request': "req",
    'result': "res",
    'revision': "rev",
    'source': "src",
    'standard': "std",
    'standing': "stdin",
    'standout': "stdout",
    'string': "str",
    'system': "sys",
    'temporary': "tmp",
    'text': "txt",
    'thanks': "thx",
    'utilities': "utils",
    'utility': "util",
    'value': "val",
    'variable': "var",
    # months
    'january': "jan",
    'february': "feb",
    'march': "mar",
    'april': "apr",
    'june': "jun",
    'july': "jul",
    'august': "aug",
    'september': "sept",
    'october': "oct",
    'november': "nov",
    'december': "dec",
}


ctx = Context('input')

keymap = {}
keymap.update(alpha)
keymap.update({
    'say <dgndictation> [over]': text,
    'shrink <dgndictation>': ShrinkWord,
    'word <dgnwords>': word,
    '(%s)+ <dgndictation>' % (' | '.join(formatters)): FormatText,
})

ctx.keymap(keymap)
