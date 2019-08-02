#!/usr/bin/ruby

class White
  def magic
    File.open('$HOME/.config/nvim/.cache/dein/repos/github.com/takkii/Jet-black-wings/autoload/source/ruby_methods', 'a:utf-8', perm = 0o777) do |f|
      f.puts Class.methods
    end
  end
end

White.new.magic
