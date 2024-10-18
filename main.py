from generator import League, Team, generate
from utils import init_out_dir
import os

nhl = League('https://upload.wikimedia.org/wikipedia/sco/3/3a/05_NHL_Shield.svg', 1.0)

teams = [ 
    Team('Anaheim',      'Ducks',          'ana', (207,69 ,32 ,255), 'https://assets.nhle.com/logos/nhl/svg/ANA_dark.svg' , 1.2),
    Team('Arizona',      'Coyotes',        'ari', (111,38 ,61 ,255), 'https://assets.nhle.com/logos/nhl/svg/ARI_dark.svg' , 1.2),
    Team('Boston',       'Bruins',         'bos', (255,184,28 ,255), 'https://assets.nhle.com/logos/nhl/svg/BOS_dark.svg' , 1.2),
    Team('Buffalo',      'Sabres',         'buf', (0,  48 ,135,255), 'https://assets.nhle.com/logos/nhl/svg/BUF_dark.svg' , 1.2),
    Team('Carolina',     'Hurricanes',     'car', (200,16 ,46 ,255), 'https://assets.nhle.com/logos/nhl/svg/CAR_dark.svg' , 1.0),
    Team('Columbus',     'Blue Jackets',   'cbj', (4  ,30 ,66 ,255), 'https://assets.nhle.com/logos/nhl/svg/CBJ_dark.svg' , 1.2),
    Team('Calgary',      'Flames',         'cgy', (200,16 ,46 ,255), 'images/nhl-cgy.svg'                                 , 1.2),
    Team('Chicago',      'Blackhawks',     'chi', (206,17 ,38 ,255), 'https://assets.nhle.com/logos/nhl/svg/CHI_dark.svg' , 1.2),
    Team('Colorado',     'Avalanche',      'col', (138,36 ,50 ,255), 'https://assets.nhle.com/logos/nhl/svg/COL_dark.svg' , 1.2),
    Team('Dallas',       'Stars',          'dal', (0  ,130,62 ,255), 'https://assets.nhle.com/logos/nhl/svg/DAL_dark.svg' , 1.2),
    Team('Detroit',      'Red Wings',      'det', (200,16 ,46 ,255), 'https://assets.nhle.com/logos/nhl/svg/DET_dark.svg' , 0.9),
    Team('Edmonton',     'Oilers',         'edm', (209,69 ,32 ,255), 'https://assets.nhle.com/logos/nhl/svg/EDM_dark.svg' , 1.2),
    Team('Florida',      'Panthers',       'fla', (200,16 ,46 ,255), 'https://assets.nhle.com/logos/nhl/svg/FLA_dark.svg' , 1.2),     
    Team('Los Angeles',  'Kings',          'lak', (162,170,173,255), 'https://assets.nhle.com/logos/nhl/svg/LAK_dark.svg' , 0.85),    
    Team('Minnesota',    'Wild',           'min', (14 ,68 ,49 ,255), 'https://assets.nhle.com/logos/nhl/svg/MIN_dark.svg' , 0.90),       
    Team('Montreal',     'Canadiens',      'mtl', (166,25 ,46 ,255), 'https://assets.nhle.com/logos/nhl/svg/MTL_dark.svg' , 1.05),   
    Team('New Jersey',   'Devils',         'njd', (204,0  ,0  ,255), 'https://assets.nhle.com/logos/nhl/svg/NJD_dark.svg' , 1.2),    
    Team('Nashville',    'Predators',      'nsh', (255,184,28 ,255), 'https://assets.nhle.com/logos/nhl/svg/NSH_dark.svg' , 1.0),  
    Team('New York',     'Islanders',      'nyi', (0  ,70 ,139,255), 'https://assets.nhle.com/logos/nhl/svg/NYI_dark.svg' , 1.2),   
    Team('New York',     'Rangers',        'nyr', (21 ,75 ,148,255), 'https://assets.nhle.com/logos/nhl/svg/NYR_dark.svg' , 1.2),     
    Team('Ottawa',       'Senators',       'ott', (200,16 ,46 ,255), 'https://assets.nhle.com/logos/nhl/svg/OTT_dark.svg' , 1.0),      
    Team('Philadelphia', 'Flyers',         'phi', (210,67 ,3  ,255), 'https://assets.nhle.com/logos/nhl/svg/PHI_dark.svg' , 1.1),  
    Team('Pittsburgh',   'Penguins',       'pit', (255,184,28 ,255), 'https://assets.nhle.com/logos/nhl/svg/PIT_dark.svg' , 1.2),  
    Team('Seattle',      'Kraken',         'sea', (150,216,216,255), 'https://assets.nhle.com/logos/nhl/svg/SEA_dark.svg' , 1.2),       
    Team('San Jose',     'Sharks',         'sjs', (0  ,119,139,255), 'https://assets.nhle.com/logos/nhl/svg/SJS_dark.svg' , 1.1),      
    Team('St. Louis',    'Blues',          'stl', (0  ,73 ,134,255), 'https://assets.nhle.com/logos/nhl/svg/STL_dark.svg' , 1.0),      
    Team('Tampa Bay',    'Lightning',      'tbl', (0  ,32 ,91 ,255), 'https://assets.nhle.com/logos/nhl/svg/TBL_dark.svg' , 1.1),  
    Team('Toronto',      'Maple Leafs',    'tor', (0  ,32 ,91 ,255), 'https://assets.nhle.com/logos/nhl/svg/TOR_dark.svg' , 1.2),  
    Team('Utah',         'Hockey Club',    'uta', (1  ,1  ,1  ,255), 'https://assets.nhle.com/logos/nhl/svg/UTA_dark.svg' , 1.2),  
    Team('Vancouver',    'Canucks',        'van', (0  ,32 ,91 ,255), 'https://assets.nhle.com/logos/nhl/svg/VAN_dark.svg' , 1.1),    
    Team('Vegas',        'Golden Knights', 'vgk', (185,151,91 ,255), 'https://assets.nhle.com/logos/nhl/svg/VGK_dark.svg' , 1.2), 
    Team('Winnipeg',     'Jets',           'wpg', (4  ,30 ,66 ,255), 'https://assets.nhle.com/logos/nhl/svg/WPG_dark.svg' , 1.2),        
    Team('Washington',   'Capitals',       'wsh', (200,16 ,46 ,255), 'images/nhl-wsh.svg'                                 , 0.8)  
]


out_dir = init_out_dir()

for t1 in teams:
    for t2 in teams:
        if t1 == t2: continue
        generate(nhl, t1, t2, 1280, 720, os.path.join(out_dir, f'nhl_{t1.abbr}_{t2.abbr}_thumbnail.png'))
        generate(nhl, t1, t2, 680, 1000, os.path.join(out_dir, f'nhl_{t1.abbr}_{t2.abbr}_poster.png'), team_width=1.00)
        generate(nhl, t1, t2, 1000, 1000, os.path.join(out_dir, f'nhl_{t1.abbr}_{t2.abbr}_square.png'), team_width=1.00)

