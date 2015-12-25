#!/usr/bin/python3
import subprocess

import os
import os.path
#prerequisite
# wget
# unzip
# gnu global 

g_strHOME= os.environ['HOME']
g_strMYBIN = g_strHOME+'/my_bin'
g_strVIM_SETTING=g_strHOME+'/.vim'


g_strBASHRC_filename=g_strHOME+'/.bashrc'
g_strBashrc_script = """
# _:x:_ Add Script for the dev. environment
export PATH+=:$HOME/my_bin:$HOME/my_bin/global/bin
export MWPATH=$HOME/work/TEST_PRJ
export MWPATH_ROOT=$MWPATH
alias ls='ls -hF --color=tty'    # classify Files in colour
alias vi='vim'
export LS_COLORS='di=01;94' # 짙은 파랑으로 나오는 디렉토리 표시를 밝은 파랑으로
export GTAGSROOT=$MWPATH
export GTAGSDBPATH=$MWPATH
            """
g_strBashrc_writemode ='a' # :x: add the script in the end of .bashrc file


g_strMW_filename=g_strMYBIN+'/mw'
g_strMW_script= """
# _:x:_ Add Script for the dev. environment
echo "Now MW_PATH is " $PWD
awk -F= '{if ($1 ~/export MWPATH$/) {"echo $PWD"|getline curr_dir ;  print $1"=" curr_dir; }  else { print $0;}  }' ~/.bashrc > ~/.tmpoutput
cp ~/.tmpoutput ~/.bashrc
rm ~/.tmpoutput
source ~/.bashrc
echo "Make GTAGS"
cd $MWPATH && gtags && cd -
echo "Make GTAGS Done"

"""
g_strMW_writemode ='w' # :x: write new script for mw file

g_strMdb_files_filename =g_strMYBIN+'/_mdb_files.sh'
g_strMdb_files_script ="""
#!/bin/sh
find ${MWPATH}/ -name '*.[ch]' -o -name '*.cpp' -o -name '*.cc' -not -name '.svn' > ${MWPATH}/tmp_db_files.out
mv ${MWPATH}/tmp_db_files.out ${MWPATH}/db_files.out
"""
g_strMdb_files_writemode='w'

g_strMdb_ctags_filename =g_strMYBIN+'/_mdb_ctags.sh'
g_strMdb_ctags_script ="""
#!/bin/sh
_TMP_DB_FILES_NAME=tmp_db_ctags_`date '+%0k_%0M_%0S_%0N'`.out
ctags -L ${MWPATH}/db_files.out -f ${MWPATH}/${_TMP_DB_FILES_NAME} -b
mv ${MWPATH}/${_TMP_DB_FILES_NAME} ${MWPATH}/tags
"""
g_strMdb_ctags_writemode='w'



g_strVIMRC_filename=g_strHOME+"/.vimrc"
g_strVIMRC_script = """
set autoindent
set nu
set enc=UTF-8
set fencs=usc-bom,utf-8,euc-kr,cp949
set bs=2
"syntax 설정
syntax enable
"ctags 설정
set tags=$MWPATH/tags
"tab 설정
set tabstop=2
set et
set ts=4 sw=4 sts=4
set background=dark
"마우스
"set mouse=a
"탐색결과 하이라이트
set hlsearch
"탐색시 대소문자 무시
set ignorecase
 
"Tag list 설정
let Tlist_WinWidth = 40
filetype on "이것이 없으면 Taglist동작하지 않음
"set makeprg=$MWPATH_ROOT/makefile
 
"Tag bar 설정
let g:tagbar_left = 1 "왼쪽으로 배치
 
 
"NERD tree설정
let NERDTreeWinSize = "40"
let NERDTreeWinPos ="right"
"let NERDTreeWinPos ="left"
 
"주요단축키
nmap [1 <Insert><Insert>printf("\\033[1;32m[%s][%d] :x: chk \\033[m\\n",__FUNCTION__,__LINE__);<CR><C-C>
nmap [2 <Insert><Insert>printf("\\033[1;33m[%s][%d] :x: chk \\033[m\\n",__FUNCTION__,__LINE__);<CR><C-C>
nmap [3 <Insert><Insert>printf("\\033[1;36m[%s][%d] :x: chk \\033[m\\n",__FUNCTION__,__LINE__);<CR><C-C>
nmap [4 a/* :x: projectname_myname<C-R>=strftime("%Y%m%d")<CR>_*/<C-C>
nmap [5 :Gtags -r<SPACE><cword>
nmap [6 <Insert><Insert>#if 0 // :x: for test<CR>#endif // :x: for test<CR><C-C>
 
"ctags/cscope관련 단축키
nmap [7 :!~/my_bin/_mdb_files.sh &<CR><CR>
nmap [8 :!~/my_bin/_mdb_ctags.sh &<CR><CR>
nmap [0 :source ~/.vimrc<CR>:e!<CR>
nmap [- :source ~/.vimrc<CR>:UpdateTypesFileOnly<CR>
nmap [w :w<CR>:!~/my_bin/_mdb_ctags.sh &<CR><CR>
 
"gnu global 관련 단축키
nmap <C-\><C-]> :GtagsCursor<CR>


nmap <F2> :BufExplorer<CR>
"map <F3> :TlistToggle<CR>
"TagList보다 Tagbar가 좀 더 우수하다
map <F3> :TagbarToggle<CR>
map <F4> :NERDTreeToggle $PWD<CR>
map <F7> :Gtags<SPACE>
map <F8> :!bash<CR>
 
"Vim grep 설정
map <C-a> :noautocmd vimgrep <cword> `cat $MWPATH/db_files.out`



"highlight 색깔 변경
hi Comment term=NONE ctermfg=white guifg=#80a0ff gui=bold
hi Function term=bold ctermfg=Green guifg=#80a0ff gui=bold
"term 변경
set term=xterm
set t_Co=256
" gnu global 자동 갱신 설정
let Gtags_Auto_Update=1   
let Gtags_No_Auto_Jump=1
"""
g_strVIMRC_writemode ='w'



g_downloadtool='wget'
g_package_list = [
     # info, url,filename
    ["cvim.zip	6.1.1	2014-04-21","http://www.vim.org/scripts/download_script.php?src_id=21803","cvim.zip"],
    ["nerdtree.zip   4.2.0   2011-12-28","http://www.vim.org/scripts/download_script.php?src_id=17123","nerdtree.zip" ],
    ["tagbar.vmb 2.6.1   2014-01-23","http://www.vim.org/scripts/download_script.php?src_id=21362","tagbar.vmb" ],
    ["bufexplorer-7.4.6.zip  7.4.6   2014-11-04","http://www.vim.org/scripts/download_script.php?src_id=22601","bufexplorer-7.4.6.zip" ],
    ["DoxygenToolkit.vim 0.2.13  2010-10-16","http://www.vim.org/scripts/download_script.php?src_id=14064","DoxygenToolkit.vim" ],
    ["taghighlight_r2.1.4.zip    2.1.4   2011-12-15","http://www.vim.org/scripts/download_script.php?src_id=17066","taghighlight_r2.1.4.zip"],
]

def download_file(url,filename,target_dir):
    cmd = g_downloadtool + ' '+ url +' -O '+target_dir+'/'+filename
    output=subprocess.call (cmd, shell=True)    
    if output!=0:
        print('Error on downloading file;',filename)
        return False
    print('OK')
    return True

    

def download_packages():
    for item in g_package_list:
        print("Download ["+item[0]+"]") # package info
        
        if os.path.isfile(g_strVIM_SETTING+'/'+item[2]) == True:
            print("Already it has the file ; "+g_strVIM_SETTING+'/'+item[2])
            continue 
        if download_file(item[1],item[2],g_strVIM_SETTING) != True:
            print("error on ["+item[0]+"]")
            return False
        else:
            print("Download Done ["+item[0]+"]")
    return True
def install_packages():

    for item in g_package_list:
        cmd=""
        # check file type and install the plugin according to file type
        if item[2][-4:] =='.zip' :
            cmd="cd "+g_strVIM_SETTING+";"+"unzip "+g_strVIM_SETTING+"/"+item[2]+";cd -"
            print("zip!")
        elif item[2][-4:] =='.vmb' :
            cmd="cd "+g_strVIM_SETTING+";"+"vim -c \'so %\' -c \'q\' "+item[2]+";cd -"
            print("vmb")
        elif item[2][-4:] =='.vim' :
            cmd="cp "+g_strVIM_SETTING+"/"+item[2]+" "+g_strVIM_SETTING+"/plugin/"+item[2]
            print("vim")
        else:
            print("Error, cannot find the file type on package[",item[0],"]")
            return False
        output=subprocess.call (cmd, shell=True)    
        if output!=0:
            print('Error on install package;',item[0])
            return False
        print('OK')

    return True


##
# @brief check the directory if not exist make it
#
# @param targetPath[IN] the path to make
#
# @return True when it success
def check_directory_or_make(targetPath):
    print ('check',targetPath, 'directory')
    if os.path.isdir(targetPath) == False:
        if os.mkdir(targetPath) == False:
            return False
    else:
        print (targetPath,"is already exist")
    return True

def check_directories():
    # :x: The directories to check
    directories = [
        g_strMYBIN ,        # ~/my_bin
        g_strVIM_SETTING    # ~/.vim
        ]
    for item in directories :
        if check_directory_or_make(item) == False :
            print('Error on ',item)
            return False
    return True
def add_script(contents):
    writeFlag=False
    targetfilename = contents[0]
    scriptcontents = contents[1]
    writemode = contents[2]
    
    if writemode == 'a' and os.path.isfile(targetfilename) == True :
        # :x: to prevent rewriting same script
        f = open(targetfilename,'r')
        script = f.read()
        if script.find('# _:x:_ Add Script for the dev. environment') == -1 :
            writeFlag = True
        else :
            print("the script for "+targetfilename+" is already existed")
        f.close()
    elif writemode =='w' :
        writeFlag = True

    if writeFlag == True :
        f = open(targetfilename,writemode)
        f.write(scriptcontents)
        f.close()
    if writemode == 'w' :
        os.chmod(targetfilename,0o700)
    return True

def add_scripts():
    print('make additional script on .bashrc')

    scripts =[ #filename, script to write, write mode 'w'(write) 'a'(add)
               [g_strBASHRC_filename,g_strBashrc_script,g_strBashrc_writemode],
               [g_strMW_filename,g_strMW_script,g_strMW_writemode],
               [g_strMdb_files_filename,g_strMdb_files_script,g_strMdb_files_writemode],
               [g_strMdb_ctags_filename,g_strMdb_ctags_script,g_strMdb_ctags_writemode],
               [g_strVIMRC_filename,g_strVIMRC_script,g_strVIMRC_writemode],
            ]
    for item in scripts:
        if add_script(item) != True:
            return False
    return True
g_STR_global_compressed_name='global-6.5.tar.gz'

g_STR_global_URL= 'http://ftp.gnu.org/gnu/global/global-6.5.tar.gz'
def install_gnu_global():
    print('install GNU global ; ',g_STR_global_compressed_name)
    print('download the ',g_STR_global_compressed_name)

    if os.path.isfile('.'+'/'+g_STR_global_compressed_name) == True:
        print("Already it has the file ; "+g_strVIM_SETTING+'/'+g_STR_global_compressed_name)
    else :
        if download_file(g_STR_global_URL,g_STR_global_compressed_name,'.') == False :
            print('download error!')
            return False
    print('extract ',g_STR_global_compressed_name)
    cmd = 'tar xf ' +g_STR_global_compressed_name
    output=subprocess.call (cmd, shell=True)    
    if output!=0:
        print('Error on extract file;',g_STR_global_compressed_name)
        return False
    print('build GNU global and install on ~/my_bin/global')



    cmd = 'mkdir ~/my_bin/global ' 
    output=subprocess.call (cmd, shell=True)    
    if output!=0:
        print('Error on make directory ~/my_bin/global;')



    cmd = 'cd global-6.5 && ./configure --prefix=$HOME/my_bin/global && make && make install'
    output=subprocess.call (cmd, shell=True)    
    if output!=0:
        print('Error on installation')
        return False
    print('copy vim plugin for gnu global')
    cmd = 'cp ~/my_bin/global/share/gtags/gtags.vim ~/.vim/plugin'
    output=subprocess.call (cmd, shell=True)    
    if output!=0:
        print('Error on extract file;',g_STR_global_compressed_name)
        return False
    
    print('clean up gnu global files')
    cmd = 'rm ' +g_STR_global_compressed_name+ ' && rm -rf global-6.5'
    output=subprocess.call (cmd, shell=True)    
    if output!=0:
        print('Error on cleanup files')
        return False


    print('GNU global installation done')
    return True

def main():
    nPhase =0
    print ("Development Environment setting is now start")
    print ("2015.08.04 by windheim")
    nPhase+=1
    print ("Phase #",nPhase," ; Check the base directories")
    if check_directories() == False :
        print ("Error on Phase #",nPhase)
        return False

    nPhase+=1
    print ("Phase #",nPhase," ; Download vim plugins")
    if download_packages() == False :
        print("Error on Phase #",nPhase)
        return False
    nPhase+=1
    print ("Phase #",nPhase," ; Install vim plugins")
    if install_packages() == False :
        print("Error on Phase #",nPhase)
        return False
    
    nPhase+=1
    print ("Phase #",nPhase," ; Make additional scripts(.bashrc,.vimrc)")
    if add_scripts() == False :
        print("Error on Phase #",nPhase)
        return False
    nPhase+=1
    print ("Phase #",nPhase," ; install GNU global manually")
    if install_gnu_global() == False :
        print("Error on Phase #",nPhase)
        return False
    



    return True
if __name__ == '__main__':
    main()
