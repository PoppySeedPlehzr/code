
# Function to computer the perimeter
def perm(n, r)
    return n*(2*Math::sin(Math::PI/n)*r)
end


d = gets.chomp.split()
n = d[0].to_i
s = d[1].to_f

if n < 3 or n > 100
    puts "First value must be an integer between 3 and 100"
    abort
elsif s < 0.1 or s > 100.0
    puts "First value must be a float between 0.1 and 100.0"
    abort
end
puts "#{'%.03f' % perm(d[0].to_i, d[1].to_f)}"



