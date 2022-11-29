#Amirreza Hosseini 9820363
import os

#run a command and store the output in a variable
def run_command(command):
    return os.popen(command).read()

output=run_command('ubcsat -alg gsat -inst "DIMACS Input.txt" -solve -r solution "temp.txt"')
                   
#open the file and read the solution
f=open("temp.txt","r")
solution=f.read()
f.close()

#want secend line of output
solution=solution.split("\n")
solution=solution[1]

#split the second line and get the last element
solution=solution.split(" ")
solution=solution[-1]

#delete the temp file
os.remove("temp.txt")

#write the solution to a file
f=open("DIMACS Output.txt","w")
f.write(solution)
f.close()

print(solution)





