from abc import ABC, abstractmethod


class Article(ABC):
    def __init__(self, title, content):
        self._content = content
        self._title = title

    @property
    def content(self):
        return self._content

    @property
    def title(self):
        return self._title

    @abstractmethod
    def clone(self):
        pass


class WikipediaArticle(Article):
    def __init__(self, title, content):
        Article.__init__(self, title, content)

    def clone(self):
        return WikipediaArticle(self.title, self._content)


article = WikipediaArticle(title="Каприз Олмейера",
                           content="""(англ. Almayer's Folly) — роман английского писателя Джозефа Конрада,
опубликованный в 1895 году. Первый роман из серии, объединённой сквозным персонажем капитана Лингарда, куда входят также 
романы «Изгнанник» (англ. An Outcast of the Islands, 1896) и «Спасатели» (англ. Rescue, 1920).""")

article_backup = article.clone()

print("ORIGINAL: ", article.title, article.content, end='\n\n')

print("BACKUP: ", article_backup.title, article_backup.content, end='\n\n')
