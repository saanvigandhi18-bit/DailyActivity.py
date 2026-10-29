minutes = int(input("Enter the number of minutes you spent on homework today: "))
if minutes > 60:
   plan = "start homework now" 
   print("That is a long homework session.")
else: 
    plan = "finish homework quickly"
    print("That is a short homework session.")

free_time = input("Do you have free time after homework? (yes/no):  ")
if free_time == "yes":
    print("Pick a hobby")
else:
    print("")

print("=== DAILY PLAN ===")
print("Homework Plan:", plan)
print("Free Time After Homework:", free_time)
print("===================")    