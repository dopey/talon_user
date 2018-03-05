from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'exit session': [Key('ctrl-c'), 'exit\n'],
    'broadcaster': Key('cmd-alt-i'),
    'clear session': [Key('ctrl-c'), 'clear\n'],
    'exit session': [Key('ctrl-c'), 'exit\n'],
    'full-screen': Key('cmd-shift-enter'),
    'pseudo': 'sudo',
    'split horizontal': Key('cmd-shift-d'),

}

ctx.keymap(keymap)
