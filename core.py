import subprocess

result =  -1
while result < 0:
    result = subprocess.run(["python", "./funsearch_official_code/funsearch.py"], capture_output=True, text=True)
    print(result)

