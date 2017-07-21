# Run two ways
# Command Line: julia first_julia.jl
# Julia Promt:  include("OneDrive/CS/Julia/first_julia.jl")
# Use text color for python, probably similar


println("Hello world")
println("Lets play!")

v = 5
println("Number ", v)

arr = [1,2,3]
push!(arr, 10)
println(arr)
for i in arr
	println(i)
end

for (k,v) in Dict("dog"=>"mammal","cat"=>"mammal","mouse"=>"mammal")
    println("$k is a $v")
end

println(maximum(arr))
println(in(3,arr))
println(in(4,arr))

function multi2(x)
	temp = []
	for i in 1:length(x)
		push!(temp, x[i]*2)
	end
	x = temp
end

println(multi2(arr))

dot2 = dot(arr, arr)
println(dot2, " ", norm(arr))


statisticians = Dict("Gosset" => "1876-1937", "Pearson" => "1857-1936", "Galton" => "1822-1911")
get!(statisticians, "Kendall", "I'm sorry, I don't know when this person lived.")
statisticians
declaration = "We hold these truths to be self evident."
re1 = r"uths"
match = declaration[search(declaration, re1)]
print("Re match $match\n")

manyM = matchall(r" th[a-z]*|truths ", declaration)
for m in manyM
	println(m)
end

done = false

println("start while loop not $(done)")

i = 0
while done != true
	println(i)
	i += 1
	if i > 5
		done = true
	end
end

function symbol1(y, x, z)
	val = x(y, z)
	return val
end

println(symbol1(5,+,3))


type c1{x}
	size::x
end

class1 = c1(3)
println(class1.size)