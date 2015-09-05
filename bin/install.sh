#!/bin/sh

echo "Append config .vimrc"
echo "source ~/tools/env/.vimrc" >> ~/.vimrc

echo "Append config tools.sh"
echo "source ~/tools/bin/tools.sh" >> ~/.bashrc

echo "Reload .bashrc"
source ~/.bashrc

echo "Downloading... Vundle"
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

echo "Downloading... color scheme for vim"
git clone https://github.com/tomasr/molokai.git ~/.vim/colors/molokai.git
cp ~/.vim/colors/molokai.git/colors/molokai.vim ~/.vim/colors/molokai.vim
rm -rf ~/.vim/colors/molokai.git

echo "Install Vundle Plugins"
vim -c :PluginInstall -c :qa

echo "Completed!"
