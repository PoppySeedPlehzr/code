
def compute_spin(vals)
    vals.each { |x| raise "Values must be ints between 0 and #{vals[0].to_i}" unless 0 <= x.to_i and x.to_i <= vals[0].to_i }
    n = vals[0].to_i
    a1 = vals[1].to_i
    a2 = vals[2].to_i
    a3 = vals[3].to_i
    return (3*n+a1
end


if $0 == __FILE__
    unless ARGV.length == 4
        puts "Must provide 3 integers"
    else
        puts compute_spin ARGV 
    end
end



