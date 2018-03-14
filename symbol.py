from talon.voice import Context, Key

ctx = Context('symbol')

keymap = {
    '(escape | lulu | randall)': [Key('esc'), Key('right')],
    '(question [mark] | questo)': '?',
    '(minus | dash)': '-',
    'plus': '+',
    'tilde': '~',
    '(bang | exclamation point | clamor)': '!',
    '(dollar [sign] | dolly)': '$',
    '(downscore | crunder)': '_',
    '(semi | semicolon | sunk)': ';',
    'colon': ':',

    '(square | left square [bracket] | brackorp)': '[',
    '(rsquare | are square | right square [bracket] | brackose)': ']',
    '(paren | left paren)': '(',
    '(rparen | are paren | right paren)': ')',
    '(brace | left brace | kirksorp)': '{',
    '(rbrace | are brace | right brace | kirkos)': '}',
    '(angle | left angle | less than)': '<',
    '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | hash [sign] | octo | thorpe | number sign)': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    '(pipe | spike)': '|',

    '(dubquote | double quote | quatches)': '"',
    '(quote | quatchet)': "'",
    'triple quote': "'''",
    'tick': "`",
    'triple tick': "```",
    '(dot | period)': '.',
    'comma': ',',
    'swipe': ', ',
    'coalgap': ': ',
    'skoosh': ' ',
    '[forward] slash': '/',
    '[forward] slasher': '// ',
    '[forward] dubslash': '//',
    'backslash': '\\',
    'coalshock': [':', Key('enter')],
    'coal twice': '::',
    'ellipsis': '...',
    'mintwice': '--',
    'plustwice': '++',

    # equality
    'coleek': ' := ',
    'empty dict': '{}',
    'minquall': '-=',
    'pluqual': '+=',
    'starqual': '*=',
    'lessqual': ' <= ',
    'grayqual': ' >= ',
    'equals': '=',
    'equeft': ' = ',
    '([is] equal to | longqual)': ' == ',
    '([is] not equal to | banquall)': ' != ',
    'trickle': ' === ',
    '(ranqual | nockle)': ' !== ',

    '(arrow | lambo)': '->',
    'shrocket': ' => ',
    'sinker': [Key('cmd-right ;')],

    # surrounders
    'angler': ['<>', Key('left')],
    '(empty array | brackers)': '[]',
    'brax': ['[]', Key('left')],
    'brax-block': ['[', Key('enter')],
    'posh': ["''", Key('left')],
    'coif': ['""', Key('left')],
    'glitch': ['``', Key('left')],
    'kirk': ['{}', Key('left')],
    '(block | kirblock)': ['{}', Key('left enter')],
    '(call | prekris)': '()',
    'prex': ['()', Key('left')],
    'prex-block': ['(', Key('enter')],
    'precoif': ['("")', Key('left'), Key('left')],

    'and sign': '&',

    '(dot dot | dotdot | doodle)': '..',
    '(enter | shock)': Key('enter'),
    'junk': Key('backspace'),
    'spunk': Key('delete'),


}

ctx.keymap(keymap)
