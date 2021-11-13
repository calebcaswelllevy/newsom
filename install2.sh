#!/bin/zsh


echo "Installing Q game." 

mkdir /usr/local/bin/newsom
cp -R ./scripts /usr/local/bin/newsom




echo  "\nalias newsom='python3 /usr/local/bin/newsom/scripts/gamePlay.py'" >> ~/.zshrc
source ~/.zshrc



echo "To play, open terminal and type newsom"