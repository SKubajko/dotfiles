#!/usr/bin/env python3
import subprocess

result = subprocess.run(['playerctl', 'metadata', 'xesam:artist'], stdout=subprocess.PIPE)
artist = result.stdout.decode('utf-8').replace("\n","")

result = subprocess.run(['playerctl', 'metadata', 'xesam:title'], stdout=subprocess.PIPE)
title = result.stdout.decode('utf-8').replace("\n","")

if len(artist) > 0 and len(title) > 0:
    out = f" {artist} - {title}"
else:
    out = ""
print(f'{{"text":"{out}"}}')
