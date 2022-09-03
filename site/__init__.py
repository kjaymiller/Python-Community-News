from render_engine.blog import Blog
from render_engine.page import Page
from render_engine.site import Site
from jinja2 import Environment, FileSystemLoader


class Site(Site):
    output_path = "output"
    site_vars: dict = {
        "SITE_TITLE": "Python Community News",
        "SITE_URL": "https://pythoncommunitynews.com",
    }
    engine = Environment(
        loader=FileSystemLoader(["site/templates", "templates"])
    )

if __name__ == "__main__":
    site = Site(static="static")

    @site.render_page
    class index(Page):
        template = "index.html"

    @site.render_page
    class CoC(Page):
        content_path = "CODE_OF_CONDUCT.md"
        template = "markdown_page.html"
        title = "Code of Conduct"

    @site.render_collection
    class archive(Blog):
        has_archive = True
        output_path = "./"
        content_path = "./site/content"
        template = "new_post.html"
        archive_template: str = "archive.html"
