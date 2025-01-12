#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit(1)
end

input = ARGV[0]

regex = /School/

if input.match?(regex)
  puts "Match found: #{input}"
else
  puts "No match"
end
