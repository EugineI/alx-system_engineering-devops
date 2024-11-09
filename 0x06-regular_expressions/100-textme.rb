#!/usr/bin/env ruby
#take log entries
entry = ARGV[0]
sender = entry.match(/\[from:(.+?)\]/)[1]
receiver = entry.match(/\[to:(.+?)\]/)[1]
flag = entry.match(/\[flags:(.+?)\]/)[1]
puts "#{sender},#{receiver},#{flag}"
