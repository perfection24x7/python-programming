x = int(input("Please enter max limit "))

# Here I used int to collect the value in Integer format. 

a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for i in range(x) :
        c = a + b
        if c >= x: break
        print (c, end=' ')
        a = b
        b = c

print()
