# gambas build
gbc3 -e -a -g -t  -f public-module -f public-control || gbc3 -e -a -g -t -p -m
gba3 || return 1

