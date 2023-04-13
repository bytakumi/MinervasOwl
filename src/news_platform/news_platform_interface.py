from abc import ABC, abstractmethod, ABCMeta


# TODO: 抽象クラスを用意する
class NewsPlatformInterface(ABC):
    def news_delivery(self, delivery_client):
        article = self.get_article()
        message = delivery_client.generate_message(article)
        delivery_client.post(message)

    @abstractmethod
    def get_article(self):
        """記事情報を返す

        Returns:
            (obj): 記事情報
                [{
                    "title": "xxx",
                    "summary": "xxx",
                    "url": "url",
                    "author": "xxx",
                    "thumbnail_url": "https://..."
                }]
        """
        raise NotImplementedError
