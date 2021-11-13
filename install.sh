

echo "Installing Q game." 
echo "To play, open terminal and type newsom"
cwd=$(pwd)/gamePlay.py
chmod a+x install.sh

echo  "\nalias newsom='python3 $cwd'" >> ~/.zshrc
source ~/.zshrc



