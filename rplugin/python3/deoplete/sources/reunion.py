import os
import re
import traceback
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------

home = expanduser("~")

d1 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings")
d2 = os.path.expanduser("~/.cache/dein/repos/github.com/takkii/Jet-black-wings")

if os.path.exists(d1):
    ruby = open(os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/complete/ruby_methods"))
    ruby_lib = open(os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload/source/ruby_list"))
elif os.path.exists(d2):
    ruby = open(os.path.expanduser("~/.cache/dein/repos/github.com/takkii/Jet-black-wings/complete/ruby_methods"))
    ruby_lib = open(os.path.expanduser("~/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload/source/ruby_list"))
else:
    print("Don't forget, Install dein plugin manager github repo")

just_ruby = ruby_lib.readlines()
new_ruby = ruby.readlines()
index_ruby = new_ruby + just_ruby
data_ruby = list(map(lambda s:s.rstrip(),index_ruby))
ruby.close()
ruby_lib.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'Jet-black-wings'
        self.filetypes = ['ruby']
        self.mark = '[JUDGEMENT_NIGHT_OF!]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_ruby
            dic.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()
