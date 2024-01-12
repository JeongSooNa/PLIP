# Linux Basic

### path setting
- python script 혹은 bash script 사용 시 경로에 따른 에러가 많이 발생하기 때문에 사전에 input file 혹은 필요한 패키지, script 들의 경로를 미리 setting 해 놓는 것이 중요하다.
```sh
# 최상위 디렉토리
/

# 현재경로
./

# 상위 디렉토리
../

# 절대경로 : 최상위 경로를 기준으로 위치 작성
/workflow/my_directory/data

# 상대경로 : 현재 위치를 기준으로 위치 작성
my_directory/data
./my_directory/data
```

### basic command
```sh
# 현재 경로
pwd

# 현재 경로의 파일 및 폴더 확인
ll # 파일, 폴더들의 최종 편집 일시, 권한, 용량등까지 표기
ls # 파일, 폴더들의 이름만 표기

# 해당 경로의 파일 및 폴더 확인
ll my_directory
ls my_directory

# 해당 위치로 이동
cd my_directory

# 폴더 생성
mkdir my_directory

# 파이썬 script 실행
python py_script.py

# bash script 실행
bash sh_script.sh

# 파일의 내용 출력
cat my_file.txt

# 최근 사용 command 출력
history

# 출력되는 내용 중 원하는 단어를 포함하는 라인만 출력
cat my_file.txt | grep "want"
cat my_file.txt | grep -c "want" # grep한 라인의 수
```

### Vi 편집기
- vim 편집기로 linux 내에서 파일을 편집하는데에 사용
- insert mode, command mode를 확인하고 사용할 것
    insert mode : Ctrl+A 로 커서위치 끝라인에 입력
    command mode : Esc 후 command 입력
```
# 편집기 나가기
:q

# 편집기 저장 후 나가기
:wq

# 저장하지 않고 강제로 편집기 나가기
:q!

# 라인 넘버 표기
:set nu
```