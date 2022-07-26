## CF-contest-parser

python client for codeforces contest parser

## Usage
```bash
git clone https://github.com/saurabh10041998/cf-contest-parser.git
export PATH=$PATH:<path-to-cf-contest-parser folder>
```
Suppose you want to parse problem under ~/Documents directory
```bash
cd ~/Documents
prepare.sh <contest_no> <problem_code>
```
For example
```bash
cd ~/Documents
prepare.sh 1691 a
```

This will parse the problem a of contest 1691 and will put input and output test cases file under `$(pwd)/cf/contest/1691/a`

## Important Note:
Update: **26/07/2022**
Looks like codeforces has removed their regular AES cipher check. So original <a href="https://github.com/xalanq/cf-tool">cf tool</a> will work.
But I am keeping this project in case they decide to add the support back.


