import csv
import re 

with open('Anomodom_Annotations.csv', newline='') as csv_file:

# input: a csv with four columns: names, start, end and type

    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader =  list(csv_reader) # save everything as a list here
    csv_reader.pop(0) # remove header
    final_list = [] # create an empty list to housing all the rows
    name_list = [] # an empty list to store the gene names 
    
    
    for row in csv_reader: # each row is a list
        
        name = (row.pop(0)).split() # remove the gene name, name[0] = gene name
        name_list.append(name[0])
       
        if "gene" in name:
            final_list.append(row)
            final_list.append(["", "", "", "gene", name[0]])
            
        elif "CDS" in name:
            final_list.append(row)
            final_list.append(["", "", "", "product", name[0]]) # add translatable later
            final_list.append(["", "", "", "transl_table", "11"])
            
        elif "tRNA" in name:
            final_list.append(row)
            final_list.append(["", "", "", "tRNA", name[0]])

        elif "rRNA" in name:
            final_list.append(row)
            final_list.append(["", "", "", "rRNA", name[0]])

    for row in enumerate(csv_reader):
            
        if "exon" in row:
            row [2] = "CDS"
            final_list.append(row)
           
            if name[0] == next(name[0]):
                row [2] = ""
                final_list.append(row)
                
            else:
                final_list.append(["","","","product",name[0]])
                final_list.append(["", "", "", "transl_table", "11"])
                
# output: a CSV with species name as header, and everything else in the five column format

with open('Genbank_5Column_Anomodon.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(["> Feature Anomodon", "", "", "", ""])
    for row in final_list:
        spamwriter.writerow(row)
    
