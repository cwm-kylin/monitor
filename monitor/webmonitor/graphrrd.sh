#!/bin/bash
rrdfile=$1
pngfile=$2
rrdtype=$3
appname=$4
GraphStart=$5
GraphEnd=$6
ymax=$7
Alarm=$8

rrdtool_font_msyhbd="/opt/monitor/static/font/msyhbd.ttf"
rrdtool_font_msyh="/opt/monitor/static/font/msyh.ttf"
export LANG=zh_CN.utf8
export LC_ALL=zh_CN.utf8
export LANG=zh_CN.utf8
export LANGUAGE=zh_CN.utf8
export LC_CTYPE=zh_CN.utf8
export LC_TIME=zh_CN.utf8

if [ "$rrdtype" == "time" ]; then
/usr/bin/rrdtool graph ${pngfile} -w 500 -h 207 \
-n TITLE:9:${rrdtool_font_msyhbd} \
-n UNIT:8:${rrdtool_font_msyh} \
-n LEGEND:8:${rrdtool_font_msyh} \
-n AXIS:8:${rrdtool_font_msyh} \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c FONT#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
--title "Business_reposonse-${appname}" -v "speed(s)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u ${ymax} -r  \
DEF:NAMELOOKUP_TIME=${rrdfile}:NAMELOOKUP_TIME:AVERAGE \
DEF:CONNECT_TIME=${rrdfile}:CONNECT_TIME:AVERAGE \
DEF:PRETRANSFER_TIME=${rrdfile}:PRETRANSFER_TIME:AVERAGE \
DEF:STARTTRANSFER_TIME=${rrdfile}:STARTTRANSFER_TIME:AVERAGE \
DEF:TOTAL_TIME=${rrdfile}:TOTAL_TIME:AVERAGE \
COMMENT:" \n" \
AREA:TOTAL_TIME#0011ff:total_time \
GPRINT:TOTAL_TIME:LAST:"current\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:AVERAGE:"avg\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:MAX:"max\:%0.2lf %Ss"  \
GPRINT:TOTAL_TIME:MIN:"min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:NAMELOOKUP_TIME#eeee00:name_lookup \
GPRINT:NAMELOOKUP_TIME:LAST:"current\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:AVERAGE:"avg\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:MAX:"max\:%0.2lf %Ss"  \
GPRINT:NAMELOOKUP_TIME:MIN:"min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:CONNECT_TIME#00aa00:connect_time \
GPRINT:CONNECT_TIME:LAST:"current\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:AVERAGE:"avg\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:MAX:"max\:%0.2lf %Ss"  \
GPRINT:CONNECT_TIME:MIN:"min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:PRETRANSFER_TIME#ff5511:Start_transmission \
GPRINT:PRETRANSFER_TIME:LAST:"current\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:AVERAGE:"avg\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:MAX:"max\:%0.2lf %Ss"  \
GPRINT:PRETRANSFER_TIME:MIN:"min\:%0.2lf %Ss"  \
COMMENT:" \n" \
LINE1:STARTTRANSFER_TIME#004455:Frist_byte \
GPRINT:STARTTRANSFER_TIME:LAST:"current\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:AVERAGE:"avg\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:MAX:"max\:%0.2lf %Ss"  \
GPRINT:STARTTRANSFER_TIME:MIN:"min\:%0.2lf %Ss"  \
COMMENT:" \n" \
HRULE:${Alarm}#ff0000:"(Alarm_value)" \
COMMENT:" \n" \
COMMENT:" \n" \
COMMENT:"\t\t\t\t\t\t\t\t\t\tLast_update \:$(date '+%Y-%m-%d %H\:%M')\n"

elif [ "$rrdtype" == "download" ]; then
/usr/bin/rrdtool graph ${pngfile} -w 320 -h 102 \
-n TITLE:9:${rrdtool_font_msyhbd} \
-n UNIT:8:${rrdtool_font_msyh} \
-n LEGEND:8:${rrdtool_font_msyh} \
-n AXIS:8:${rrdtool_font_msyh} \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
-t "download_speed-${appname}" -v "speed (KB/S)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u ${ymax} -r  \
DEF:SPEED_DOWNLOAD=${rrdfile}:SPEED_DOWNLOAD:AVERAGE \
COMMENT:" \n" \
AREA:SPEED_DOWNLOAD#68CEFF:download_speed \
GPRINT:SPEED_DOWNLOAD:AVERAGE:"avg\:%6.0lf%Sbyte"  \
GPRINT:SPEED_DOWNLOAD:MAX:"max\:%6.0lf%Sbyte"  \
GPRINT:SPEED_DOWNLOAD:MIN:"min\:%6.0lf%Sbyte"  \
COMMENT:" \n"

elif [ "$rrdtype" == "unavailable" ]; then
/usr/bin/rrdtool graph ${pngfile}  -w 320 -h 102 \
-n TITLE:9:${rrdtool_font_msyhbd} \
-n UNIT:8:${rrdtool_font_msyh} \
-n LEGEND:8:${rrdtool_font_msyh} \
-n AXIS:8:${rrdtool_font_msyh} \
-c SHADEA#808080 \
-c SHADEB#808080 \
-c FRAME#006600 \
-c ARROW#FF0000 \
-c AXIS#000000 \
-c CANVAS#eeffff \
-c BACK#ffffff \
-t "Business_availability-${appname}" -v "frequency(num)" \
--start ${GraphStart} \
 --end ${GraphEnd} \
--lower-limit=0 \
--base=1024 \
-u 1 -r  \
DEF:UNAVAILABLE=${rrdfile}:UNAVAILABLE:AVERAGE \
COMMENT:" \n" \
AREA:UNAVAILABLE#33ff00:unavailable \
GPRINT:UNAVAILABLE:AVERAGE:"avg\:%0.2lf"  \
GPRINT:UNAVAILABLE:MAX:"max\:%0.2lf"  \
GPRINT:UNAVAILABLE:MIN:"min\:%0.2lf"  \
COMMENT:" \n"
else
    echo "ERROR!"
fi
