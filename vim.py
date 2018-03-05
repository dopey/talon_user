from talon.voice import Context, Str, Word, Key, Rep
from typing import Iterable
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('vim', func=lambda app, win: any(
    t in app.bundle for t in terminals))

def prefix(destination, item):
  if isinstance(destination, Iterable):
    result = [item]
    result.extend(destination)
    return result
  else:
    return [item, destination]

def temp_escape_prefix(command):
    # ',/': maps to '<esc>l' in insert mode, maps to '<nop>' in other modes.
    return prefix(command, ',/')

def get_first_word(m):
  str(m.dgndictation[0]._words[0])

def find_next_word(m):
  word = get_first_word(m)
  Str("/%s\n" % word)(None)

for_temp_escape_prefix = {
    # buffer-quit
    'barf': ':q\n',
    # buffer-write
    'sage': ':w\n',
    # buffer-write-quit
    'ragequit': ':wq\n',

    # jump
    'spring': 'gg',

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
    # move-forward-big-word
    'wacko': 'W',
    # move-line-end
    'ricky': '$',
    # move-line-end-insert
    'derek': 'A',
    # move-line-start
    'lefty': '^',
    # move-page-down
    'page down': Key('ctrl-d'),
    # move-page-up
    'page up': Key('ctrl-u'),
    # move-top
    'jeepway': 'gg',

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
    'fudge commit':  ':Gcommit -v -a -q\n',
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

    # copy
    'yank': 'yy',

    # find
    'marco': '/',
    # find-current
    'marthis': '*n',
    # find-dictation
    'crew <dgndictation>': find_next_word,
    # find-next
    'marneck': 'n',
    # find-next
    'marprev': 'N',

    # repeat
    'rep': Rep(1),
}


keymap = {}

keymap.update({k: temp_escape_prefix(for_temp_escape_prefix[k]) for k in for_temp_escape_prefix})

ctx.keymap(keymap)
