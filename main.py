def changeRecord(searchName, newScore):
    

    # Open the golfers.txt file.
    golfers_file = open('golfers.txt', 'r')
    
    # Open the temp file
    temp_file = open('temp.txt', 'w')

    # Read the first record's description field.
    golfer_name = golfers_file.readline()

    # Read the rest of the file.
    while golfer_name != '':
        # Read the score field.
        score = float(golfers_file.readline())

        # Strip the \n from the name.
        golfer_name = golfer_name.rstrip('\n')

        # Determine whether this record matches
        # the search value.
        if golfer_name == searchName:
            temp_file.write(golfer_name, '\n')
            temp_file.write(newScore, '\n')
        else:
            temp_file.write(golfer_name, '\n')
            temp_file.write(score, '\n')
            
        # Read the next name.
        golfer_name = golfers_file.readline()

    # Close the file.
    golfers_file.close()

    

def addRecord(name, newScore):
    #create a variable to control the loop
    meeps = 'y'
    #open the golfers.txt file in a mode

    golfers_file = open("golfers.txt", "a")

    while meeps == 'y' or meeps == 'Y':
        # Open the golfers.txt file in append mode.
         golfers_file = open('golfers.txt', 'a')

     # Add records to the file.
    while meeps == 'y' or meeps == 'Y':
         # Get the golfer record data.

         print('Enter the following golfer data:')
         golfer_name = input('golfer_name: ')
         score = int(input('Score (in numbers): '))

         # Append the data to the file.
         golfers_file.write(golfer_name + '\n')
         golfer_file.write(str(score) + '\n')

         # Determine whether the user wants to add
         # another record to the file.
         print('Do you want to add another record?')
         another = input('Y = yes, anything else = no: ')

# Close the file.

print(" Data added to golfers.txt.")                   
            
        
               

def removeRecord(searchName):

    import os #this is needed to remove or rename
    #get a bool variable
    found = false

    # Get the golfer to delete.
    search = input('Which golfer do you want to delete? ')
 
    # Open the original golfers.txt file.
    golfer_file = open('golfers.txt', 'r')
 
    # Open the temporary file.
    temp_file = open('temp.txt', 'w')
 
    # Read the first record's golfer_name field.
    golfer_name = golfer_file.readline()

    # Read the rest of the file.
    while golfer_name != '':
        # Read the quantity field.
        score = float(golfer_file.readline())
 
        # Strip the \n from the golfer_name
        golfer_name = golfer_name.rstrip('\n')
 
        # If this is not the record to delete, then
        # write it to the temporary file.
        if golfer_name != search:
            # Write the record to the temp file.
            temp_file.write(golfer_name + '\n')
            temp_file.write(str(score) + '\n')
 
            # Set the found flag to True.
            found = True
 
        # Read the next golfer_name.
        golfer_name = golfer_file.readline()
    
    # Close the golfer file and the temporary file.
    golfer_file.close()
    temp_file.close()
 
    # Delete the original golfers.txt file.
    os.remove('golfers.txt')
 
    # Rename the temporary file.
    os.rename('temp.txt', 'golfers.txt')
 
    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
    
def displayRecords():
    golfers_file = open("golfers.txt", "r")
    #read the first golfername
    golfer_name = golfers_file.readline()
    #read the rest
    while golfer_name !='':
               
        # Read the score field.
        score = float(golfers_file.readline())

        # Strip the \n from the name.
        golfer_name = golfer_name.rstrip('\n')

        # Display the record.
        print('Name of Golfer:', golfer_name)
        print('Score:', score)

        # Read the next name.
        golfer_name = golfers_file.readline()

    # Close the file.
    golfers_file.close()

    


def main():
    #open the golfers.txt file.
    displayRecords()
    
    

    #display the menu for the user
    while True:
        print("Menu")
        print("C (make a change to one of the records)")
        print("A  (add a record to the file)")
        print("D  (displays records)")
        print("R   (display the file with all records)")
        print("Q  (time to quit the program)")

        
        user_input = input("Your choice: ")
        print ("")
        print ("you selected:", user_input)
        
        if  user_input =="C" or user_input == "c":
            print("you selected:", user_input)
            searchName = input("Enter the name of the golfer you want to change the score for: ")
            newScore = input("Enter the score for the golfer: ")
            if newScore in range(1,151):
                changeRecord(searchName, newScore)
            else:
                print("Invalid Score provided", newsScore)


        elif user_input == "A" or user_input == "a":
            print("you selected:", user_input)
            print("Enter the name of the golfer you want to add to the file")
            addRecord(name, newScore)

        elif  user_input == "D" or user_input == "d":
            print("you selected:", user_input)
            print("Here is the list of golfers in the data file")
            displayRecords()


        elif user_input == "R" or user_input == "r":
            print("you selected:", user_input)
            print("Displaying the file with all the records")
            removeRecord(searchName)

        elif user_input == "Q" or user_input == "q":
            print("you selected:", user_input)
            print(" time to quit the program")

        else:
            print("invalid input provided:", user_input)
            print("")



if __name__ == "__main__":
    main()