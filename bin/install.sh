#!/bin/sh
echo "Append config .vimrc"
echo "source ~/tools/env/.vimrc" >> ~/.vimrc

echo "Append config tools.sh"
echo "source ~/tools/bin/tools.sh" >> ~/.bashrc

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

echo "Install gnu global"
global_version="global-6.5"
global_archive=$global_version".tar.gz"
global_down_url="http://ftp.gnu.org/gnu/global/"$global_archive

mkdir -p $HOME/tools/bin/global
wget $global_down_url -P $HOME
tar xvzf $global_archive -C $HOME

cd $HOME/$global_version
./configure --prefix=$HOME/tools/bin/global
make
make install

echo "Remove install files"
rm -rf $HOME/$global_archive
rm -rf $HOME/$global_version

echo "global install done"

echo "Reload .bashrc"
source ~/.bashrc

echo "Completed!"
