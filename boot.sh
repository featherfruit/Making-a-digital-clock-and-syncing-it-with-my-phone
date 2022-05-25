PATH=~/bin:/usr/bin/:/bin
SHELL=/bin/bash

#  OLED display
tmux new -d -s oled /home/qtpy/display/start-disp.sh

# Flask server
tmux new -d -s flask /home/qtpy/live-clock/start-server.sh
