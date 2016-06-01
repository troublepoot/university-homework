
#------------------------------------------------------------------

#Name: Hayden Bridges
#Class: CST 100-1003
#Instructor: Sylvia Barnai
#Assignment 1
#Date: 01/16/2016

#-------------------------------------------------------------------


#part 1 ------------------------------------------------------------

#opening prompt
print("The following will convert the Farenheit temperature into Celsius

#asks user for Farenheit temperature
f_input_string = input("Enter the Farenheit temperature ")

#convert data into integer
f_input_int = int(f_input_string)

#convert Farenheit into Celsius
c = ((5.0 / 9.0) * (f_input_int - 32))

print ("The temperature in Celsius is ", c)

#part 2 -------------------------------------------------------------

#opening prompt
print("The following will calculate the area for a trapezoid")

#requests data from user
height_string = input("Enter the height ")
bottom_base_string = input("Enter the length of the bottom base ")
top_base_string = input("Enter the length of the top base ")

#convert data into integers
height_int = int(height_string)
bottom_base_int = int(bottom_base_string)
top_base_int = int(top_base_string)

#formula for area
A = ((0.5) * (bottom_base_int + top_base_int) * (height_int))

#post output
print("The area of the trapezoid is ", A)