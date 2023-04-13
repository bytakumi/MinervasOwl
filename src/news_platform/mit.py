from .news_platform_interface import NewsPlatformInterface
import feedparser


class MIT(NewsPlatformInterface):
    def __init__(self):
        self.__feed_url = "https://www.technologyreview.jp/feed/"
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
                "author": "MIT Technology Review JP",
                "thumbnail_url": "https://ase.mit.edu/wp-content/uploads/2019/12/1-fRTAqrjmS6BLG1L49aq-dg.jpeg"
            })

            # 記事の配信上限を超えたら処理を終える
            if article_count >= self.__article_limit:
                break
            article_count += 1

        return contents

    def __remove_html(self, article):
        """有料記事についている有料プラン案内文を削除する

        Args:
            article(string): 記事文章

        Returns:
            (string): 有料プラン案内文を削除した記事文章
        """
        pos = article.find("<div")
        return article[:pos]