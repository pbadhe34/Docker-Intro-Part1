Docker running on macOS:

$ base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/usr/local/bin/docker-machine &&
  chmod +x /usr/local/bin/docker-machine

Docker running on Linux:

$ base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo install /tmp/docker-machine /usr/local/bin/docker-machine

Docker running with Windows with Git BASH:

$ base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  mkdir -p "$HOME/bin" &&
  curl -L $base/docker-machine-Windows-x86_64.exe > "$HOME/bin/docker-machine.exe" &&
  chmod +x "$HOME/bin/docker-machine.exe"


Make the docker-machine binary executable.

chmod +x ./docker-machine

Move the binary in to your PATH.

sudo mv ./docker-machine /usr/local/bin/docker-machine


OR
Download from
https://github.com/docker/machine/releases/

Check the installation by displaying the Machine version:

$ docker-machine version
docker-machine version 0.14.0, build 9371605

Install bash completion scripts

The Machine repository supplies several bash scripts that add features such as:

    command completion
    a function that displays the active machine in your shell prompt
    a function wrapper that adds a docker-machine use subcommand to switch the active machine

Confirm the version and save scripts to /etc/bash_completion.d or /usr/local/etc/bash_completion.d:

base=https://raw.githubusercontent.com/docker/machine/v0.14.0
for i in docker-machine-prompt.bash docker-machine-wrapper.bash docker-machine.bash
do
  sudo wget "$base/contrib/completion/bash/${i}" -P /etc/bash_completion.d
done


Then you need to run source /etc/bash_completion.d/docker-machine-prompt.bash in your bash terminal to tell your setup where it can find the file docker-machine-prompt.bash that you previously downloaded.

To enable the docker-machine shell prompt, add $(__docker_machine_ps1) to your PS1 setting in ~/.bashrc.

PS1='[\u@\h \W$(__docker_machine_ps1)]\$ '


How to uninstall Docker Machine

To uninstall Docker Machine:

    Optionally, remove the machines you created.

    To remove each machine individually: docker-machine rm <machine-name>

    To remove all machines: docker-machine rm -f $(docker-machine ls -q) (you might need to use -force on Windows).

    Removing machines is an optional step because there are cases where you might want to save and migrate existing machines to a Docker for Mac or Docker for Windows environment, for example.

    Remove the executable: rm $(which docker-machine)



