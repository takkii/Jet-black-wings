#!/usr/bin/ruby

class Dark
  def black
    Dir.mkdir('~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload', perm = 0o777) unless FileTest.exist?('~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload')
    Dir.mkdir('~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload/source', perm = 0o777) unless FileTest.exist?('~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload/source')
  end
end

Dark.new.black

class White
  def magic
    File.open('~/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload/source/ruby_methods', 'a:utf-8', perm = 0o777) do |f|
      f.puts Class.methods
    end
  end
end

White.new.magic
