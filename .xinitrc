#!/bin/sh

# dbus
dbus-update-activation-environment --all
if test -z "$DBUS_SESSION_BUS_ADDRESS"; then
	eval $(dbus-launch --sh-syntax --exit-with-session)
fi

# autostart
autostart

# qtile
exec qtile start
