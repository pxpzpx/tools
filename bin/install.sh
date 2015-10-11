#!/bin/sh

echo "Append config .vimrc"
echo "source ~/tools/env/.vimrc" >> ~/.vimrc

echo "Append config tools.sh"
echo "source ~/tools/bin/tools.sh" >> ~/.bashrc

echo "Reload .bashrc"
source ~/.bashrc

echo "Downloading... Vundle"
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

echo "Downloading... solarized color scheme for vim"
git clone git://github.com/altercation/vim-colors-solarized.git ~/.vim/colors/vim-colors-solarized
cp ~/.vim/colors/vim-colors-solarized/colors/solarized.vim ~/.vim/colors/solarized.vim
rm -rf ~/.vim/colors/vim-colors-solarized

echo "Downloading... molokai color scheme for vim"
git clone https://github.com/tomasr/molokai.git ~/.vim/colors/molokai
cp ~/.vim/colors/molokai/colors/molokai.vim ~/.vim/colors/molokai.vim
rm -rf ~/.vim/colors/molokai

echo "Install Vundle Plugins"
vim -c :PluginInstall -c :qa

echo "Completed!"
