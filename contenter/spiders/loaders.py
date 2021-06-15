from itemloaders.processors import TakeFirst, Join
from scrapy.loader import ItemLoader


class GCarticleLoader(ItemLoader):
    default_item_class = dict
    title_out = TakeFirst()
    text_content_out = Join()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get("response"):
            self.add_value("url", self.context["response"].url)
