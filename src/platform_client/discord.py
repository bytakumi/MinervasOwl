from discordwebhook import Discord as DiscordWebhook


# TODO: 抽象クラスを用意する
class Discord():
    def __init__(self, webhook):
        self.client = DiscordWebhook(url=webhook)

    def post(self, content):
        """ Discordにメッセージを送信する

        Args:
            content(string): Discordに送信するメッセージ
        """
        self.client.post(content=content)
