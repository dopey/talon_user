from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'broadcaster': Key('cmd-alt-i'),
    'full-screen': Key('cmd-shift-enter'),
    'split horizontal': Key('cmd-shift-d'),

}

ctx.keymap(keymap)
