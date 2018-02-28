#!/bin/bash

cd static/posters/
for i in $( ls *.pdf); do convert -verbose -density 150 -trim $i -quality 100 -flatten -sharpen 0x1.0 -geometry x200 thumbnails/$i.png; done
cp *.pdf ../on-program/

cd ../../static/presentations/
for i in $( ls *.pdf); do convert -verbose -density 150 -trim $i[0] -quality 100 -flatten -sharpen 0x1.0 -geometry x200 thumbnails/$i.png; done
cp *.pdf ../on-program/

