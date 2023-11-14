#!/bin/sh

# Launch dbus if necessary.
dbus-update-activation-environment --all
if test -z "$DBUS_SESSION_BUS_ADDRESS"; then
   eval $(dbus-launch --sh-syntax --exit-with-session)
fi

# Start Gnome Keyring.
export $(gnome-keyring-daemon --start --components=pkcs11,secrets,ssh,gpg)


# Start SSH agent.
eval $(ssh-agent)
export SSH_ASKPASS=/usr/libexec/seahorse/ssh-askpass

source $HOME/.config/xprofile

# Start Qtile WM.
exec qtile start
