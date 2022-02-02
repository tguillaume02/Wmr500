# installer for the wxWmr500 driver
#
# Based on installer for bootstrap skin
#
# Configured by Bill to install weewxMQTT user driver, 2016.

#import os.path
#import configobj

import setup
#import distutils

def loader():
    return wxWmr500Installer()

class wxWmr500Installer(setup.ExtensionInstaller):
    def __init__(self):
        super(wxWmr500Installer, self).__init__(
            version="0.2",
            name='wxWmr500',
            description='A weewx driver which subscribes to MQTT topics providing weewx compatible data',
            author="Tim Sneddon",
            author_email="tim@sneddon.id.au",
            config={
                'wxWmr500': {
                    'driver': 'user.wxWmr500',
                    'host': 'localhost',           # MQTT broker hostname
                    'poll_interval': 10
                 },
	    },
            files=[('bin/user', ['bin/user/wxWmr500.py'])]
	)
