# import modules 
import os 
import csv

# Get the paths for reading and writing 
dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, '03-Python_homework_assignment_PyPoll_Resources_election_data.csv' )
output_path = os.path.join(dir_path, "output.csv")
# Declare the variables 
total_vote = 0
khan = 0 
correy = 0 
Li = 0 
o_tooley = 0 

# Open file and read row by row and check and see who was voted for and add that number to the persons variable 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    row1 = next(csvreader)
    for row in csvreader:
        total_vote = total_vote + 1 
        if(row[2] == 'Khan'):
            khan = khan + 1
        elif(row[2] == 'Correy'):
            correy = correy + 1
        elif(row[2] == 'Li'):
            Li = Li + 1
        else:
            o_tooley = o_tooley + 1
    # Created a dictionary to get the name of the person that won. Gave the number of votes to the name
    winner = {khan: "Khan", correy: "Correy", Li: "Li", o_tooley: "O'Tooley"}
    # print the values  
    print("Election Votes \n")
    print("-------------------- ")
    print("Total Votes: " , (total_vote) )
    print("-------------------- \n")
    print("Khan:", round(((khan / total_vote) * 100),2), '% (' ,khan, ')')
    print("Coorey:", round(((correy / total_vote) * 100),2), '% (' ,correy, ')')
    print("Li:", round(((Li / total_vote) * 100),2), '% (' ,Li, ')')
    print("O'Tooley:", round(((o_tooley / total_vote) * 100),2), '% (' ,o_tooley, ')')
    print("--------------------")
    print("Winner: ", winner.get(max(winner)))
    print("--------------------")
    #    Used for writing the values in the output 
    mytuple = (total_vote,khan,correy,Li,o_tooley,winner.get(max(winner)))
# Write in the output file our values found 
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Votes' , 'Khan' , 'Coorey', 'Li', 'O Tooley', 'Winner'])
    csvwriter.writerow(mytuple)