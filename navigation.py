from talon.voice import Context, Key

ctx = Context('navigation')

keymap = {
    # Requires activation of System Preferences -> Shortcuts -> Input Sources
    # -> "Select the previous input source"
    'change language': Key('ctrl-space'),

    # Application navigation
    'swick': Key('cmd-tab'),
    'totch': Key('cmd-w'),
    'new window': Key('cmd-n'),
    '(next window | gibby)': Key('cmd-`'),
    '(last window | shibby)': Key('cmd-shift-`'),
    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    # Following three commands should be application specific
    #'(baxley | go back)': Key('cmd-alt-left'),
    #'(fourthly | go forward)': Key('cmd-alt-right'),
    # '(new tab | peach)': Key('cmd-t'),

    # deleting
    # '(delete line)': Key('cmd-right cmd-backspace'),
    'steffi': Key('alt-ctrl-backspace'),
    'stippy': Key('alt-ctrl-delete'),
    'carmex': Key('alt-backspace'),
    'kite': Key('alt-delete'),
    'snipple': Key('cmd-shift-left delete'),
    'snipper': Key('cmd-shift-right delete'),
    'slurp': Key('backspace delete'),
    'slurpies': Key('alt-backspace alt-delete'),

    # moving
    '(tab | tarp)': Key('tab'),
    'tarsh': Key('shift-tab'),
    # 'slap': [Key('cmd-right enter')],
    'shocker': [Key('cmd-left enter up')],
    'wonkrim': Key('alt-ctrl-left'),
    'wonkrish': Key('alt-ctrl-right'),
    'fame': Key('ctrl-left'),
    'fish': Key('ctrl-right'),
    'ricky': Key('cmd-right'),
    'ricky 2': [Key('cmd-right'), Key('cmd-right')],
    'ricky 3': [Key('cmd-right'), Key('cmd-right'), Key('cmd-right')],
    'ricky 4': [Key('cmd-right'), Key('cmd-right'), Key('cmd-right'), Key('cmd-right')],
    'lefty': Key('cmd-left'),
    'lefty 2': [Key('cmd-left'), Key('cmd-left')],
    'lefty 3': [Key('cmd-left'), Key('cmd-left'), Key('cmd-left')],
    'lefty 4': [Key('cmd-left'), Key('cmd-left'), Key('cmd-left'), Key('cmd-left')],
    'crimp': Key('left'),
    'crimp 2': [Key('left'), Key('left')],
    'crimp 3': [Key('left'), Key('left'), Key('left')],
    'crimp 4': [Key('left'), Key('left'), Key('left'), Key('left')],
    'crimp 5': [Key('left'), Key('left'), Key('left'), Key('left'), Key('left')],
    'chris': Key('right'),
    'chris 2': [Key('right'), Key('right')],
    'chris 3': [Key('right'), Key('right'), Key('right')],
    'chris 4': [Key('right'), Key('right'), Key('right'), Key('right')],
    'chris 5': [Key('right'), Key('right'), Key('right'), Key('right'), Key('right')],
    '(up | jeep)': Key('up'),
    '(down | dune | doom)':  Key('down'),

    'scroll down': [Key('down')] * 30,
    '(doomway | scroll way down)': Key('cmd-down'),
    'scroll up': [Key('up')] * 30,
    '(jeepway | scroll way up)': Key('cmd-up'),

    # selecting
    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep': Key('shift-up'),
    'shroom': Key('shift-down'),
    'lecksy': Key('cmd-shift-left'),
    'ricksy': Key('cmd-shift-right'),
    'scram': Key('alt-shift-left'),
    'scrish': Key('alt-shift-right'),
    'schrim': Key('shift-left'),
    'shrish': Key('shift-right'),
}

ctx.keymap(keymap)
