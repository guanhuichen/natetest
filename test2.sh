#!/bin/bash
ARGS=$(getopt -a -o T:O:LMSsth -l param1:,param2: -- "$@")
eval set -- "${ARGS}"
while true; do
  case "$1" in
  -T | --param1)
    param1="$2"
    shift
    ;;
  -O | --param2)
    param2="$2"
    shift
    ;;
  --)
    shift
    break
    ;;
  esac
  shift
done

mkdir -p "${param1%/*}"
mkdir -p "${param2%/*}"

echo "this is param1" > ${param1}
echo "this is param2" > ${param2}
