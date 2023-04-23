# Vergel, Chean Bernard Villanueva
# Assignment No. 4
# Question No. 3

# Creating header 
import pyfiglet
import random

print("")
print("=" * 80)
print("")
welcome = pyfiglet.figlet_format("Welcome to my space".center(57, " "), font="digital")
print(welcome)
print("")
print("=" * 80)
print("\033[33mHi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.\033[0m")
print("")

# DEFINE write_to_file
def write_to_file():
 # OPEN file 'mylife.txt' in write mode
  with open('mylife.txt', 'w') as file:
  # SET line equal to user input of a line of text
     line = input("Enter line: ")
  # WRITE line to file with newline character
     file.write(line + '\n')
  # SET line_choice equal to user input of 'y' or 'n'
     line_choice = input("Enter another line? (y/n): ")
  # WHILE line_choice.lower is equal to 'y'
     while line_choice.lower() == 'y':
    # SET line equal to user input of a line of text
      line = input("Enter line: ")
    # WRITE line to file with newline character
      file.write(line + '\n')
    # SET line_choice equal to user input of 'y' or 'n'
      line_choice = input("Enter another line? (y/n): ")
    # Make a greeting for the user  
      greetings = ["You are making great progress!, You have what it takes, You are amazing!, It is awesome!"]
      print(random.choice(greetings))

  # CLOSE file
  file.close()
  print("Writing to file complete")
  
write_to_file()
