#!/bin/sh

# dbus
dbus-update-activation-environment --all
if test -z "$DBUS_SESSION_BUS_ADDRESS"; then
	eval $(dbus-launch --sh-syntax --exit-with-session)
fi

# keyring
# export $(gnome-keyring-daemon --start --components=pkcs11,secrets,ssh,gpg)

# ssh
# eval $(ssh-agent)
# export SSH_ASKPASS=/usr/libexec/seahorse/ssh-askpass

# xprofile
. ~/.xprofile

# picom
picom -b &
wezterm &
librewolf &

# qtile
exec qtile start
