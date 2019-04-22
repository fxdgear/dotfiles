#! /bin/bash

# Start i3 and log to ~/.i3/logfile
echo "Starting at $(date)" >> ~/.i3/logfile
exec /usr/bin/i3 -V -d all >> ~/.i3/logfile
