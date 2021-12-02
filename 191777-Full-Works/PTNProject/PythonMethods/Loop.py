#Example file for working with conditional statement
def main():
	x,y =2,8
	if(x < y):
		st= "x is less than y"
	print(st)
if __name__ == "__main__":
	main()

#Example file for working with conditional statement with else
def main():
	x,y =8,4
	if(x < y):
		print(st= "x is less than y")
	else:
		st= "x is greater than y"
	print (st)
if __name__ == "__main__":
    main()

#Example file for working with conditional statement with elseif
def main():
	x,y =8,8
	if (x < y):
		print("x is less than y")
	elif (x == y):
		print( "x is same as y")
	else:
		print("x is greater than y")
if __name__ == "__main__":
	main()


# minium code execution
def main():
	x, y = 10, 8
	if (x < y):
		print("st=x is less than y")
	else:
		print("x is greater than or equal to y")
if __name__ == "__main__":
	main()

#nested if
total = 100
#country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
        print("Shipping Cost is $25")
elif total <= 150:
	    print("Shipping Costs $5")
else:
        print("FREE")
if country == "AU":
	  if total <= 50:
	    print("Shipping Cost is  $100")
else:
	    print("FREE")

#while loop#
#Example file for working with loops
x=0
#define a while loop
while(x <4):
		#print(x)
		x = x+1

#Define a for loop
for x in range(2,7):
		print(x)

Months = ["Jan","Feb","Mar","April","May","June"]
for m in (Months):
    print (m)

for x in range (10,20):
       if (x == 15): break
       #print (x)
#Use of Continue statement in for loop
for x in range (10,20):
       if (x % 5 == 0): continue
       print (x)
#Code for “enumerate function” with “for loop”
Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
    print (i,m)




