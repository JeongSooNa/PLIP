### Get PLIP Interaction Information csv file
### JeongSoo Na
### 2023.07.26

### Needs Column
### H-BOND : RESNR | RESTYPE | RESNR_LIG | SIDECHAIN | DIST_H-A | DIST_D-A | DON_ANGLE | PROTISDON | DONORTYPE | ACCEPTOORTYPE
### pi-STACK : RESNR | RESTYPE | RESNR_LIG | CENTDIST | ANGLE | TYPE | LIG_IND_LIST

import os

f = open('/lwork01/jsna/list' , 'r')
raw = f.read()
list = raw.split('\n')
list.remove('')
len = len(list)
f.close()

# Hydrogen Bond Column
h_list = ["RESNR","RESTYPE","RESCHAIN","RESNR_LIG","RESTYPE_LIG","RESCHAIN_LIG","SIDECHAIN","DIST_H-A","DIST_D-A","DON_ANGLE","PROTISDON","DONORIDX","DONORTYPE","ACCEPTORIDX","ACCEPTORTYPE","LIGCOO","PROTCOO"]
h_list_header = '| RESNR | RESTYPE | RESCHAIN | RESNR_LIG | RESTYPE_LIG | RESCHAIN_LIG | SIDECHAIN | DIST_H-A | DIST_D-A | DON_ANGLE | PROTISDON | DONORIDX | DONORTYPE | ACCEPTORIDX | ACCEPTORTYPE | LIGCOO                 | PROTCOO                | \n+=======+=========+==========+===========+=============+==============+===========+==========+==========+===========+===========+==========+===========+=============+==============+========================+========================+'
#pi-Stacking Column
p_list = ["RESNR","RESTYPE","RESCHAIN","RESNR_LIG","RESTYPE_LIG","RESCHAIN_LIG","PROT_IDX_LIST","CENTDIST","ANGLE","OFFSET","TYPE","LIG_IDX_LIST","LIGCOO","PROTCOO"]
p_list_header_2 = '| RESNR | RESTYPE | RESCHAIN | RESNR_LIG | RESTYPE_LIG | RESCHAIN_LIG | PROT_IDX_LIST                 | CENTDIST | ANGLE | OFFSET | TYPE | LIG_IDX_LIST                  | LIGCOO                 | PROTCOO                | \n+=======+=========+==========+===========+=============+==============+===============================+==========+=======+========+======+===============================+========================+========================+'
p_list_header_1 = '| RESNR | RESTYPE | RESCHAIN | RESNR_LIG | RESTYPE_LIG | RESCHAIN_LIG | PROT_IDX_LIST                 | CENTDIST | ANGLE | OFFSET | TYPE | LIG_IDX_LIST             | LIGCOO                 | PROTCOO                | \n+=======+=========+==========+===========+=============+==============+===============================+==========+=======+========+======+==========================+========================+========================+'

h = open("resert_hydrogen_bond.csv","w")
h.write("No,PDB_Name,Interaction_type,RESNR,RESTYPE,RESCHAIN,RESNR_LIG,RESTYPE_LIG,RESCHAIN_LIG,SIDECHAIN,DIST_H-A,DIST_D-A,DON_ANGLE\n")

p = open("resert_pi_stacking.csv","w")
p.write("No,PDB_Name,Interaction_type,RESNR,RESTYPE,RESCHAIN,RESNR_LIG,RESTYPE_LIG,RESCHAIN_LIG,PROT_IDX_LIST,CENTDIST,ANGLE,OFFSET,TYPE")

no_1 = 1
no_2 = 1

for i in list:
	for j in range(4001,5001):
		f = open('/STG24-1/jsna/' + str(i) + '/' + str(j) + '/report.txt')
		text = f.read()
		if 'LIG:A:264 (LIG) - SMALLMOLECULE' in text:
			text = text.split('LIG:A:264 (LIG) - SMALLMOLECULE')[1]
			### Get Hydrogen Bonds
			if '**Hydrogen Bonds**' in text:
				text_h = text.split(h_list_header)[1].split('+-------+---------+----------+-----------+-------------+--------------+-----------+----------+----------+-----------+-----------+----------+-----------+-------------+--------------+------------------------+------------------------+\n\n')[0]
				text_i = text_h.split("\n+-------+---------+----------+-----------+-------------+--------------+-----------+----------+----------+-----------+-----------+----------+-----------+-------------+--------------+------------------------+------------------------+")
				for k in text_i:
					text_list = k.split("|")
					del text_list[0]
					del text_list[17]
					for l in range(0,17):
						text_list[l] = text_list[l].replace(" ","")
					print(text_list)
					h.write(str(no_1) + "," + str(i) + "-" + str(j) + ".pdb,Hydrogen Bonds," + text_list[0] + "," + text_list[1] + "," + text_list[2] + "," + text_list[3] + "," + text_list[4] + "," + text_list[5] + "," + text_list[6] + "," + text_list[7] + "," + text_list[8] + "," + text_list[9] + "\n")
				no_1 = no_1 + 1
			### Get pi-Stacking
			if '**pi-Stacking**\n+-------+---------+----------+-----------+-------------+--------------+-------------------------------+----------+-------+--------+------+--------------------------+------------------------+------------------------+' in text:
				text_p = text.split(p_list_header_1)[1].split('+-------+---------+----------+-----------+-------------+--------------+-------------------------------+----------+-------+--------+------+--------------------------+------------------------+------------------------+\n\n')[0]
                                text_i = text_p.split("\n+-------+---------+----------+-----------+-------------+--------------+-------------------------------+----------+-------+--------+------+--------------------------+------------------------+------------------------+")
                                for k in text_i:
                                        text_list = k.split("|")
                                        del text_list[0]
                                        del text_list[13]
                                        for l in range(0,13):
                                                text_list[l] = text_list[l].replace(" ","")
						if(l==6):
							text_list[l] = text_list[l].replace(",","/")
                                        print(text_list)
                                        p.write(str(no_2) + "," + str(i) + "-" + str(j) + ".pdb,Hydrogen Bonds," + text_list[0] + "," + text_list[1] + "," + text_list[2] + "," + text_list[3] + "," + text_list[4] + "," + text_list[5] + "," + text_list[6] + "," + text_list[7] + "," + text_list[8] + "," + text_list[9] + "," + text_list[10] + "\n")
                                no_2 = no_2 + 1
			if '**pi-Stacking**\n+-------+---------+----------+-----------+-------------+--------------+-------------------------------+----------+-------+--------+------+-------------------------------+------------------------+------------------------+' in text:
                                text_p = text.split(p_list_header_2)[1].split('+-------+---------+----------+-----------+-------------+--------------+-------------------------------+----------+-------+--------+------+-------------------------------+------------------------+------------------------+\n\n')[0]
                                text_i = text_p.split("\n+-------+---------+----------+-----------+-------------+--------------+-------------------------------+----------+-------+--------+------+-------------------------------+------------------------+------------------------+")
                                for k in text_i:
                                        text_list = k.split("|")
                                        del text_list[0]
                                        del text_list[13]
                                        for l in range(0,13):
                                                text_list[l] = text_list[l].replace(" ","")
                                                if(l==6):
                                                        text_list[l] = text_list[l].replace(",","/")
                                        print(text_list)
                                        p.write(str(no_2) + "," + str(i) + "-" + str(j) + ".pdb,Hydrogen Bonds," + text_list[0] + "," + text_list[1] + "," + text_list[2] + "," + text_list[3] + "," + text_list[4] + "," + text_list[5] + "," + text_list[6] + "," + text_list[7] + "," + text_list[8] + "," + text_list[9] + "," + text_list[10] + "\n")
                                no_2 = no_2 + 1
		else:
			print("There is no ligand information.")
	
h.close()
p.close()
