#!/bin/sh

set -xe

cd /app

case "$DEBUGGER" in
    True) WORKERS=1 THREADS=6 ;; # Single Worker for Debugger
       *) WORKERS=3 THREADS=6 ;;
esac

gunicorn --reload --worker-tmp-dir /dev/shm --workers=$WORKERS --threads=$THREADS --worker-class=gthread --bind 0.0.0.0:8000 run:app