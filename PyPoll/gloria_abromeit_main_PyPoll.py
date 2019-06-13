file = "../Resources/election_data.csv"

import csv



with open(file) as pypoll_data:
    reader = csv.reader(pypoll_data)

    next(reader) 
    ID = []
    vote = []

    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    Khan = 0
    Correy = 0
    Li = 0
    O_Tooley = 0

    for row in reader:
        vote.append(row[2])

        if row[2] == candidates[0]:
            Khan += 1
        if row[2] == candidates[1]:
            Correy += 1
        if row[2] == candidates[2]:
            Li += 1
        if row[2] == candidates[3]:
            O_Tooley += 1

    Khan_Av = (Khan / (len(vote))) * 100
    Correy_Av = (Correy / (len(vote))) * 100
    Li_Av = (Li / (len(vote))) * 100
    O_Tooley_Av = (O_Tooley / (len(vote))) * 100

    winner_decision = [Khan_Av, Correy_Av, Li_Av, O_Tooley_Av]
    maximum = max(winner_decision)


    if maximum == Khan_Av:
        winner = "Kahn"
    elif maximum == Correy_Av:
        winner = "Correy"
    elif maximum == Li_Av:
        winner = "Li"
    elif maximum == O_Tooley_Av:
        winner = "O'Tooley"

print("Election Results")
print("--------------------------")
print("Total Votes: ", len(vote))
print("--------------------------")
print("Kahn: ", round(Khan_Av,0),"%", "(",Khan,")")
print("Correy: ", round(Correy_Av,0),"%", "(",Correy,")")
print("Li: ", round(Li_Av,0),"%", "(",Li,")")
print("O'Tooley: ",round(O_Tooley_Av,0),"%", "(",O_Tooley,")")
print("--------------------------")
print("Winner:", winner)
print("--------------------------")

with open('voteresults.txt', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Election Results"])
    filewriter.writerow(["--------------------------"])
    filewriter.writerow(["Total Votes: ", len(vote)])
    filewriter.writerow(["--------------------------"])
    filewriter.writerow(["Kahn: ", round(Khan_Av,0),"%", "(",Khan,")"])
    filewriter.writerow(["Correy: ", round(Correy_Av,0),"%", "(",Correy,")"])
    filewriter.writerow(["Li: ", round(Li_Av,0),"%", "(",Li,")"])
    filewriter.writerow(["O'Tooley: ",round(O_Tooley_Av,0),"%", "(",O_Tooley,")"])
    filewriter.writerow(["--------------------------"])
    filewriter.writerow(["Winner:", winner])
    filewriter.writerow(["--------------------------"])