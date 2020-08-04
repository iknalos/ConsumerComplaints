import csv
import sys
import os
input_filename, output_filename = sys.argv[1:]

# Creating an error file to log the details of the errors
error_file = open(os.path.dirname(sys.argv[2])+'/error_logfile.txt', 'a')

listy=[]
listz=[]
with open(input_filename, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        row[0]=row[0].split('-')[0]
        row[1]=str(row[1].lower())
        listy.append([row[0]+row[1]])
        listz.append([row[0]+row[1]+row[7]])
#        print (row)
#        row.groupby('Date received').Product.nunique()
#total number of complaints received for that product and year
Output = {} 
  
# Using Iteration 
for lis in listy: 
    Output.setdefault(tuple(lis), list()).append(1) 
for a, b in Output.items(): 
    Output[a] = sum(b) 
del Output[next(iter(Output))]  

#total number of companies receiving at least one complaint for that product and year

Output1 = {} 

for lis in listz: 
    Output1.setdefault(tuple(lis), list()).append(1) 
for a, b in Output1.items(): 
    Output1[a] = sum(b) 
del Output1[next(iter(Output1))]

###
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
List1=[]
final_list=[]
#print (type(key))
for keys in Output:
#    print(type(key))
    value = convertTuple(keys) 
#    print (value[4:len(value)]+","+value[0:4],Output[keys]) 
    

    loop=[]
    i=0
    for key in Output1:
        valuex= str(key)
        if (value[:len(value)]) in valuex:
            i+=1
            z= {valuex,(Output1[key])}    
            loop.append(Output1[key])
    f1=max(loop)
#    print(f1)
    Percent=(f1/Output[keys])*100
    
    final=(value[4:len(value)],int(value[0:4]),Output[keys],i,round(Percent))
    final_list.append(final)
final_list.sort()
with open(output_filename, mode='a') as report_file:
    for row in final_list:
        report_writer = csv.writer(report_file, delimiter=',')
        report_writer.writerow(final)
