from talon.voice import Context, Str, Word, Key, Rep, press
from typing import Iterable
import functools

ctx = Context('vim', bundle='com.googlecode.iterm2')

def prefix(destination, item):
  if isinstance(destination, Iterable):
    result = [item]
    result.extend(destination)
    return result
  else:
    return [item, destination]

def temp_escape_prefix(command):
    # ',' is my leader key in vim
    # ',/': maps to '<esc>l' in insert mode, maps to '<nop>' in other modes.
    return prefix(command, ',/')

def get_first_word(input):
    print(input.dgndictation[0]._words)
    return str(input.dgndictation[0]._words[0]).lower()

def find_next_word(input):
    word = get_first_word(input)
    Str("/%s\n" % word)(None)

numeral_map = {
    'o': '0',
    'oh': '0',
    'gun': '1',
    'shoe': '2',
    'me': '3',
    'door': '4',
    'dive': '5',
    'sticks': '6',
    'heaven': '7',
    'gate': '8',
    'knife': '9',
    'nice': '9'
}
delimiter_words = ['click', 'clip']

def parse_first_number(words):
    result = ''
    for index, word in enumerate(words):
        if word in delimiter_words:
            return (result, words[index+1:])
        if not word in numeral_map:
            raise Exception('%s not a number' % word)
        result += numeral_map[word]

    return (result, [])

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    return word

def get_words(input):
    tmp = [str(s).lower() for s in input.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    return words


def jump(input):
    words = get_words(input)
    jump_first(words)

def jump_first(words):
    line, remainder = parse_first_number(words)
    if line != '':
        Str("%sgg" % line)(None)
    return remainder

def range_action(action, input):
    words = get_words(input)
    print(words)
    remainder = jump_first(words)
    press('V')
    if remainder:
        jump_first(remainder)
    press(action)


for_temp_escape_prefix = {
    # range-copy
    'yank <dgndictation>': functools.partial(range_action, 'y'),
    # range-delete
    'delete lines <dgndictation>': functools.partial(range_action, 'd'),
    # range-poach
    'poach <dgndictation>': functools.partial(range_action, 'p'),
    # range-visual
    'visor <dgndictation>': functools.partial(range_action, ''),

    # jump
    'spring <dgndictation>': jump,

    # move-back-big-word
    'basil': 'B',
    # move-back-big-word-insert
    'basey': 'Bi',
    # move-back-word
    'baz': 'b',
    # move-back-word-insert
    'bazy': 'bi',
    # move-bottom
    'doomway': 'G',
    # move-forward-word
    'wax': 'w',
    # move-forward-word
    'waxy': 'wi',
    # move-forward-big-word
    'wacko': 'W',
    # move-forward-big-word-insert
    'wacky': 'Wi',
    # move-line-end-insert
    'derek': 'A',
    # move-page-down
    'page down': Key('ctrl-d'),
    # move-page-up
    'page up': Key('ctrl-u'),
    # move-top
    'goofy': 'gg',

    # surround-change
    'chapel': 'cs',
    # surround-delete
    'delltrap': 'ds',
    # surround-word
    'trap': 'ysiw',
    # surround-word-big
    'traple': 'ysiW',

    # redo
    'rizzle': Key('ctr-r'),
    # undo
    'dizzle': 'u',

    # fugitive-add
    'fudge pack':  ':Gwrite\n',
    # fugitive-commit
    'fudge commit':  [':Gcommit -v -a -q\n', 'i'],
    # fugitive-push
    'fudge push': ':Gpush origin HEAD\n',
    # fugitive-status
    'fudge status': ':Gstatus\n',

    # combine-line
    'jiggle': 'J',
    # new-line-above
    'spronko': 'O',
    # new-line-below
    'spronk': 'o',

    # find
    'marco': '/',
    # find-current
    'marthis': '*',
    # find-dictation
    'crew <dgndictation>': find_next_word,
    # find-next
    'marneck': 'n',
    # find-next
    'marprev': 'N',

    # repeat
    'rep': Rep(1),

    # center
    'zen': 'zz',

    # execute to the right
    'slap': [Key('esc'), ':w\n', Key('cmd-right up enter')],
}


keymap = {
    # copy
    'yank': 'yy',
    # delete
    'delete line': 'dd',

    # jump
    'jump': 'gg',
    # jump-insert-bol
    'jumpy': 'ggi',
    # jump-insert-eol
    'jumper': 'ggA',
    # jump-new-below
    'jumpo': 'ggo',

    #symbol
    'block': ['{\n}', Key('esc'), 'O'],

    # buffer-quit
    'barf': [Key('esc'), ':q\n'],
    # buffer-write
    'sage': [Key('esc'), ':w\n'],
    # buffer-write-quit
    'ragequit': [Key('esc'), ':wq\n'],
}

keymap.update({k: temp_escape_prefix(for_temp_escape_prefix[k]) for k in for_temp_escape_prefix})

ctx.keymap(keymap)
