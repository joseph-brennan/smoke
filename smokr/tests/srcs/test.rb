#!/usr/bin/env ruby
count = gets.to_i
numbers = gets.split.map(&:to_i)
min = 10000000
numbers.each do |number|
  min = number if min.abs > number.abs or (min.abs == number.abs and min < number)
end

if count>0
  puts min
else
  puts 0
end
