#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y zsh curl tmux zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev libffi-dev python3-pip python-pip zeal vlc vim

sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get install -y git gitk

# For AsciidocFX (pide confirmacion!)
sudo apt-get install -y ttf-mscorefonts-installer

sudo apt-get install -y graphviz
sudo apt-get install -y snmp


# pref
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r` logwatch tilix

# sudo apt-get install network-manager-openvpn 
sudo apt-get install network-manager-openvpn-gnome


sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

sudo apt-get install emacs25
sudo apt-get install p7zip-full p7zip-rar uget calibre sysstat iftop htop ack silversearcher-ag xchm cmake nmap portaudio19-dev ffmpeg

sudo apt-get install xclip


# dns cache
sudo apt-get install nscd
# cli command
sudo apt-get install tree

# disk analysis
sudo apt-get install smartmontools

sudo apt-get install inotify-tools

# pdf printer (The pdf printer provided by that package will "print" the resulting PDFs into the /home/[user]/PDF directory)
sudo apt-get install printer-driver-cups-pdf

sudo apt-get install rlwrap

sudo apt install resolvconf

# urlencode
sudo apt-get install gridsite-clients




# kvm
sudo apt install -y libvirt-bin
# Android
sudo adduser a kvm

sudo add-apt-repository ppa:alexx2000/doublecmd
sudo apt-get install -y doublecmd-gtk



sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt-get install -y wireshark

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository  "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update

sudo apt-get install docker-ce 
sudo usermod -aG docker $USER 
sudo systemctl enable docker 

# sudo apt-get install libgconf-2-4
