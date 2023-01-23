import os

from slack_bolt import App
from views.home import update_home_tab
from views import view_registry
from commands import commands_registry
from actions import actions_registry

# Initializes your app with your bot token and signing secret
app = App(
    token="xoxb-4575803423105-4565651521380-qRKiioj62EQLoVrz3t1Ueuaf",
    signing_secret="bef4624815f04e5e9f0d6262efab24a0",
)

for key in view_registry:
    app.event(key)(view_registry[key])


for key in commands_registry:
    app.command(key)(commands_registry[key])


for key in actions_registry:
    app.action(key)(actions_registry[key])
