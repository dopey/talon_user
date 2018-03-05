from talon.voice import Context, Key

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('code', func=lambda app, win: any(
    t in app.bundle for t in terminals))
#languages = ['.php', '.py', '.java', '.yml', '.json']
#bundles = ['com.postmanlabs.mac']
#ctx = Context('code', func=lambda app, win:
#              any(app.bundle == b for b in bundles)
#              or any(win.doc.endswith(l) for l in languages)
#              )

def surround(by):
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word
    return func

keymap = {
    'state if': ['if ()', Key('left')],
    'state else': ['else {}', Key('left enter')],
    'state else if': ['else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state for each': ['foreach ()', Key('left')],
    'state switch': ['switch ()', Key('left')],

    'const': 'const ',
    'static': 'static ',
    'tip pent': 'int ',

    'word no': 'null',
    'word kneel': 'nil',
    'word printf': 'printf',
    'word define': 'def ',
    'word import': 'import ',
}

ctx.keymap(keymap)
