!#bin/bash

echo "***************************************"
echo "Loading..."
read -p "Do you want to know a secret about me? y/n" BRANCH
if [[ $BRANCH = "y" ]]; then
read -p "What's my name? (Yuan)" NAME
if [[ $NAME = "Yuan" ]]; then
echo "Yuan~~~~~"; fi
fi
echo "***************************************"
read -p "Please enter a number: " NUM1
echo "$NUM1 LiYuan(s)!"
read -p "Please enter another number: " NUM2
NUM3=$((NUM1+NUM2))
echo "$NUM1 + $NUM2 = $NUM3 Liyuan(s)!"
echo "$((NUM3))Yuan~~~~~~~~~~~"
echo "---------------------------------------"
echo "People can add more please."

