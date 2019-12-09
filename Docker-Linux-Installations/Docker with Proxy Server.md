 The proxy server provides the internet connection to your system.
 To configre the proxy for the Linux system to get the connection for installation of Docker

 Click  On topMost left icon 'Search Your Computer' and search and click Network to open the network panel.

 1. Select Network proxy from the list on the left. 

  2. Select Network proxy from the list on the left.

    Choose which proxy method you want to use from:

    None

        The applications will use a direct connection to fetch the content from the web.
    Manual

        For each proxied protocol, define the address of a proxy and port for the protocols. The protocols are HTTP, HTTPS, FTP and SOCKS.
    Automatic

        A URL pointing to a resource, which contains the appropriate configuration for your system.

Applications that use the network connection will use the  specified proxy settings.
  
  *********************************
 Docker with Proxy
 Docker needs the Internet connection.To configire the proxy for Docker usgae

   If the Docker needs to use an HTTP, HTTPS, or FTP proxy server, you can configure it in different ways:

    In Docker 17.07 and higher, you can configure the Docker client to pass proxy information to containers automatically.

    In Docker 17.06 and lower, you must set appropriate environment variables within the container. You can do this when you build the image (which makes the image less portable) or when you create or run the container.


Configure the Docker client

    On the Docker client, create or edit the file ~/.docker/config.json in the home directory of the user which starts containers. Add JSON such as the following, substituting the type of proxy with httpsProxy or ftpProxy if necessary, and substituting the address and port of the proxy server. You can configure multiple proxy servers at the same time.

    You can optionally exclude hosts or ranges from going through the proxy server by setting a noProxy key to one or more comma-separated IP addresses or hosts. Using the * character as a wildcard is supported, as shown in this example.

    {
     "proxies":
     {
       "default":
       {
         "httpProxy": "http://127.0.0.1:3001",
         "noProxy": "*.test.example.com,.example2.com"
       }
     }
    }

    Save the file.

    When you create or start new containers, the environment variables are set automatically within the container.

  2.. Use environment variables
Set the environment variables manually

When you build the image, or using the --env flag when you create or run the container, you can set one or more of the following variables to the appropriate value. This method makes the image less portable, so if you have Docker 17.07 or higher, you should configure the Docker client instead.
Variable-Name	Dockerfile example 	                     docker run Example
HTTP_PROXY 	ENV HTTP_PROXY "http://127.0.0.1:3001" 	        --env HTTP_PROXY="http://127.0.0.1:3001"
HTTPS_PROXY 	ENV HTTPS_PROXY "https://127.0.0.1:3001" 	--env HTTPS_PROXY="https://127.0.0.1:3001"
FTP_PROXY 	ENV FTP_PROXY "ftp://127.0.0.1:3001" 	         --env FTP_PROXY="ftp://127.0.0.1:3001"
NO_PROXY 	ENV NO_PROXY "*.test.example.com,.example2.com"  --env NO_PROXY="*

