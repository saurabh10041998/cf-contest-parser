#! /usr/bin/python3
import requests
import subprocess
import re
import pdb
from bs4 import BeautifulSoup

def getCipher():
    resp = requests.get("https://codeforces.com")
    raw_resp = resp.text
    c_tok = re.search("c=toNumbers\(\"(.*)\"\)", raw_resp).group(1)
    return c_tok

def getRCPC(cipher):
    output = subprocess.check_output(['node', 'ape.js', cipher]).decode()
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
    pdb.set_trace()


cipher = getCipher()
rcpc_token = getRCPC(cipher).split(";")[0]
cookies = {"RCPC": rcpc_token}

parse_problem(1691, "C", cookies)

