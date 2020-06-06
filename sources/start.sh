#! /usr/bin/env sh
set -e

# If there's a prestart.sh script in the /app directory, run it before starting
PRE_START_PATH=/app/prestart.sh
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . $PRE_START_PATH
else
    echo "There is no script $PRE_START_PATH"
fi

if [ "$NODE_TYPE" = "worker" ]; then
    echo "Instance will run as worker node"
    CONFIG_FILE_PATH=/etc/supervisor/conf.d/supervisord-worker-node.conf
elif [ "$NODE_TYPE" = "web" ]; then
    echo "Instance will run as web node"
    CONFIG_FILE_PATH=/etc/supervisor/conf.d/supervisord-web-node.conf
else
  echo "NODE_TYPE var is not defined neither worker nor web"
  exit 22
fi

# Start Supervisor using the proper configuration
exec /usr/bin/supervisord -c "$CONFIG_FILE_PATH"