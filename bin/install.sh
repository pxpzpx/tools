#!/bin/sh
echo "Append config .vimrc"
echo "source $HOME/tools/env/.vimrc" >> $HOME/.vimrc

echo "Append config tools.sh"
echo "source $HOME/tools/bin/tools.sh" >> $HOME/.bashrc

echo "Downloading... Vundle"
git clone https://github.com/gmarik/Vundle.vim.git $HOME/.vim/bundle/Vundle.vim

echo "Downloading... solarized color scheme for vim"
git clone git://github.com/altercation/vim-colors-solarized.git $HOME/.vim/colors/vim-colors-solarized
cp $HOME/.vim/colors/vim-colors-solarized/colors/solarized.vim $HOME/.vim/colors/solarized.vim
rm -rf $HOME/.vim/colors/vim-colors-solarized

echo "Downloading... molokai color scheme for vim"
git clone https://github.com/tomasr/molokai.git $HOME/.vim/colors/molokai
cp $HOME/.vim/colors/molokai/colors/molokai.vim $HOME/.vim/colors/molokai.vim
rm -rf $HOME/.vim/colors/molokai

echo "Install Vundle Plugins"
vim -c :PluginInstall -c :qa

MType=`uname`
if [[ "$MType"  = *"CYGWIN"* ]]
then
    echo "Cygwin System"
    echo "Downloading... Global Win32 Version"
    mkdir -p $HOME/tools/bin/global
    git clone https://github.com/jjangun/GLOBAL_Win32.git $HOME/tools/bin/global
else
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
fi

echo "Completed!"
