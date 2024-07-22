# Command Line Interface

## What is an OS?
- An operating system is software that acts as an interface between the user and the computer hardware.
- Every computer must have at least one operating system to run other software programs and applications like MS Word, Chrome, Games, etc.
- The operating system helps you communicate with the computer withouth knowing how to speak the computer's language.
- It is not possible for the user to use any computer or mobile device withouth having an operating system.

## Kernel
- The kernel is the central component of a computer's operating systems.
- The only work done by the kernel is to manage communication between software and hardware.
- A kernel is at the core of a computer
- While the kernel is the innermost part of an **Operating System**, a **shell** is the outermost part.

## Console
- The console is the physical device that allows you to interact with the computer.

## Terminal
- A terminal is a text input and output environment. It is a program that acts as a wrapper and allows us to enter commands that the computer processes.
 - The terminal is a program, just like any other. And like any program, you can install it and uninstall it as you please. It's also possible to have many terminals installed in your computer and run whichever you want whenever you want.

## Shell
- A shell is a program that acts as command-line interpreter. It processes commands and outputs results. It interprets and processes the commands entered by the user.
- Same as the terminal, the shell is a program that comes by default in all operating systems, but can also be installed and uninstalled by the user.
- Different shells come with different syntax and chracteristcs as well. It's also possible to have many shells installed at your computer.
- In most Linux and Mac operating systems the default shell is bash.

## CLI
- The CLI is the interface in which we enter commands for the computer to process.
- Most operating systems have two different types of interfaces:
    - CLI
    - GUI

### Why should we use the terminal?
- It's more efficient. There are many tasks where a GUI would require many clicks around different windows. But on the CLI these tasks can be executed with a single command.
- We can easily automate tasks. We can build scripts with our shell and later on execute those scripts whenever we want. This is incredibly useful when dealing with repetitive tasks that we don't want to do over and over again.
- Sometimes the CLI will be the only way in which we'll be able to interact with a computer. Take, for example, the case when you would need to interact with a robotic plataform. In most of these cases, you won't have a GUI available, just a CLI to run commands in.

### How to know what shell I'm running?
- To know what shell you're currently running, you can use the following command:
```bash
echo $0
```

## Communication
- `ssh` securely sends commands to a computer over an unsecured network
```bash
$ ssha user@ipmachine
```

- `scp` command allows the user to securely copy files and directories between to locations
```bash
$ scp [opcções] user@host1:arq1 user@host2:arq2
$ scp usuario@origm:/dir/arquivo usuario@destino:/dir/arquivo
$ scp -r usuario@origem:/dir usuario@destino:/dir
```

## Bash Script
- A bash script is a file that contains a series of commands that the computer will execute.
- To create a bash script, you can create a file with the `.sh` extension and write the commands you want to execute in it.
```bashscript
#! /bin/bash
repoName=$1
while [ -z "$repoName"]
do
    echo 'Provide a repository name'
    read -r -p $'Repository name:' repoName
done
echo "# $repoName" >> README.md
git init
git add .
git commit -m "Initial commit"
```
