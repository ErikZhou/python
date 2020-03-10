#!/bin/bash
#
# e.g.
# for https://www.youtube.com/playlist?list=PLL7JeXQtCv0MslQgUCV3DvKmaagaB9Nms use:
# youtube-list.sh PLL7JeXQtCv0MslQgUCV3DvKmaagaB9Nms

for i in \
    `curl -s "https://www.youtube.com/playlist?list=$1" |\
    grep -Po "/watch.*?$1" |\
    sed -r "s#&.*##" | uniq`;
do
        echo "https://www.youtube.com$i" >> list.txt
    done
