#!/bin/bash

# setup script to install texlive and add to path
texlive_year="2020"

sudo apt-get -qq update
export PATH=/tmp/texlive/bin/x86_64-linux:$PATH

if ! command -v lualatex > /dev/null; then
    echo "Texlive not installed"
    echo "Downloading texlive and installing"
    curl -L http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | tar xz
    echo I | TEXLIVE_INSTALL_PREFIX=~/tmp/texlive ./install-tl-*/install-tl
    echo "Finished install TexLive"
fi

echo "Now updating TexLive"
# update texlive
tlmgr option -- autobackup 0
tlmgr update --self --all --no-auto-install

echo "Finished updating TexLive"
