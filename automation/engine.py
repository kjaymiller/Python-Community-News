from jinja2 import Environment, FileSystemLoader

engine = Environment(loader=FileSystemLoader(["templates", "automation/templates"]))
