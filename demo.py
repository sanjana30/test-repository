# this is just a demo code for github

# change your name in the following line
name = "Sanjana"

# Display the value in the name variable (placeholder tag for a real number) )
print ("Hello my name is ",name)

# change the hobbies array by replacing the text in " " by your hobbies. You can also add more hobbies if you want
hobbies = ["Reading", "Cleaning"]

# Display a placeholder text
print ("My hobbies are: ")

# In the following code, we have created a "for" loop. 
# A "for" loop will take a variable (here the variable is "i") and a range of numbers and then it will execute the lines that follow the for loop and are indented to the right a certain number of times.
# Here I am just looping through the hobbies array (len(hobbies) returns a count of how long the array is. The length here is 3). So the loop will run 3 times and print each hobby one by one
for i in range(0, len(hobbies)):
	print(i+1, ": ", hobbies[i])
	print("\n")