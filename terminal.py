from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

mapping = {
    'semicolon': ';',
    r'new-line': '\n',
    r'new-paragraph': '\n\n',
}

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

# Ask for forgiveness not permission in failure scenario.
# https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
def text(m):
    try:
        tmp = [str(s).lower() for s in m.dgndictation[0]._words]
        words = [parse_word(word) for word in tmp]
        Str(' '.join(words))(None)
    except AttributeError:
        return

keymap = {
    'cd': ['cd ; ls', Key('left'), Key('left'), Key('left'), Key('left')],
    '(ls | run ellis | run alice)': 'ls\n',
    '(la | run la)': 'ls -la\n',
    'durrup': 'cd ..; ls\n',
    'go back': 'cd -\n',

    'pseudo': 'sudo ',
    'shell clear': [Key('ctrl-c'), 'clear\n'],
    'shell copy [<dgndictation>]': ['cp ', text],
    'shell copy curse [<dgndictation>]': ['cp -r', text],
    'shell exit': [Key('ctrl-c'), 'exit\n'],
    'shell kill': Key('ctrl-c'),
    'shell list [<dgndictation>]': ['ls ', text],
    'shell list all [<dgndictation>]': ['ls -la ', text],
    'shell make (durr | dear) [<dgndictation>]': ['mkdir ', text],
    'shell mipple [<dgndictation>]': ['mkdir -p ', text],
    'shell move [<dgndictation>]': ['mv ', text],
    'shell remove [<dgndictation>]': ['rm ', text],
    'shell remove curse [<dgndictation>]': ['rm -rf ', text],

    # Git
    'jet [<dgndictation>]': ['git ', text],
    'jet add [<dgndictation>]': ['git add ', text],
    'jet branch [<dgndictation>]': ['git br ', text],
    'jet branch delete [<dgndictation>]': ['git br -D ', text],
    'jet clone [<dgndictation>]': ['git clone ', text],
    'jet checkout master': 'git checkout master\n',
    'jet checkout max': 'git checkout max/',
    'jet checkout [<dgndictation>]': ['git checkout ', text],
    'jet checkout branch [<dgndictation>]': ['git checkout -B max/', text],
    'jet commit [<dgndictation>]': ['git commit ', text],
    'jet diff': 'git diff\n',
    'jet history': 'git hist\n',
    'jet merge [<dgndictation>]': ['git merge ', text],
    'jet pull [<dgndictation>]': ['git pull ', text],
    'jet pull base [<dgndictation>]': ['git pull --rebase ', text],
    'jet push [<dgndictation>]': ['git push ', text],
    'jet rebase': 'git rebase -i HEAD~',
    'jet stash': 'git stash\n',
    'jet status': 'git status\n',

    # Tools
    'grip': ['grep  .', Key('left left')],
    'gripper': ['grep -r  .', Key('left left')],
    'pee socks': 'ps aux ',
    'vi': 'vi ',
}

ctx.keymap(keymap)
