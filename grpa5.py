age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:]) # int, int, int: Get the correct parts from dob as int

fifth_birthday = str(day) + "/" + str(month) + "/" +str(year+5) # str: fifth birthday formatted as day/month/year 

last_birthday = str(day) + "/" + str(month) + "/" + str(year+age) # str: last birthday formatted as day/month/year
month += 10
month, year =(month-1)%12+1, year+(month-1)//12
tenth_month = str(day) + "/" + str(month) + "/" + str(year) # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month,fifth_birthday,last_birthday, sep=", ")