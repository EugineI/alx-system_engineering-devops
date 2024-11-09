#!/usr/bin/env ruby
#repetition 2
if ARGV[0]
  puts ARGV[0].scan(/^h[a-zA-Z0-9]{1}n$/).join
end
