#!/usr/bin/ruby

class Dark
  def black
    Dir.mkdir('complete', perm = 0o777) unless FileTest.exist?('complete')
  end
end

Dark.new.black

class White
  def magic
    File.open('complete/ruby_methods', 'a:utf-8', perm = 0o777) do |f|
      f.puts (Class.methods + Object.methods).sort.uniq
    end
  end
end

White.new.magic
