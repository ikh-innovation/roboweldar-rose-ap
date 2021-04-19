#!/bin/bash

if [[  -z "$PM2_ENABLED" ]]; then
    echo "INFO: Running standalone"
    node /opt/component/src/init
else
    echo "***********************************************"
    echo "INFO: Encapsulated by pm2-runtime "
    echo "see https://pm2.io/doc/en/runtime/integration/docker/"
    echo "***********************************************"
    pm2-runtime /opt/component/src/init
fi