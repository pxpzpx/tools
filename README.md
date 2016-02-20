# tools
=======

Description
-----------
tools is the simple installation of vim configs.
It provides pre-settings for vim, bashrc, etc.

How to Install tools?
-----------
git clone https://github.com/jjangun/tools.git ~/tools

sh ~/tools/bin/install.sh

Please check bellow comment if you use cygwin.
-----------
You just need to install clang binary in Cygwin setup.exe.
And then modify these lines like bellow in .vim/bundle/YouCompleteMe/third_party/ycmd/build.py

BEFORE Modify:
def GetCmakeArgs( parsed_args ):
  cmake_args = []
  if parsed_args.clang_completer or parsed_args.all_completers:
    cmake_args.append( '-DUSE_CLANG_COMPLETER=ON' )

  if parsed_args.system_libclang:
    cmake_args.append( '-DUSE_SYSTEM_LIBCLANG=ON' )

  if parsed_args.system_boost:
    cmake_args.append( '-DUSE_SYSTEM_BOOST=ON' )

  extra_cmake_args = os.environ.get( 'EXTRA_CMAKE_ARGS', '' )
  # We use shlex split to properly parse quoted CMake arguments.
  cmake_args.extend( shlex.split( extra_cmake_args ) )
  return cmake_args

AFTER Modify:
def GetCmakeArgs( parsed_args ):
  cmake_args = ['-DEXTERNAL_LIBCLANG_PATH=/usr/lib/libclang.dll.a']
  if parsed_args.clang_completer or parsed_args.all_completers:
    cmake_args.append( '-DUSE_CLANG_COMPLETER=ON' )

  if parsed_args.system_libclang:
    cmake_args.append( '-DUSE_SYSTEM_LIBCLANG=ON' )

  if parsed_args.system_boost:
    cmake_args.append( '-DUSE_SYSTEM_BOOST=ON' )

  extra_cmake_args = os.environ.get( 'EXTRA_CMAKE_ARGS', '' )
  # We use shlex split to properly parse quoted CMake arguments.
  cmake_args.extend( shlex.split( extra_cmake_args ) )
  return cmake_args

Then run these command line.

    cd ~/.vim/bundle/YouCompleteMe
    ./install.sh --clang-completer
