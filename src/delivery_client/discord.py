from .delivery_client_interface import DeliveryClientInterface
from discordwebhook import Discord as DiscordWebhook


class Discord(DeliveryClientInterface):
    def __init__(self, webhook):
        self.client = DiscordWebhook(url=webhook)

    def generate_message(self, articles):
        contents = []
        for article in articles:
            contents.append({
                "title": article["title"],
                "url": article["url"],
                "author": {
                    "name": article["author"],
                    "icon_url": article["thumbnail_url"],
                },
                "thumbnail": {
                    "url": article["thumbnail_url"]
                }
            })
        return contents

    def post(self, content):
        self.client.post(embeds=content)