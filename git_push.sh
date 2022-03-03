# !/bin/sh

today=$(date "+%Y-%m-%d %H:%M:%S")
commit_msg="[update](${today}): auto commit and push"
echo $commit_msg
git pull origin master
git add -A
git commit -m "${commit_msg}"
git push origin master
echo "push code success"