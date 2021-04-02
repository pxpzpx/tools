# tools
=======

Description
-----------
tools is the simple installation of vim configs.
It provides pre-settings for vim, bashrc, etc.

How to Install tools?
-----------
git clone https://github.com/pxpzpx/tools.git ~/tools

sh ~/tools/bin/install.sh

Please check bellow comment if you use linux (ubuntu base).
-----------
sudo apt-get install git vim build-essential cmake clang exuberant-ctags libncurses5-dev libncurses5 python-dev python3-dev python-pip python-setuptools

Please check bellow comment if you use cygwin.
-----------
You just need to install clang binary in Cygwin setup.exe.
And then modify these lines like bellow in .vim/bundle/YouCompleteMe/third_party/ycmd/build.py

Before modify:

    ...
    def GetCmakeArgs( parsed_args ):
      cmake_args = []
    ...

After modify:

    ...
    def GetCmakeArgs( parsed_args ):
      cmake_args = ['-DEXTERNAL_LIBCLANG_PATH=/usr/lib/libclang.dll.a']
    ...

Then run these command line.

    cd ~/.vim/bundle/YouCompleteMe
    ./install.py --clang-completer

YouCompleteMe unavailable: requires Vim 8.1.2269+. Error 시에 Go to youcompleteme directory

git checkout d98f896
git submodule update --init --recursive
./install.py
