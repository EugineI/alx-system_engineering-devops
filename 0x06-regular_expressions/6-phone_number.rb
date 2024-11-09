#!/usr/bin/env ruby
#phone number
if ARGV[0]
  puts ARGV[0].scan(/^[0-9]{10}$/).join
end
