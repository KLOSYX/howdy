# Open the config file in an editor

# Import required modules
import os
import subprocess

from i18n import _

# Let the user know what we're doing
print(_("Opening config.ini in the default editor"))

# Default to the nano editor
editor = "/bin/nano"

# Use the user preferred editor if available
if "EDITOR" in os.environ:
	editor = os.environ["EDITOR"]
elif os.path.isfile("/etc/alternatives/editor"):
	editor = "/etc/alternatives/editor"

config_path = "/etc/howdy"
# Open the editor as a subprocess and fork it
subprocess.call([editor, os.path.dirname(config_path) + "/config.ini"])
