#!/bin/bash
displayCount=$(xrandr | grep connected | wc -l)


if [ $displayCount > 1 ]; then
    supergfxctl --mode hybrid
    echo "External Display was detected, setting graphic mode to HYBRID"
else
    supergfxctl --mode integrated
    echo "No externaml Dieplay was detected. Nothing to do."
fi
