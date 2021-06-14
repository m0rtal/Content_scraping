PAGINATION = {
    "selector": "//li[@class='pager-next']"
                "/a"
                "/@href",
    "callback": "parse",
}

ARTICLES = {
    "selector": "//div[@class='text-content']"
                "/h4"
                "/a"
                "/@href",
    "callback": "parse_article",
}

ARTICLE_DATA = {
    "title": "//h1[@class='page-header']/text()",
    "text_content": "//div[contains(@class, 'field')]"
                    "//text()"
}

PAYWALL_ARTICLE_DATA = {
    "title": "//h1[@class='page-header']",
    "text_content": "//div[contains(@class, 'field-name-body')]",
    "images": "//div[@class='rtecenter']/img"
}
