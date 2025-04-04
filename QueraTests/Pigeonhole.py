userinput = str(input())
ninput = userinput[:0]
minput= userinput[1:2]
print(int(ninput) , int(minput))
if int(ninput) > int(minput) :
    print("Yes")
if int(ninput) < int(minput):
    print("No")
if int(ninput)==int(minput):
    print("No")

