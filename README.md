# Build BTRE Real Estate Project
The project will contain listing of properties along with the information of each property.
The search filter to search the properties according to the requirements.

## Syntax to follow for README file creation
[file] (https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)

## Set python environment variable

### All the commands are according to git bash window (may not work on command prompt)

## GIT Initialization
>git init

This command will initialize empty git repository

## Create .gitignore file
gitignore.io will lead you to file content we need to add to this file
Search django & vagrant and copy the content to .gitignore file
[.gitignore] (http://gitignore.io/)

## Create LICENSE file
[LICENSE] (https://choosealicense.com/licenses/mit/)

## Create ssh key
### Use git bash for following command after locating to your project directory
ssh-keygen -t rsa -b 4096 -C "akashdraut93@gmail.com"
Leave the remaining upcoming prompts empty

### To check if files exists..
ls ~/.ssh
Login to git account
click on settings from left side profile
select SSH and GPG keys
On git bash... enter

> cat ~/.ssh/id_rsa.pub

Copy the key and paste in key section
click Add SSH-key

Now go to home page of git and click to new for new repository
give name to repository (btre_project)

> git remote add origin https://github.com/akashdraut/btre_project.git

> git push -u origin master

## Create vagrant file using the command

> vagrant init ubuntu/bionic64

## Predefined vagrant file is mentioned in below link
[vagrant file] (https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682)

### Start Vagrant box
> vagrant up

### Connect to Vagrant box
> vagrant ssh

> cd /vagrant
### Disconnect from Vagrant box
Note: This command is a standard linux command for ending an SSH session
exit

### Stop Vagrant box

> vagrant halt

### Remove Vagrant box

> vagrant destroy

### Update Vagrant box image
Note: you must rebuild the image after updating

> vagrant box update

## How we can use our development server when we work on our project

Because the development server is virtual machine

To push the code to git, open new git bash window.
Get to the project directory.
And follow the git commands to push the code.

## Create virtual environment
> python -m venv ~/env

This will create virtual environment. (Make sure you are in vagrant server).
This is because we must not synchronize it with local machine.
So if you ever need to destroy and recreate vagrant over from scratch you can do that with fresh  python virtual environment.

To activate the environment...
>source ~/env/bin/activate

## Install packages into the virtual environment
Make sure vagrant is running and virtual environment is activated
>pip install -r requirements.txt

## Activate the server

> python manage.py runserver 0.0.0.0:8000
