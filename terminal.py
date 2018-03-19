from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

keymap = {
    'cd': ['cd ; ls', Key('left'), Key('left'), Key('left'), Key('left')],
    '(ls | run ellis | run alice)': 'ls\n',
    '(la | run la)': 'ls -la\n',
    'durrup': 'cd ..; ls\n',
    'go back': 'cd -\n',

    'pseudo': 'sudo ',
    'shell clear': [Key('ctrl-c'), 'clear\n'],
    'shell copy': 'cp ',
    'shell copy curse': 'cp -r',
    'shell exit': [Key('ctrl-c'), 'exit\n'],
    'shell kill': Key('ctrl-c'),
    'shell list': 'ls ',
    'shell list all': 'ls -la',
    'shell make (durr | dear)': 'mkdir ',
    'shell mipple': 'mkdir -p ',
    'shell move': 'mv ',
    'shell remove': 'rm ',
    'shell remove curse': 'rm -rf ',

    # Git
    'jet': 'git ',
    'jet add': 'git add ',
    'jet clone': 'git clone ',
    'jet checkout': 'git checkout ',
    'jet checkout branch': 'git checkout -B ',
    'jet commit': 'git commit ',
    'jet diff': 'git diff\n',
    'jet history': 'git hist\n',
    'jet merge': 'git merge ',
    'jet pull': 'git pull ',
    'jet pull base': 'git pull --rebase ',
    'jet push': 'git push origin ',
    'jet rebase': 'git rebase -i HEAD~',
    'jet stash': 'git stash\n',
    'jet status': 'git status\n',

    # Tools
    'gripper': 'grep -r ',
    'pee socks': 'ps aux ',
    'vi': 'vi ',
}

ctx.keymap(keymap)
