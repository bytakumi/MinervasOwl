from .news_platform_interface import NewsPlatformInterface
from bs4 import BeautifulSoup
import feedparser


class Gigazine(NewsPlatformInterface):
    def __init__(self):
        self.__feed_url = "https://gigazine.net/news/rss_2.0/"
        self.__article_limit = 5  # 記事の配信数

    def get_article(self):
        articles = feedparser.parse(self.__feed_url)
        article_count = 1

        contents = []
        for article in articles["entries"]:
            contents.append({
                "title": article["title"],
                "summary": self.__remove_html(article["summary"]),
                "url": article["link"],
                "author": "Gigazine",
                "thumbnail_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/GIGAZINE_logo.svg/2560px-GIGAZINE_logo.svg.png"
            })

            # 記事の配信上限を超えたら処理を終える
            if article_count >= self.__article_limit:
                break
            article_count += 1

        return contents

    def __remove_html(self, article):
        """文中からhtmlタグを削除する

        Args:
            article(string): 記事文章

        Returns:
            (string): HTMLタグを削除した記事文章
        """
        return BeautifulSoup(article, "html.parser").text
