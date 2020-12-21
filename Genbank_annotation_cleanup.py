import csv
import re 

exon_pattern = "

with open('Anomodom_Annotations.csv', newline='') as csv_file:

# input: a csv with four columns: names, start, end and type

    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader =  list(csv_reader) # save everything as a list here
    csv_reader.pop(0) # remove header
    final_list = [] # create an empty list to housing all the rows
    name_list = [] # an empty list to store the gene names 
    
    
    for row in csv_reader: # each row is a list
        new_row = [] # create new row for each row for appending into final_list
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

        elif "exon" in name: # can append, cannot add final line 
            if name[2] == "1":
                row[2] = "CDS"
                final_list.append(row)
                
            elif name[0] in name_list[-1] and name[1] == "exon":
                row[2] = ""
                final_list.append(row)

        else: # we don't need introns 
            pass

    # for row in final_list: # check row above and row below for adding extra row

        # index_row = final_list.index(row) # translatable is not unique

        # for index_row in range(0, (len(final_list)-3)):

            # if final_list[index_row-1] [2] == "" and final_list[index_row+1] [2] == "gene":
                # final_list.insert(index_row, ["", "","","product",name_list[index_row]])
                # final_list.insert(index_row+1, ["", "", "", "transl_table", "11"])
            
            # elif final_list[index_row-1] [3] == "product":
                # final_list.insert(index_row+1, ["", "", "", "transl_table", "11"])

            # elif index_row >= len(final_list):
                # pass

# output: a CSV with species name as header, and everything else in the five column format

with open('Genbank_5Column_Anomodon.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(["> Feature Anomodon", "", "", "", ""])
    for row in final_list:
        spamwriter.writerow(row)
    
