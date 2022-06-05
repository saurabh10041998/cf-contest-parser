#! /usr/bin/python3
import requests
import subprocess
import re
import pdb
from bs4 import BeautifulSoup
import sys
import logging
import os

INPUT = 0
OUTPUT = 1
SCRIPT_PATH = ""

try:
    if os.environ['SCRIPT_PATH']:
        SCRIPT_PATH = os.environ['SCRIPT_PATH']
except KeyError:
        SCRIPT_PATH = ""
        logging.warning("\x1B[33mSCRIPT_PATH env not set, running in src dir\x1B[0m")

def getCipher():
    resp = requests.get("https://codeforces.com")
    raw_resp = resp.text
    c_tok = re.search("c=toNumbers\(\"(.*)\"\)", raw_resp).group(1)
    return c_tok

def getRCPC(cipher):
    js_script_path = os.path.join(SCRIPT_PATH, 'ape.js')
    output = subprocess.check_output(['node', js_script_path, cipher]).decode()
    token = re.search("RCPC=(.*)", output).group(1)
    return token


def parse_problem(contest_no, problem_code, cookies):
    url = f"https://codeforces.com/contest/{contest_no}/problem/{problem_code}"
    resp = requests.get(url, cookies=cookies)
    raw_resp = resp.text
    soup = BeautifulSoup(raw_resp, 'html.parser')
    ans = []
    for div in soup.findAll('div'):
        if div.get('class'):
            if div.get('class')[0] == 'sample-tests':
                ans.append(div)
    assert(len(ans) != 0)
    cases = ans[0].findAll('pre')
    input_cases = []
    output_cases = []
    for tc in cases:
        if tc.find_previous().text == "Input":
            input_cases.append(tc.text)
        elif tc.find_previous().text == "Output":
            output_cases.append(tc.text)
    input_cases = [x.lstrip("\n").rstrip("\n") for x in input_cases]
    output_cases = [x.lstrip("\n").rstrip("\n") for x in output_cases]
    return [*zip(input_cases, output_cases)]

cipher = getCipher()
rcpc_token = getRCPC(cipher).split(";")[0]
cookies = {"RCPC": rcpc_token}
assert(len(sys.argv) > 1)
contest_no = int(sys.argv[1])
problem_code = sys.argv[2].upper()
testcases = parse_problem(contest_no, problem_code, cookies)
## write test cases to file
for idx, tc in enumerate(testcases):
    with open(f"in{idx + 1}.txt", 'w') as f:
        f.writelines(tc[INPUT])
    with open(f"ans{idx + 1}.txt", "w") as f:
        f.writelines(tc[OUTPUT])
