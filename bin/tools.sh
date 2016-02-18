#/bin/bash
MType=`uname`
if [[ "$MType"  = *"CYGWIN"* ]]
then
    export PATH+=:$HOME/tools/bin:$HOME/tools/bin/global/bin
else
    export PATH+=:$HOME/tools/bin:$HOME/tools/bin/global/bin
fi

# sources {{{
source acd_func.sh
# }}}

# aliases {{{
alias cd..='cd ..'
# }}}

# powerline {{{
if [ -f /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh ]; then
    source /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh
fi
# }}}

# etc {{{
export TERM='xterm-256color'
# }}}
