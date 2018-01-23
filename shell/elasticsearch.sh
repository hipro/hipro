#!/bin/sh
export ES_HEAP_SIZE=28g
# export ES_HEAP_NEWSIZE=5g
export ES_GC_LOG_FILE=/var/log/es/gc.log

ES_DIR=/opt/app/elasticsearch
PID_FILE=${ES_DIR}/es.pid
EXEC=${ES_DIR}/bin/elasticsearch

case "$1" in
    start)
        if [ -f ${PID_FILE} ]
        then
            echo "$PID_FILE exists, process is already running or crashed"
        else
            echo "Starting ElasticSearch..."
            ${EXEC} -d -p ${PID_FILE}
        fi
        ;;
    stop)
        if [ ! -f ${PID_FILE} ]
        then
            echo "$PID_FILE does not exist, process is not running"
        else
            PID=$(cat ${PID_FILE})
            echo "Stopping ..."
            kill ${PID}
            while [ -x /proc/${PID} ]
            do
                echo "Waiting for ElasticSearch to shutdown ..."
                sleep 1
            done
            echo "ElasticSearch stopped"
        fi
        ;;
    status)
        PID=$(cat ${PID_FILE})
        if [ ! -x /proc/${PID} ]
        then
            echo 'ElasticSearch is not running'
        else
            echo "ElasticSearch is running ($PID)"
        fi
        ;;
    restart)
        $0 stop
        $0 start
        ;;
    *)
        echo "Please use start, stop, restart or status as first argument"
        ;;
esac
