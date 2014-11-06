import yaml
from jinja2 import Template

def isdict(thing):
    return isinstance(thing, dict)

with open("presentation.yml", 'r') as source:
    pres = yaml.load(source)
    for slide in pres.get("slides"):
        print slide.get("name")
    # print yaml.dump(pres, default_flow_style=False)
    # extensions = []
    # env = Environment(
    #     extensions=extensions)
    with open("index-template.html", "r") as template_file:
        data = template_file.read()
        template = Template(data)
        template.globals = {'isdict': isdict}
        rendered = template.render(**pres)
        with open("index.html", "w") as target:
            target.write(rendered)

