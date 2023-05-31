from .news_platform_interface import NewsPlatformInterface
from bs4 import BeautifulSoup
from trans007 import GoogleTranslate
import feedparser


class GatesNotes(NewsPlatformInterface):
    def __init__(self):
        self.__feed_url = "https://www.gatesnotes.com/RSS"
        self.__article_limit = 5  # 記事の配信数

    def get_article(self):
        articles = feedparser.parse(self.__feed_url)
        article_count = 1

        contents = []
        for article in articles["entries"]:
            contents.append({
                "title": self.__translate_en_to_ja(article["title"]),
                "summary": self.__translate_en_to_ja(self.__remove_html(article["summary"])),
                "url": article["link"],
                "author": "GatesNotes",
                "thumbnail_url": "https://pbs.twimg.com/profile_images/1564398871996174336/M-hffw5a_400x400.jpg"
            })

            # 記事の配信上限を超えたら処理を終える
            if article_count >= self.__article_limit:
                break
            article_count += 1

        return contents

    def __translate_en_to_ja(self, string_en):
        trans = GoogleTranslate()
        return trans.translate(string_en, 'en', 'ja')

    def __remove_html(self, article):
        """文中からhtmlタグを削除する

        Args:
            article(string): 記事文章

        Returns:
            (string): HTMLタグを削除した記事文章
        """
        return BeautifulSoup(article, "html.parser").text
