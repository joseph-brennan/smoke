#!/bin/bash

sudo apt-get update
sudo apt-get install -y curl python3 python3-pip python3-dev python python-pip python-dev

#python3 virtualenv wrapper setup
pip3 install --user virtualenvwrapper
VIRTUALENVWRAPPER_PYTHON=$(which python3)
PATH="$PATH:$HOME/.local/bin"
source $(which virtualenvwrapper.sh)

mkvirtualenv smoke-editor

# nvm/npm/yarn setup
mkdir -p $HOME/.nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm

nvm install 8.11.0
nvm alias default v8.11.0
nvm use default

npm install -g yarn
