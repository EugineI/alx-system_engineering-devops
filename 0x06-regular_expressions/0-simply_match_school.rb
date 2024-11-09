#!/usr/bin/env ruby
# matches school
if ARGV[0]
  puts ARGV[0].scan(/School/).join
end
