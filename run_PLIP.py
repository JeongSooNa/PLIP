### run PLIP script
### JeongSoo Na
### Create At : 2023.07.20
### Update At : 2023.07.25
### Docker Command : sudo docker run --rm     -v ${PWD}:/results     -w /results     -u $(id -u ${USER}):$(id -g ${USER})     pharmai/plip:latest -f 4001.pdb -yv -o PLIP_dir/output/raw/1/ -x -t -y -p
### Input Directory : /STG24-1/smyoon/nnmt/polarisqb_md/get_contacts/
### sudo python run_PLIP.py 1

import os
import sys
import math
import time
import shutil


# check time
start = time.time()


#
set_num = sys.argv[1]
o_dir = "/STG24-1/jsna/"
i_dir = "/STG24-1/smyoon/nnmt/polarisqb_md/get_contacts/"


try:
	if not os.path.exists(o_dir + set_num):
		os.makedirs(o_dir + set_num)
except OSError:
	print("Error: Failed to create the directory.")

#os.system("sudo docker run --rm     -v ${PWD}:/results     -w /results     -u $(id -u ${USER}):$(id -g ${USER})     pharmai/plip:latest -f 4031.pdb -yv -o PLIP_dir/output/raw/1/ -x -t -y -p")

for i in range(4001,5001):
	if not os.path.exists(o_dir + set_num + "/" + str(i)):
		os.makedirs(o_dir + set_num + "/" + str(i))
	shutil.copy(i_dir + set_num + "/"  + str(i) + ".pdb", "./" + str(i) + ".pdb")
	os.system("sudo docker run --rm     -v ${PWD}:/results     -w /results     -u $(id -u ${USER}):$(id -g ${USER})     pharmai/plip:latest -f " + str(i) +".pdb -yv -o " + o_dir + set_num + "/" + str(i) + "/ -x -t -y -p")
	os.remove(str(i) + ".pdb")


end = time.time()
print("Required Time : " , end - start)
print("Done")
