'''Laura V. Bullock
9/24/2024
Week4 - Day1
In-Class Lab - hackathon_9-24.py

You are given both messages:'''

msg1 = "welcome to aws python 101 class: strings"
msg2 = "The instructor here is Cloudio"

#Write a python program what will:

#1 Capitalize all first character of each word of msg 1
print(msg1.title())

#2 Reverse msg2
print(msg2[::-1])

#3 Write msg1 in lower case
print(msg1.lower())

#4 Write msg2 in upper case
print(msg2.upper())

#5 Find how many "e" character was use in msg2
count_e = msg2.count("e")
print(count_e)

#6 Replace "python" by "java" in msg1
replaced_msg1 = msg1.replace("python", "java")
#note:  "welcome to aws java 101 class: strings" is now assigned to replaced_msg1
print(replaced_msg1)

#7 Create a new message "python is great" using msg1 characters.
new_msg1 = msg1[15:21] + " " + msg1[-4] + msg1[-1] + " " + msg1[-2] + msg1[-5] + msg1[1] + msg1[11] + msg1[-6]
print(new_msg1)

#8 Create a new message "Java is well done" using msg1 characters.
#Note:  use #6 variable as it is now a new sentence with the word java
new_msg2 = replaced_msg1[15:19].capitalize() + " " + replaced_msg1[-4] + replaced_msg1[-1] + " " + replaced_msg1[0:3] + replaced_msg1[2] + " " +  "d" + replaced_msg1[4] + replaced_msg1[-3] + replaced_msg1[1]
print(new_msg2)