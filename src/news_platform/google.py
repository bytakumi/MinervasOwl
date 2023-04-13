from .news_platform_interface import NewsPlatformInterface
from bs4 import BeautifulSoup
import feedparser


class Google(NewsPlatformInterface):
    def __init__(self):
        self.__feed_url = "https://news.google.com/news/rss/headlines/section/topic/WORLD?hl=ja&gl=JP&ceid=JP:ja"
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
                "author": "Google (Topic: World)",
                "thumbnail_url": "https://expresswriters.com/wp-content/uploads/2015/09/google-new-logo-450x450.jpg"
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
