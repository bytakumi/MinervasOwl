from delivery_client.discord import Discord
from news_platform.mit import MIT
from news_platform.google import Google
from news_platform.gizmodo import Gizmodo

import os


def delivery():
    # MIT Technology Review JPの配信
    mit_channel = Discord(os.environ.get("DISCORD_WEBHOOK_MIT"))
    mit = MIT()
    mit.news_delivery(delivery_client=mit_channel)

    # Google News の配信
    google_channel = Discord(os.environ.get("DISCORD_WEBHOOK_GOOGLE"))
    google = Google()
    google.news_delivery(delivery_client=google_channel)

    # Gizmodoの配信
    gizmodo_channel = Discord(os.environ.get("DISCORD_WEBHOOK_GIZMODO"))
    gizmodo = Gizmodo()
    gizmodo.news_delivery(delivery_client=gizmodo_channel)

    # TODO: NewsPicksの配信

    # TODO: Courrier Japanの配信

    # TODO: CNET JAPANの配信

    # TODO: IT Mediaの配信

    # TODO: WIRED JPの配信

    # TODO: ロイターの配信

    # TODO: TechCrunchの配信

    # TODO: Venture Beatの配信

    # TODO: BBC Newsの配信

    # TODO: PublicKeyの配信


if __name__ == "__main__":
    delivery()
