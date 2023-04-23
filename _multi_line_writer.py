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

# Ask for the name of the user
name_user = input("\033[40mHow about you what is your name? \033[0m")
print("")
print(f"\033[40m\033[33mHi, {name_user}! I welcome you on this program. \033[0m")
print("")

# DEFINE write_to_file
def write_to_file():
 # OPEN file 'mylife.txt' in write mode
  with open('mylife.txt', 'w') as file:
  # SET line equal to user input of a line of text
     line = input("\033[35mEnter line: \033[0m")
     print("")
  # WRITE line to file with newline character
     file.write(line + '\n')
  # SET line_choice equal to user input of 'y' or 'n'
     line_choice = input("\033[34mDo you want to enter another line? (y/n): \033[0m")
     if line_choice.lower() == "y":
       # Make a greeting for the user 
      print("") 
      greetings = ["You are making great progress!.", "You have what it takes.", "You are amazing!", "It is awesome!"]
      print(random.choice(greetings)) 
     else:
       print("You are making great progress!")
  # WHILE line_choice.lower is equal to 'y'
     while line_choice.lower() == 'y':
    # SET line equal to user input of a line of text
      print("")
      line = input("\033[35mEnter line: \033[0m")
    # WRITE line to file with newline character
      file.write(line + '\n')
    # SET line_choice equal to user input of 'y' or 'n'
      print("")
      line_choice = input("\033[34mDo you want to enter another line? (y/n): \033[0m ")
      print("")
    # Make a greeting for the user  
      greetings = ["You are making great progress!", "You have what it takes.", "You are amazing!", "It is awesome!"]
      print(random.choice(greetings))

  # CLOSE file
  file.close()
  print("")
  print("\033[32mThe program is now writing it to txt file.\033[32m ")
  # State that the output is in the txt files
  print("")
  print("\033[32mPlease have time to visit the mylife.txt, if you want to look on the outputs.\033[32m")
  print("")

  # Create Footer
  print(f"\033[40m\033[33mThank you for your time, {name_user}! \033[0m")
  print("")
  goodbye = pyfiglet.figlet_format("Visit me again", font = "digital" )
  print (goodbye)
  print("")

# Call the method to run the code
write_to_file()
