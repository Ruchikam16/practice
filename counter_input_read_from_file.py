import collections
	       
co=collections.Counter()
	       
counter_input=open("counter_input.txt","r")
	       
for line in counter_input:
	       co.update(line)
print co

	       
