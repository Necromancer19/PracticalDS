n = int(input("Enter number of elements: ")) 

print("Enter the inputs: ")
inputs = [] # creating an empty list for inputs
for i in range(0, n): 
	ele = float(input()) 
	inputs.append(ele) # adding the element 
print(inputs) 

print("Enter the weights: ")
weights = [] 
for i in range(0, n): 
	ele = float(input()) 
	weights.append(ele) # adding the element 
print(weights) 

b=float(input("Enter bias value: "))
print("The net input can be calculated as   Yin = b + x1w1 + x2w2:")

Yin = []
for i in range(0, n):
	Yin.append(inputs[i]*weights[i])
print(round((sum(Yin)+b),3))
