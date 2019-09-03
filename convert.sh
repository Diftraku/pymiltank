#!/bin/sh
BASEPATH=$(dirname  $(realpath $0))

EXTENSION='.png'
FILTER='*'
DESTINATION="${BASEPATH}/out"
SOURCE=''

if [ $# -eq 0 ]; then
    echo "Usage: $0 [-e|--ext extension] source"
    echo "    -e|--ext      Extension for sprite files (default: .png)"
    echo "    -f|--filter   Filter for sprite filenames (default: *)"
    echo "    -d|--dest     Destination folder for converted files (default: ${DESTINATION})"
    echo
    echo "Files in destination will follow the name from source (without the extension)"
fi

OUTPUT_FILENAME=""
while [ "$1" != "" ]; do
    case "$1" in
        -e | --ext) EXTENSION=$2; shift 2;;
        -d | --dest) DESTINATION=$2; shift 2;;
        -f | --filter) FILTER=$2; shift 2;;
        --) shift; break;;
        *) SOURCE="$1"; shift;;
    esac
done

if [ ! -d $DESTINATION ]; then
    while true; do
        read -p "Destination ${DESTINATION} does not exist, create it? (Y/n)" yn
        case $yn in
            [Yy]* ) break;;
            [Nn]* ) echo 'Cannot proceed, check destination and try again'; exit;;
            * ) break;;
        esac
    done
    mkdir -p $DESTINATION
fi

# Iterate over all applicable files
for sprite in $(find $SOURCE -iname "${FILTER}${EXTENSION}"); do
    echo 'Processing '$sprite
    $BASEPATH/image2ansi.py -o $DESTINATION/$(basename $sprite $EXTENSION) $sprite
done