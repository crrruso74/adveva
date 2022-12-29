if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Zk-Bots/AutoFilter2.git /AutoFilter2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AutoFilter2
fi
cd /AutoFilter
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
