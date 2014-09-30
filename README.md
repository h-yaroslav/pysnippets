h2. pysnippets

Useful python code snippets


h2. This README contains commands that were executed on the hosting

# Generate RSA key (without password) to be installed on Github
$ ssh-keygen.exe -t rsa -C "h.yaroslav@gmail.com"
# Add `id_rsa.pub` key to the "SSH Keys" on the https://github.com/settings/ssh page
# to be able to do ssh login by public key
$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAABBBBCCCxD+9x9bp h.yaroslav@gmail.com
# Test everything works !!!
$ ssh -T git@github.com
Hi h-yaroslav! You've successfully authenticated, but GitHub does not provide shell access.

# Tune GIT user on this machine
$ git config --global user.name "Rivnefish"
$ git config --global user.email "rivnefish@gmail.com"
# Clone ttp/rivnefish repo
$ cd
$ mkdir projects
$ cd ~/projects/
$ git clone git@github.com:h-yaroslav/pysnippets.git
# Sync latest changes
$ git pull

