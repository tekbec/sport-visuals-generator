from cairosvg import svg2png
import PIL, PIL.Image
import os
from utils import init_tmp_dir
import requests

def paste_svg(base: PIL.Image.Image, svg: str, pos, width: int):
    width = int(width)
    tmp_dir = init_tmp_dir()
    svg_filepath = None
    if os.path.isfile(svg):
        svg_filepath = svg
    else:
        svg_filepath = os.path.join(tmp_dir, 'tmp.svg')
        if os.path.isfile(svg_filepath): os.unlink(svg_filepath)
        response = requests.get(svg)
        response.raise_for_status()
        with open(svg_filepath, 'wb') as file:
            file.write(response.content)
    png_filepath = os.path.join(tmp_dir, 'tmp.png')
    if os.path.isfile(png_filepath): os.unlink(png_filepath)
    svg2png(url=svg_filepath, output_width=width, write_to=png_filepath)
    im = PIL.Image.open(png_filepath)
    base.paste(im, (int(pos[0]-im.width/2),int(pos[1]-im.height/2)),mask=im)