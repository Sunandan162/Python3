n=int(input("Please provide a number: "))
s=str(n)
r=s[::-1]
if r==s:
    print("Palindrome")
else:
    print("Not Palindrome")

