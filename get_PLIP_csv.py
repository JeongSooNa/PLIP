### Get PLIP Report
### Get csv file from output report.txt
### JeongSoo Na
### 2024.01.03

### Packages import
import os
import sys

current_path = os.getcwd()

### parameter
### Input data : Directory include input pdb files
### Output directory : Directory saved PLIP output data and csv table
input_dir = sys.argv[1]
input_list = os.listdir(input_dir)
output_dir = sys.argv[2]
print("pdb number : " + str(len(input_list)))

# 안돼 이동
os.chdir(input_dir)

### Make directory per pdb
try:
    if not os.path.exists(output_dir):
        os.system("sudo mkdir " + output_dir)
except OSError:
    print("Error : Directory is already exists.")

for i in input_list:
    try:
        if not os.path.exists(i):
            os.system("sudo mkdir " + output_dir + "/" + i.replace(".pdb",""))
    except OSError:
        print("Error : Directory is already exists.")
    

### Run PLIP
### command : sudo docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f target.pdb -yv -o output_dir/ -x -t -y -p
for i in input_list:
    os.system("sudo docker run --rm -v ${PWD}:/results -w /results -u $(id -u ${USER}):$(id -g ${USER}) pharmai/plip:latest -f " + i + " -yv -o " + output_dir + "/" + i.replace(".pdb","") + "/ -x -t -y -p")

### Report to csv table
### Interactions
### - Hydrophobic Interaction
### - Hydrogen Bond
### - Water Bridges
### - pi-Stacking (parallel)
### - pi-Stacking (perpendicular)
### - pi-Cation Interaction
### - Halogen Bond
### - Salt Bridge
### - Metal Complex
f = open(output_dir + "/plip_value_table.csv")
f.write("PDB,Interaction_type,RESNR,RESTYPE,DIST,DIST_sub\n")
for i in range(0,len(input_list)):
# for i in range(0,1):
    r = open(output_dir + "/" + input_list[i].replace(".pdb","") + "/report.txt")
    report = r.read()
    
    # Hydrophobic Interactions
    if "**Hydrophobic Interactions**" in report:
        len = report.split("**Hydrophobic Interactions**\n")
        for j in range(1,len):
            tmp = report.split("**Hydrophobic Interactions**\n")[j].split("\n")[0].split("+")
            report_hi = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+")
            # print(len(report_hi))
            for k in range(0,len(report_hi)):
                RESNR = report_hi[k].split("|")[1].replace(" ","")
                RESTYPE = report_hi[k].split("|")[2].replace(" ","")
                DIST = report_hi[k].split("|")[7].replace(" ","")
                ### updating
                f.write(input_list[i].replace(".pdb","") + ",Hydrophobic Interactions," + RESNR + "," + RESTYPE + "," + DIST + ",," + "\n")
            
    
    # Hydrogen Bonds
    if "**Hydrogen Bonds**" in report:
        len = report.split("**Hydrogen Bonds**\n")
        for j in range(1,len):
            tmp = report.split("**Hydrogen Bonds**\n")[j].split("\n")[0].split("+")
            report_hb = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+" + tmp[12].replace("-","=") + "+" + tmp[13].replace("-","=") + "+" + tmp[14].replace("-","=") + "+" + tmp[15].replace("-","=") + "+" + tmp[16].replace("-","=") + "+" + tmp[17].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + tmp[14] + "+" + tmp[15] + "+" + tmp[16] + "+" + tmp[17] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + tmp[14] + "+" + tmp[15] + "+" + tmp[16] + "+" + tmp[17] + "+")
            # print(len(report_hb))
            for k in range(0,len(report_hb)):
                RESNR = report_hb[k].split("|")[1].replace(" ","")
                RESTYPE = report_hb[k].split("|")[2].replace(" ","")
                DIST = report_hb[k].split("|")[8].replace(" ","")
                DIST_sub = report_hb[k].split("|")[9].replace(" ","")
                f.write(input_list[i].replace(".pdb","") + ",Hydrogen Bonds," + RESNR + "," + RESTYPE + "," + DIST + "," + DIST_sub + "\n")
            
    
    
    # Salt Bridges
    if "**Salt Bridges**" in report:
        len = report.split("**Salt Bridges**\n")
        for j in range(1,len):
            tmp = report.split("**Salt Bridges**\n")[j].split("\n")[0].split("+")
            report_sb = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+" + tmp[12].replace("-","=") + "+" + tmp[13].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+")
            # print(len(report_sb))
            for k in range(0,len(report_sb)):
                RESNR = report_sb[k].split("|")[1].replace(" ","")
                RESTYPE = report_sb[k].split("|")[2].replace(" ","")
                DIST = report_sb[k].split("|")[8].replace(" ","")
                f.write(input_list[i].replace(".pdb","") + ",Salt Bridges," + RESNR + "," + RESTYPE + "," + DIST + ",," + "\n")

f.close()

### I will update the Calculation Process & Filtering System
### Update code clearly
### MIT License

os.chdir(current_path)