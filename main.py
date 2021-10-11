#!/usr/bin/env python3

# this is just my way of using the function. Feel free to come up with your own notification system
from cockroach import was_cockroach_updated
from discord_webhook import DiscordWebhook
import sys

a = was_cockroach_updated()

if a != "NO":
    webhook = DiscordWebhook(url=sys.argv[1], rate_limit_retry=True,
                             content=f'New Cockroach DB Version!!! {a}')
    response = webhook.execute()
