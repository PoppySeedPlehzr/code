# Nick Anderson
#
# Ruby script to find the MST of a specified Adjacency Matrix
# Reddit Daily Programmer Challenge #152
# Utilized Prim's algorithm.  Running time should be ~n^2
# as I don't use a binary heap.
#

print "Enter the number of vertices: "
num_v = gets.chomp().to_i
if num_v > 26
	puts "Number of vertices must be 26 or less."
	exit
end

# List containing the edges of the MST
edge_wts = []
puts "Enter the newline delimited adjacency matrix:"
for i in 0..num_v
	edge_wts << gets.chomp()
end

# The alphabet
alph      = ("A".."Z").to_a 
traversal = []
visited   = []
# Get an initial vertex
visited   << (0..num_v).to_a.sample
mst_cost  = 0

while visited.size() < num_v do
	# Init Ruby Int max, src node, dst node
	min_edg = [(2**(0.size * 8 -2) -1),-1,-1]
	visited.each do |v|
		weights = edge_wts[v].split(',').map!{ |x| x.to_i }
		for i in 0..weights.length-1
			if weights[i] >= 0 and weights[i] <= min_edg[0] and not visited.include?(i)
				min_edg = [weights[i],v,i]
			end
		end
	end
	visited << min_edg[2]
	traversal << alph[min_edg[1]]+alph[min_edg[2]]
	mst_cost += min_edg[0]
end

# Dump the output
puts mst_cost
puts traversal.join(",")
