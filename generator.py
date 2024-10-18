from dataclasses import dataclass
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from svg import paste_svg

@dataclass
class Team:
    city: str
    name: str
    abbr: str
    background: Tuple[int]
    logo_url: str
    logo_scale: float
    city_color: Tuple[int] = (255,255,255,255)
    name_color: Tuple[int] = (255,255,255,255)
    abbr_color: Tuple[int] = (255,255,255,25)

@dataclass
class League:
    logo_url: str
    logo_scale: float

def generate(
        l: League, t1: Team, t2: Team, w: int, h: int, o: str,
        background_color: Tuple[int] = (35,31,32,255),
        circles_color: Tuple[int] = (38,38,38,255),
        dots_color: Tuple[int] = (80,80,80,255),
        vs_color: Tuple[int] = (35,31,32,255),
        vs_background: Tuple[int] = (255,255,255,255),
        team_width=0.64,
        ):

    # Teams constants

    t1_rect_width = (team_width/2)*w
    t1_rect_height = t1_rect_width * 1.40625
    t1_rect_pos = [(0.5*w-t1_rect_width,0.5*h-t1_rect_height/2),(0.5*w,0.5*h+t1_rect_height/2)]
    t1_rect_width  = t1_rect_pos[1][0] - t1_rect_pos[0][0]
    t1_rect_height = t1_rect_pos[1][1] - t1_rect_pos[0][1]
    t1_logo_width = t1.logo_scale*t1_rect_width
    t1_logo_pos = (t1_rect_pos[0][0]+(t1_rect_pos[1][0]-t1_rect_pos[0][0])/2,t1_rect_pos[0][1]+(t1_rect_pos[1][1]-t1_rect_pos[0][1])/2)
    t1_city_pos = (t1_rect_pos[0][0]+(t1_rect_pos[1][0]-t1_rect_pos[0][0])/2,t1_rect_pos[0][1]+0.05*(t1_rect_pos[1][1]-t1_rect_pos[0][1]))
    t1_name_pos = (t1_rect_pos[0][0]+(t1_rect_pos[1][0]-t1_rect_pos[0][0])/2,t1_rect_pos[0][1]+0.12*(t1_rect_pos[1][1]-t1_rect_pos[0][1]))
    t1_abbr_pos = (t1_rect_pos[0][0]+(t1_rect_pos[1][0]-t1_rect_pos[0][0])/2,t1_rect_pos[0][1]+0.93*(t1_rect_pos[1][1]-t1_rect_pos[0][1]))

    t2_rect_width = t1_rect_width
    t2_rect_height = t1_rect_height
    t2_rect_pos = [(0.5*w,0.5*h-t2_rect_height/2),(0.5*w+t2_rect_width,0.5*h+t2_rect_height/2)]
    t2_rect_width  = t1_rect_pos[1][0] - t1_rect_pos[0][0]
    t2_rect_height = t1_rect_pos[1][1] - t1_rect_pos[0][1]
    t2_logo_width = t2.logo_scale*t2_rect_width
    t2_logo_pos = (t2_rect_pos[0][0]+(t2_rect_pos[1][0]-t2_rect_pos[0][0])/2,t2_rect_pos[0][1]+(t2_rect_pos[1][1]-t2_rect_pos[0][1])/2)
    t2_city_pos = (t2_rect_pos[0][0]+(t2_rect_pos[1][0]-t2_rect_pos[0][0])/2,t2_rect_pos[0][1]+0.05*(t2_rect_pos[1][1]-t2_rect_pos[0][1]))
    t2_name_pos = (t2_rect_pos[0][0]+(t2_rect_pos[1][0]-t2_rect_pos[0][0])/2,t2_rect_pos[0][1]+0.12*(t2_rect_pos[1][1]-t2_rect_pos[0][1]))
    t2_abbr_pos = (t2_rect_pos[0][0]+(t2_rect_pos[1][0]-t2_rect_pos[0][0])/2,t2_rect_pos[0][1]+0.93*(t2_rect_pos[1][1]-t2_rect_pos[0][1]))

    # League constants
    l_pos = (w/2, t2_rect_pos[1][1])
    l_width = l.logo_scale*(t1_rect_width/4)

    # Initialize image

    im = Image.new(mode="RGBA", size=(w, h))
    dr = ImageDraw.Draw(im)

    # Image background

    dr.rectangle([(0,0),(w, h)], fill=background_color)

    # Bottom left circle

    c1_pos = (0,0.78*h)
    a1_pos = (c1_pos[0]-0.09*h,c1_pos[1])
    a1_len = 0.18*h
    a2_pos = (c1_pos[0]+0.09*h,c1_pos[1])
    a2_len = 0.10*h

    dr.circle(c1_pos, (0.04*h), fill=circles_color)
    dr.circle(c1_pos, (0.4*h), outline=circles_color, width=int(0.015*h))
    dr.line([(a1_pos[0]+a1_len,a1_pos[1]+a1_len),a1_pos,(a1_pos[0]+a1_len,a1_pos[1]-a1_len)], fill=circles_color, width=int(0.015*h))
    dr.line([(a2_pos[0]+a2_len,a1_pos[1]+a2_len),a2_pos,(a2_pos[0]+a2_len,a1_pos[1]-a2_len)], fill=circles_color, width=int(0.015*h), joint='curve')

    # Top right circle

    c2_pos = (w,(1-0.78)*h)
    a3_pos = (c2_pos[0]+0.09*h,c2_pos[1])
    a3_len = 0.18*h
    a4_pos = (c2_pos[0]-0.09*h,c2_pos[1])
    a4_len = 0.10*h

    dr.circle(c2_pos, (0.04*h), fill=circles_color)
    dr.circle(c2_pos, (0.4*h), outline=circles_color, width=int(0.015*h))
    dr.line([(a3_pos[0]-a3_len,a3_pos[1]+a3_len),a3_pos,(a3_pos[0]-a3_len,a3_pos[1]-a3_len)], fill=circles_color, width=int(0.015*h))
    dr.line([(a4_pos[0]-a4_len,a4_pos[1]+a4_len),a4_pos,(a4_pos[0]-a4_len,a4_pos[1]-a4_len)], fill=circles_color, width=int(0.015*h), joint='curve')

    # Top left dots

    d1_x   = 7
    d1_y   = 22
    d1_gap = 0.018*h
    d1_pos = (0.05*h, 0.05*h)

    for x in range(d1_x+1):
        for y in range(d1_y+1):
            dr.circle((d1_pos[0]+x*d1_gap,d1_pos[1]+y*d1_gap), (0.001*h), fill=dots_color)

    # Bottom right dots

    d2_x   = 7
    d2_y   = 22
    d2_gap = 0.018*h
    d2_pos = (w-0.05*h, h-0.05*h)
    
    for x in range(d2_x+1):
        for y in range(d2_y+1):
            dr.circle((d2_pos[0]-x*d2_gap,d2_pos[1]-y*d2_gap), (0.001*h), fill=dots_color)

    # Teams zone mask (for cutting teams abbreviation)

    t1_mask_im = Image.new("L", im.size, 255)
    t1_mask_dr = ImageDraw.Draw(t1_mask_im)
    t1_mask_dr.rectangle(t1_rect_pos, fill=0)
    t2_mask_im = Image.new("L", im.size, 255)
    t2_mask_dr = ImageDraw.Draw(t2_mask_im)
    t2_mask_dr.rectangle(t2_rect_pos, fill=0)

    # Teams background

    dr.rectangle(t1_rect_pos, fill=t1.background)
    dr.rectangle(t2_rect_pos, fill=t2.background)


    # Teams header

    city_font = ImageFont.truetype('fonts/city.otf', t1_rect_width/12.8)
    name_font = ImageFont.truetype('fonts/name.otf', t1_rect_width/9.15)

    dr.text(t1_city_pos, t1.city.upper(), fill=t1.city_color, font=city_font, anchor='mm', align='center')
    dr.text(t1_name_pos, t1.name.upper(), fill=t1.name_color, font=name_font, anchor='mm', align='center')

    dr.text(t2_city_pos, t2.city.upper(), fill=t2.city_color, font=city_font, anchor='mm', align='center')
    dr.text(t2_name_pos, t2.name.upper(), fill=t2.name_color, font=name_font, anchor='mm', align='center')

    # Teams abbreviation

    abbr_font = ImageFont.truetype('fonts/name.otf', t1_rect_width/1.68)

    abbr_1_im = Image.new('RGBA', im.size, (255,255,255,0))
    abbr_1_dr = ImageDraw.Draw(abbr_1_im)
    abbr_1_dr.text(t1_abbr_pos, t1.abbr.upper(), fill=t1.abbr_color, font=abbr_font, anchor='mm', align='center')
    im_tmp = Image.alpha_composite(im, abbr_1_im)
    im = Image.composite(im, im_tmp, t1_mask_im)
    dr = ImageDraw.Draw(im)

    abbr_2_im = Image.new('RGBA', im.size, (255,255,255,0))
    abbr_2_dr = ImageDraw.Draw(abbr_2_im)
    abbr_2_dr.text(t2_abbr_pos, t2.abbr.upper(), fill=t2.abbr_color, font=abbr_font, anchor='mm', align='center')
    im_tmp = Image.alpha_composite(im, abbr_2_im)
    im = Image.composite(im, im_tmp, t2_mask_im)
    dr = ImageDraw.Draw(im)

    # Teams logo

    paste_svg(im, t1.logo_url, t1_logo_pos, t1_logo_width)
    paste_svg(im, t2.logo_url, t2_logo_pos, t2_logo_width)

    # League logo
    paste_svg(im, l.logo_url, l_pos, l_width)

    # VS text

    vs_rect_width  = t1_rect_width/8
    vs_rect_height = t1_rect_height/20
    dr.rectangle((w/2-vs_rect_width/2, h/2-vs_rect_height/2, w/2+vs_rect_width/2, h/2+vs_rect_height/2), vs_background)
    vs_font = ImageFont.truetype('fonts/vs.ttf', t1_rect_width/14.5454)
    dr.text((w/2, 0.498*h), 'VS.', fill=vs_color, font=vs_font, anchor='mm', align='center')

    im.save(o)

