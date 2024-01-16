### Get PLIP Report
### Get csv file from output report.txt
### JeongSoo Na
### 2024.01.17

### Packages import
import os

### 현재 경로 선언
### python script를 실행하는 중 os.chdir()을 통해 경로 이동이 이뤄질 경우 절대 경로를 사용하지 않거나 위치에 의한 에러가 발생할 경우를 대비해 현재 경로를 선언해놓는다.
current_path = os.getcwd()

### report 상위 폴더(각 plip 결과)들을 모아놓은 파일 위치
### 다음과 같이 경로 구성이 될 수 있도록 PLIP 돌릴 시 조정
### input_dir / 각 output 폴더 / report.txt
input_dir = "/lwork01/jeheo/data"

### report.txt 가 들어있는 각 폴더 list 선언
input_list = os.listdir(input_dir)
### list 갯수
print("pdb number : " + str(len(input_list)))

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

### csv file 생성
f = open("plip_report.csv","w")
### csv file의 header 입력
### PDB이름, 위 주석과 같은 결합타입, 결합 위치 sequence number, 결합 위치 Amino-Acid sequence
### Hydrogen Bonds의 경우 DIST가 H-A, D-A 두 개가 있기 때문에 DIST를 두개로 분리
f.write("PDB,Interaction_type,RESNR,RESTYPE,DIST,DIST_sub\n")

### csv file 작성을 위해 각 report.txt에 접근
for i in range(0,len(input_list)):
    r = open(input_dir + "/" + input_list[i] + "/report.txt")
    report = r.read()

    # Hydrophobic Interactions
    ### 해당 interaction이 있을 경우 실행
    if "**Hydrophobic Interactions**" in report:
        ### 해당 interaction이 report.txt 내에 여러 개 있을 경우 모두 추출하기 위해 실행
        l = len(report.split("**Hydrophobic Interactions**\n"))

        for j in range(1,l):
            ### report.txt 내의 표를 보고 이해 필요
            ### tmp : 표의 첫 줄인 "+-------+---------+----------+-----------+"에서 "+" 사이의 "-" 들을 담은 list
            ### report 별로 테이블의 크기가 다를 수 있으므로 길이를 파악하고 데이터를 추출하는 작업 필요
            tmp = report.split("**Hydrophobic Interactions**\n")[j].split("\n")[0].split("+")

            ### 추출한 테이블의 길이로 각 행이 들어있는 list(report_hi) 생성
            ### "| 639   | PRO     | A        | 0         | UNK         | Z            | 3.90 | 23           | 3854          | 10.080, 48.240, -0.776 | 11.952, 47.829, 2.621 |"
            ### 위와 같은 한 줄씩 list에 담겨있다.
            report_hi = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+")

            # print(len(report_hi))

            for k in range(0,len(report_hi)):
                ### 각 행에서 필요한 컬럼 추출
                RESNR = report_hi[k].split("|")[1].replace(" ","")
                RESTYPE = report_hi[k].split("|")[2].replace(" ","")
                DIST = report_hi[k].split("|")[7].replace(" ","")

                ### 추출한 데이터를 csv file에 입력
                f.write(input_list[i].replace(".pdb","") + ",Hydrophobic Interactions," + RESNR + "," + RESTYPE + "," + DIST + ",," + "\n")


    # Hydrogen Bonds
    if "**Hydrogen Bonds**" in report:
        l = len(report.split("**Hydrogen Bonds**\n"))
        for j in range(1,l):
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
        l = len(report.split("**Salt Bridges**\n"))
        for j in range(1,l):
            tmp = report.split("**Salt Bridges**\n")[j].split("\n")[0].split("+")
            report_sb = report.split("+" + tmp[1].replace("-","=") + "+" + tmp[2].replace("-","=") + "+" + tmp[3].replace("-","=") + "+" + tmp[4].replace("-","=") + "+" + tmp[5].replace("-","=") + "+" + tmp[6].replace("-","=") + "+" + tmp[7].replace("-","=") + "+" + tmp[8].replace("-","=") + "+" + tmp[9].replace("-","=") + "+" + tmp[10].replace("-","=") + "+" + tmp[11].replace("-","=") + "+" + tmp[12].replace("-","=") + "+" + tmp[13].replace("-","=") + "+\n")[1].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+" + "\n\n")[0].split("\n" + "+" + tmp[1] + "+" + tmp[2] + "+" + tmp[3] + "+" + tmp[4] + "+" + tmp[5] + "+" + tmp[6] + "+" + tmp[7] + "+" + tmp[8] + "+" + tmp[9] + "+" + tmp[10] + "+" + tmp[11] + "+" + tmp[12] + "+" + tmp[13] + "+")
            # print(len(report_sb))
            for k in range(0,len(report_sb)):
                RESNR = report_sb[k].split("|")[1].replace(" ","")
                RESTYPE = report_sb[k].split("|")[2].replace(" ","")
                DIST = report_sb[k].split("|")[8].replace(" ","")
                f.write(input_list[i].replace(".pdb","") + ",Salt Bridges," + RESNR + "," + RESTYPE + "," + DIST + ",," + "\n")

### csv writing 종료
f.close()

### 현재 경로로 복귀
os.chdir(current_path)