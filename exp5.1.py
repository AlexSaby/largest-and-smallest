#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the
# largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
# and ignore the number.
largest= None
smallest= None
while True:
          num= input("Enter a number:")
          if(num=='done'):
             break
          try:
             value=int(num)
             if smallest is None:
                 smallest=value
             if largest is None:
                 largest=value
             if value<smallest:
                 smallest=value
             if value>largest:
                 largest=value
          except:
              print("Invalid input")

print("Maximum is",largest)
print("Minimum is",smallest)


