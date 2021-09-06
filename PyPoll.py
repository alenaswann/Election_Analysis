#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 

#Add dependencies
import csv
import os
#Assign a variable for the file to load and the path.(indirect)
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to load and the path.(direct)
#file_to_load = 'Resources/election_results.csv'

# Assisgn a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data: 

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read and print the header row.
    headers = next(file_reader)
    print(headers)
   




#Writing in data file using open & close functions
    # Create a filename variable to a direct or indirect path to the file.
    #file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Using the with statement open the file as a text file.
    #outfile = open(file_to_save, "w")
    # Write some data to the file.
    #outfile.write("Hello World")

    # Close the file
    #outfile.close()

#Writing in data file using with statements

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
