#!/bin/sh

PRIMARY=$(xrandr| grep -P '^[[:alnum:]-]+ connected primary' | cut -d ' ' -f 1)
SECONDARY=$(xrandr| grep -P '^[[:alnum:]-]+ connected (?!primary)' | cut -d ' ' -f 1)
OUTPUTS=$(xrandr | sed  -ne '2,$s;^\([^ ]\{1,\}\).*;\1;p' | grep -v "^$PRIMARY\$")

CMD="xrandr --output $PRIMARY --primary --auto "

# turn off all unused outputs
for output in $OUTPUTS; do
  if [[ "$output" != "$SECONDARY" ]]; then
    CMD="$CMD--output $output --off "
  fi
done

if [[ "$1" == "off" ]] || [[ -z "$1$SECONDARY" ]]; then
  if [[ "$SECONDARY" ]]; then
    # explicit ask to turn off secondary output
    CMD="$CMD--output $SECONDARY --off"
  fi
elif [[ "$SECONDARY" ]]; then
  # turn on secondary output
  CMD="$CMD--output $SECONDARY --${1:-right-of} $PRIMARY --auto"
else
  echo "No connected secondary!"
  exit 1
fi

exec $CMD
