from abc import ABC, abstractclassmethod


# TODO: 抽象クラスを用意する
class DeliveryClientInterface(ABC):
    @abstractclassmethod
    def generate_message(self, articles):
        """配信のための構造の記事情報を返す

        Args:
            articles(list): 記事情報
                [{
                    "title": "xxx",
                    "summary": "xxx",
                    "url": "url",
                    "author": "xxx",
                    "thumbnail_url": "https://..."
                }]
        Returns:
            各配信クライアントの引数に合う構造で返却すること
        """
        pass
        # raise NotImplementedError

    def post(self, content):
        raise NotImplementedError