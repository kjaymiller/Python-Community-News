from render_engine.site import Site
from render_engine.blog import Blog, BlogPost
from render_engine.page import Page
import jinja2

class Site(Site):
    output_path = 'output'
    site_vars: dict = {
        "SITE_TITLE": "Python Community News",
        "SITE_URL":  "https://pythoncommunitynews.com"
    }
    engine = jinja2.Environment(loader=jinja2.FileSystemLoader("./site/templates"))
    
if __name__ == '__main__':
    site = Site(static="site/static")
    
    @site.render_page
    class index(Page):
        template = 'index.html'


    @site.render_collection
    class archive(Blog):
        has_archive = True
        output_path = './'
        content_path = './site/content'
        template:str = 'new_post.html'
        archive_template: str = 'archive.html'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)