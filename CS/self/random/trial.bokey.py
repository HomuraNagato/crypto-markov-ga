import numpy as np
from collections import OrderedDict
from bokeh.plotting import *
from bokeh.models import HoverTool, TapTool, OpenURL

x = np.random.randint(100, size=10)
y = np.random.randint(100, size=10)
#buildnums = np.random.randint(1000, size=10)
buildnums = np.linspace(1e,10,num=10)
print("buildnums", buildnums)

source = ColumnDataSource(
    data=dict(x=x, y=y, buildnum=buildnums))

p = figure(title="Builds", tools="pan,wheel_zoom,reset,hover")

p.circle(x, y, radius=3, source=source,
         fill_color="blue", fill_alpha=0.6, line_color=None)

hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("Build", '@buildnum')
    ])

#tap = TapTool(plot=p, action=OpenURL(url="https://www.bing.com"))
#p.tools.append(tap)

output_file("builds.html")
show(p)
