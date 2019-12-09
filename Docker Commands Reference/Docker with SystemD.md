https://docs.docker.com/config/daemon/systemd/

Control Docker with systemd
Estimated reading time: 3 minutes

Many Linux distributions use systemd to start the Docker daemon. This document shows a few examples of how to customize Docker’s settings.
Start the Docker daemon
Start manually

Once Docker is installed, you need to start the Docker daemon. Most Linux distributions use systemctl to start services. If you do not have systemctl, use the service command.

    systemctl:

    $ sudo systemctl start docker

    service:

    $ sudo service docker start

Start automatically at system boot

If you want Docker to start at boot, see Configure Docker to start on boot.
Custom Docker daemon options

There are a number of ways to configure the daemon flags and environment variables for your Docker daemon. The recommended way is to use the platform-independent daemon.json file, which is located in /etc/docker/ on Linux by default. See Daemon configuration file.

You can configure nearly all daemon configuration options using daemon.json. The following example configures two options. One thing you cannot configure using daemon.json mechanism is a HTTP proxy.
Runtime directory and storage driver

You may want to control the disk space used for Docker images, containers, and volumes by moving it to a separate partition.

To accomplish this, set the following flags in the daemon.json file:

{
    "data-root": "/mnt/docker-data",
    "storage-driver": "overlay"
}

HTTP/HTTPS proxy

The Docker daemon uses the HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environmental variables in its start-up environment to configure HTTP or HTTPS proxy behavior. You cannot configure these environment variables using the daemon.json file.

This example overrides the default docker.service file.

If you are behind an HTTP or HTTPS proxy server, for example in corporate settings, you need to add this configuration in the Docker systemd service file.

    Create a systemd drop-in directory for the docker service:

    $ sudo mkdir -p /etc/systemd/system/docker.service.d

    Create a file called /etc/systemd/system/docker.service.d/http-proxy.conf that adds the HTTP_PROXY environment variable:

    [Service]
    Environment="HTTP_PROXY=http://proxy.example.com:80/"

    Or, if you are behind an HTTPS proxy server, create a file called /etc/systemd/system/docker.service.d/https-proxy.conf that adds the HTTPS_PROXY environment variable:

    [Service]
    Environment="HTTPS_PROXY=https://proxy.example.com:443/"

    If you have internal Docker registries that you need to contact without proxying you can specify them via the NO_PROXY environment variable:

    [Service]    
    Environment="HTTP_PROXY=http://proxy.example.com:80/" "NO_PROXY=localhost,127.0.0.1,docker-registry.somecorporation.com"

    Or, if you are behind an HTTPS proxy server:

    [Service]    
    Environment="HTTPS_PROXY=https://proxy.example.com:443/" "NO_PROXY=localhost,127.0.0.1,docker-registry.somecorporation.com"

    Flush changes:

    $ sudo systemctl daemon-reload

    Restart Docker:

    $ sudo systemctl restart docker

    Verify that the configuration has been loaded:

    $ systemctl show --property=Environment docker
    Environment=HTTP_PROXY=http://proxy.example.com:80/

    Or, if you are behind an HTTPS proxy server:

    $ systemctl show --property=Environment docker
    Environment=HTTPS_PROXY=https://proxy.example.com:443/

Configure where the Docker daemon listens for connections

See Configure where the Docker daemon listens for connections.
Manually create the systemd unit files

When installing the binary without a package, you may want to integrate Docker with systemd. For this, install the two unit files (service and socket
