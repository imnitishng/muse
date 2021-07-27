#!/bin/sh

# Remove old scrapy.cfg or pids
rm scrapy.cfg twistd.pid

# Add new config with docker supported URL
FILENAME="scrapy.cfg"

cat > $FILENAME << EOL
[settings]
default = lyricraper.settings

[deploy]
url = http://0.0.0.0:6800/
project = lyricraper
EOL

# Run scrapyd server in the backgound and sleep for 5 seconds,
# after sleeping start scrapyd-deploy as a background service
# send all the output that should belong to the terminal at to
# `docker_logs.txt`, in the format of stderr > stdoutput (2>1)
# & declares that those are file descriptors and not actual files 
# once all this happens successfully and returns true, execute the
# next statement with && to tail the docker logs file as it grows
# tail is a never ending function (-F) because if it ends then the
# spiders container will exit causing everything to shutdown.
(scrapyd & sleep 5 && scrapyd-deploy &) > docker_logs.txt 2>&1 && tail -F docker_logs.txt
