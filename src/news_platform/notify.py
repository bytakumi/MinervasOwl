from .news_platform_interface import NewsPlatformInterface


class Notify(NewsPlatformInterface):
    def get_article(self):
        return [{
            "title": "本日の分のニュースが配信されました。",
            "author": "SYSTEM",
            "thumbnail_url": "",
            "url": ""
        }]
