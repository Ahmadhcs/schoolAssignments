
"""
Ahmad Almesned
September 25th,2020
CSCI_UA.0003-001


"""

print(format("*" * 9, ">50"))
print(format(" |welcome|", ">50"))
print(format("*" * 9, ">50"))
print("Perhaps I can help you calculate $$$ for yr tip!")

people = int(input("How many people?\n>"))
cost = float(input("how much did it cost?\n>"))

# main component of program, that calculates the tip
if people >= 6:
   print("You should probably tip:", "$" + str(format(cost * .2, ">.2f")))
else:
   service = input("How was the service?\n>")
   if service == "terrible":
       print("You should tip nothing")
   elif service == "poor":
       print("you should probably tip:", "$" + str(format(cost * .1, ">.2f")))
   elif service == "ok":
       print("you should probably tip:", "$" + str(format(cost * .15, ">.2f")))
   elif service == "good":
       print("you should probably tip:", "$" + str(format(cost * .2, ">.2f")))
   elif service == "great":
       print("you should probably tip:", "$" + str(format(cost * .25, ">.2f")))
   else:
       print("you should probably tip:", "$" + str(format(cost * .2, ">.2f")))


