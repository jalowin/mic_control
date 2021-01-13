#!/bin/bash
devicename=$1
device=$(arecord -l | awk -v b="$devicename" 'match($0, b, a) {print}' | gawk '$2 {print $2}' | sed 's/://g')
state=$(amixer -c $device set Mic toggle | gawk 'match($0, /Capture .*\[(.*)\]/, a) {print a[1]}') 
if [ $state = "off" ]; then
	icon="audio-input-microphone-muted-symbolic"
else
    icon="audio-input-microphone-symbolic"
fi
notify-send --hint=int:transient:1 -i $icon "Mic switched: $state" -i "audio-input-microphone" "Mic switched: $state"
