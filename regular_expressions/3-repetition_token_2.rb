#!/usr/bin/env ruby

# Print matches for "htn" and "hbtn" in the input argument
puts ARGV[0].scan(/hbt{1,5}n/).join
