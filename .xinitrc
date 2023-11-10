#!/bin/sh

# Launch dbus if necessary.
dbus-update-activation-environment --all
if test -z "$DBUS_SESSION_BUS_ADDRESS"; then
   eval $(dbus-launch --sh-syntax --exit-with-session)
fi

export $(gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)

# Swap Caps and Esc.
setxkbmap -option caps:swapescape

# Start Qtile WM.
exec qtile start
