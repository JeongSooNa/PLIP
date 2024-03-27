### Get PLIP Report
### Get csv file from output report.txt
### JeongSoo Na
### Create At : 2024.01.17
### Update At : 2024.03.27

### Import Packages
import os
import argparse

### Command
'''get_PLIP.py --input_dir '''

### Arguments
parser = argparse.ArgumentParser(prog="python get_PLIP_csv.py", add_help=True)
parser.add_argument("-i","--input_dir")
parser.add_argument("-o","--output")
args = parser.parse_args()

# pdb list
list = os.listdir(args.input_dir)

# Write output.csv
out = open(args.output,"w")
out.write("pdb,interaction,res_no,res_type,res_chain,lig_no,lig_type,lig_chain,distance\n")

for i in list:
    # Read each report
    f = open(args.input_dir + i + "/report.txt","r")
    data = f.read()
    data_list = data.split("\n**")
    
    # pdb name
    pdb = i
    
    # data each lines in report
    for j in range(1,len(data_list)):
        tmp = data_list[j].split("\n")
        
        # interaction
        interaction = tmp[0].replace("**","")
        
        # report files dividing line
        line_1 = tmp[1]
        line_2 = tmp[1].replace("-","=")
        
        # raw data list : only value & '|'
        raw_data = data_list[j].split(line_2 + "\n")[1]
        raw_data_list = raw_data.split("\n" + line_1 + "\n\n")[0].split("\n" + line_1 + "\n")
        for k in raw_data_list:
            raw = k.split("|")
            
            # Write data
            # replace to raw[_].strip() - using Copilot
            res_no = raw[1].replace(" ","")
            res_type = raw[2].replace(" ","")
            res_chain = raw[3].replace(" ","")
            lig_no = raw[4].replace(" ","")
            lig_type = raw[5].replace(" ","")
            lig_chain = raw[6].replace(" ","")
            dist = raw[7].replace(" ","")
            
            # replace each specific column data
            if interaction == "Hydrogen Bonds":
                dist = raw[8].replace(" ","")
            if interaction == "Salt Bridges":
                lig_no = raw[5].replace(" ","")
                lig_type = raw[6].replace(" ","")
                lig_chain = raw[7].replace(" ","")
                dist = raw[8].replace(" ","")
            if interaction == "pi-Stacking":
                dist = raw[8].replace(" ","")
            if interaction == "pi-Cation Interactions":
                lig_no = raw[5].replace(" ","")
                lig_type = raw[6].replace(" ","")
                lig_chain = raw[7].replace(" ","")
                dist = raw[8].replace(" ","")
                
            #csv
            out.write(pdb + ","\
                    + interaction + ","\
                    + res_no + ","\
                    + res_type + ","\
                    + res_chain + ","\
                    + lig_no + ","\
                    + lig_type + ","\
                    + lig_chain + ","\
                    + dist + "\n")
            
    f.close()
    
out.close()