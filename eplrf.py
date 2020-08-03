import pandas as pd
import numpy as np
import math

p_score_r = 0
p_score_w = 0
p_score = 0
r_score_r = 0
r_score_w = 0
r_score = 0
f1_score = 0
d_score = 0
d_score_r = 0
d_score_w = 0
home_p = 0
home_w = 0
home_l = 0
away_p = 0
away_w = 0
away_l = 0
draw_p = 0
draw_w = 0
draw_l = 0

year = 2020
#year = 2019
#year = 2018
y = str(year)
yp = str(year - 1)
r = 1
s = int(46)
tr = 553
Lg = 'EFL'
#Lg = EPL,EFL,EFL1,EFL2,SPL,IPL,GPL,FPL,DPL,MLS
# s = 381,553,553,,553,,381,381,341,381, 

#EPL/SPL
#result_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Fixtures.csv",usecols=[0,4,6,8])
result_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Fixtures.csv",usecols=[0,4,5,6])

for r in range(r, tr, 1):

    # Sim {
    g = result_raw.iat[r-1,0]
    t_1 = result_raw.iat[r-1,1]
    pos = result_raw.iat[r-1,2]
    t_2 = result_raw.iat[r-1,3]
    #po = - int(pos[0]) + int(pos[2])
    po = 0
    
    #2019/2020 EPL
    #t_1yp = t_1.replace("Norwich City", "Cardiff City").replace("Sheffield United", "Fulham").replace("Aston Villa", "Huddersfield Town")
    #t_2yp = t_2.replace("Norwich City", "Cardiff City").replace("Sheffield United", "Fulham").replace("Aston Villa", "Huddersfield Town")
    #2018/2019 EPL
    #t_1yp = t_1.replace("Cardiff City", "West Bromwich Albion").replace("Fulham", "Swansea City").replace("Wolverhampton Wanderers", "Stoke City")
    #t_2yp = t_2.replace("Cardiff City", "West Bromwich Albion").replace("Fulham", "Swansea City").replace("Wolverhampton Wanderers", "Stoke City")
    #2017/2018 EPL
    #t_1yp = t_1.replace("Brighton & Hove Albion", "Hull City").replace("Huddersfield Town", "Hull City").replace("Newcastle United", "Hull City")
    #t_2yp = t_2.replace("Brighton & Hove Albion", "Hull City").replace("Huddersfield Town", "Hull City").replace("Newcastle United", "Hull City")
 
    #2019/2020 EFL
    t_1yp = t_1.replace("Cardiff City", "Norwich City").replace("Fulham", "Sheffield Utd").replace("Huddersfield", "Aston Villa").replace("Luton Town", "Rotherham Utd").replace("Barnsley", "Bolton").replace("Charlton Ath", "Ipswich Town")
    t_2yp = t_2.replace("Cardiff City", "Norwich City").replace("Fulham", "Sheffield Utd").replace("Huddersfield", "Aston Villa").replace("Luton Town", "Rotherham Utd").replace("Barnsley", "Bolton").replace("Charlton Ath", "Ipswich Town")
    #2018/2019 EFL
    #t_1yp = t_1.replace("Swansea City", "Wolves").replace("Stoke City", "Cardiff City").replace("West Brom", "Fulham").replace("Wigan Athletic", "Barnsley").replace("Blackburn", "Burton Albion").replace("Rotherham Utd", "Sunderland")
    #t_2yp = t_2.replace("Swansea City", "Wolves").replace("Stoke City", "Cardiff City").replace("West Brom", "Fulham").replace("Wigan Athletic", "Barnsley").replace("Blackburn", "Burton Albion").replace("Rotherham Utd", "Sunderland")

    #2018/2019 SPL
    #t_1yp = t_1.replace("Huesca", "La Coruña").replace("Rayo Vallecano", "Las Palmas").replace("Valladolid", "Málaga")
    #t_2yp = t_2.replace("Huesca", "La Coruña").replace("Rayo Vallecano", "Las Palmas").replace("Valladolid", "Málaga")

    tmcom = t_1 + t_2
    odds_raw_tm = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Odds.csv")
    odds_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Odds.csv", usecols=[2,3,4])
    oddstm = odds_raw_tm['Team1'] + odds_raw_tm['Team2']
    oddstmcom = oddstm.to_frame().join(odds_raw)
    odds = oddstmcom.rename(columns={0:'Team'})
    h_o = odds.loc[odds["Team"]==str(tmcom), "H"]
    d_o = odds.loc[odds["Team"]==str(tmcom), "D"]
    a_o = odds.loc[odds["Team"]==str(tmcom), "A"]
    #rh = int(h_o)
    #rd = int(d_o)
    #ra = int(a_o)
    rh = 100
    rd = 100
    ra = 100
    if rh <= 0:
        rh = - rh / (- rh + 100)
    elif rh > 0:
        rh = 100 / (rh + 100)
    if rd <= 0:
        rd = - rd / (- rd + 100)
    elif rd > 0:
        rd = 100 / (rd + 100)
    if ra <= 0:
        ra = - ra / (- ra + 100)
    elif ra > 0:
        ra = 100 / (ra + 100)
    tr = rh + rd + ra
    hl = rh / tr
    dl = rd / tr
    al = ra / tr
    hld = 1 / hl
    dld = 1 / dl
    ald = 1 / al

    h_1 = 0.2
    h_2 = 0
    # }

    # reads the csv files and gathers variables for each team(points for and against in current and prior year)
    # pyp/py: points for year prior/current year; oyp/oy: points against year prior/current year
    pyp = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+yp+".csv",usecols=[1,6])
    pyp_1 = pyp.loc[pyp["Squad"]==str(t_1yp), "GF"]
    pyp_2 = pyp.loc[pyp["Squad"]==str(t_2yp), "GF"]
    oyp = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+yp+".csv",usecols=[1,7])
    oyp_1 = oyp.loc[oyp["Squad"]==str(t_1yp), "GA"]
    oyp_2 = oyp.loc[oyp["Squad"]==str(t_2yp), "GA"]
    ypg = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+yp+".csv",usecols=[1,2])
    ypg_1 = ypg.loc[ypg["Squad"]==str(t_1yp), "MP"] 
    ypg_2 = ypg.loc[ypg["Squad"]==str(t_2yp), "MP"]
    
    rfgl = 5

    if g >= rfgl:
        recent_form_raw_tm = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Fixtures.csv")
        #EPL/SPL
        #recent_form_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Fixtures.csv", usecols=[0,4,6,8])
        recent_form_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+y+"Fixtures.csv", usecols=[0,4,5,6])
        recentformtm = recent_form_raw_tm['Home'] + '-' + recent_form_raw_tm['Away']
        recentformtmcom = recentformtm.to_frame().join(recent_form_raw)
        recentraw = recentformtmcom.rename(columns={0:'Team'})
        recent = recentraw.set_index(['Team', 'Wk'])
        tablefilter1 = recent.filter(like=t_1, axis=0)
        rfg = g - 1
        rfgm = g - (rfgl + 1)
        gf_1 = 0
        ga_1 = 0
        for rfg in range(rfg,rfgm,-1):
            recentgame = tablefilter1.filter(like=str(rfg),axis=0).head(1)
            if t_1 == recentgame.iloc[0,0]:
                gf_1 += int(recentgame.iloc[0,1][0])
                ga_1 += int(recentgame.iloc[0,1][2])
            if t_1 == recentgame.iloc[0,2]:
                gf_1 += int(recentgame.iloc[0,1][2])
                ga_1 += int(recentgame.iloc[0,1][0])

        tablefilter2 = recent.filter(like=t_2, axis=0)
        rfg = g - 1
        rfgm = g - (rfgl + 1)
        gf_2 = 0
        ga_2 = 0
        for rfg in range(rfg,rfgm,-1):
            recentgame = tablefilter2.filter(like=str(rfg),axis=0).head(1)
            if t_2 == recentgame.iloc[0,0]:
                gf_2 += int(recentgame.iloc[0,1][0])
                ga_2 += int(recentgame.iloc[0,1][2])
            if t_2 == recentgame.iloc[0,2]:
                gf_2 += int(recentgame.iloc[0,1][2])
                ga_2 += int(recentgame.iloc[0,1][0])

    elif g < rfgl:
        recent_form_raw_tm = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+yp+"Fixtures.csv")
        #EPL/SPL
        #recent_form_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+yp+"Fixtures.csv", usecols=[0,4,6,8])
        recent_form_raw = pd.read_csv("/Users/Dallon/Desktop/Python_Stuff/Sports_App/"+Lg+"_Team_Data/"+Lg+yp+"Fixtures.csv", usecols=[0,4,5,6])
        recentformtm = recent_form_raw_tm['Home'] + '-' + recent_form_raw_tm['Away']
        recentformtmcom = recentformtm.to_frame().join(recent_form_raw)
        recentraw = recentformtmcom.rename(columns={0:'Team'})
        recent = recentraw.set_index(['Team', 'Wk'])
        tablefilter1 = recent.filter(like=t_1yp, axis=0)
        rfg = s
        rfgm = s - rfgl
        gf_1 = 0
        ga_1 = 0
        for rfg in range(rfg,rfgm,-1):
            recentgame = tablefilter1.filter(like=str(rfg),axis=0).head(1)
            if t_1yp == recentgame.iloc[0,0]:
                gf_1 += int(recentgame.iloc[0,1][0])
                ga_1 += int(recentgame.iloc[0,1][2])
            if t_1yp == recentgame.iloc[0,2]:
                gf_1 += int(recentgame.iloc[0,1][2])
                ga_1 += int(recentgame.iloc[0,1][0])

        tablefilter2 = recent.filter(like=t_2yp, axis=0)
        rfg = s
        rfgm = s - rfgl
        gf_2 = 0
        ga_2 = 0
        for rfg in range(rfg,rfgm,-1):
            recentgame = tablefilter2.filter(like=str(rfg),axis=0).head(1)
            if t_2yp == recentgame.iloc[0,0]:
                gf_2 += int(recentgame.iloc[0,1][0])
                ga_2 += int(recentgame.iloc[0,1][2])
            if t_2yp == recentgame.iloc[0,2]:
                gf_2 += int(recentgame.iloc[0,1][2])
                ga_2 += int(recentgame.iloc[0,1][0])
    
    py_1 = gf_1
    py_2 = gf_2
    oy_1 = ga_1
    oy_2 = ga_2
    yg_1 = rfgl
    yg_2 = rfgl

    # takes variables from above and generates mean for points for and against
    mmpyp_1 = pyp_1 / ypg_1
    mmpy_1 = py_1 / yg_1
    mmoyp_1 = oyp_1 / ypg_1
    mmoy_1 = oy_1 / yg_1
    mmpyp_2 = pyp_2 / ypg_2
    mmpy_2 = py_2 / yg_2
    mmoyp_2 = oyp_2 / ypg_2
    mmoy_2 = oy_2 / yg_2

    # takes mean and calculates a weighted average between current and prior season
    ypw = .5
    yw = .5
    mmp_1 = float(mmpyp_1 * ypw + mmpy_1 * yw)
    mmo_1 = float(mmoyp_1 * ypw + mmoy_1 * yw)   
    mmp_2 = float(mmpyp_2 * ypw + mmpy_2 * yw)
    mmo_2 = float(mmoyp_2 * ypw + mmoy_2 * yw)  

    m_1 = mmp_1 * .5 + mmo_2 * .5
    m_2 = mmo_1 * .5 + mmp_2 * .5
    mm_1 = m_1 + h_1
    mm_2 = m_2 + h_2
    k_1 = 0
    k_2 = 0
    km = 11
    p_1 = 0
    p_2 = 0
    d = 0
    ou = mm_1 + mm_2
    t = {}

    for k_1 in range(k_1, km, 1):
        p1 = (math.e**-mm_1 * mm_1**k_1) / math.factorial(k_1)
        k_2 = 0
        for k_2 in range(k_2, km, 1):
            p2 = (math.e**-mm_2 * mm_2**k_2) / math.factorial(k_2)
            p = p1 * p2
            if k_1 > k_2:
                p_1 += p
            if k_1 == k_2:
                d += p
            if k_1 < k_2:
                p_2 += p

    k = 0
    for k in range(k, km, 1):
        tou = ((math.e**-ou * ou**k) / math.factorial(k)) * ((math.e**-ou * ou**k) / math.factorial(k))
        t[k] = (round(tou, 4))
        tp = max(t, key=lambda key: t[key])
    
    ln = - mm_1 + mm_2
    mm = (- p_1 + p_2) * 100
    dd = d * 100
    pp_1 = p_1 * 100
    pp_2 = p_2 * 100
    mld = 1.33
    moe = 0
    #.249
    dp = 0

    #if p_1 > hl and po < 0 and p_1 - hl >= moe:
    if p_1 > p_2 and po < 0 and hld >= mld:
        home_p += 1
        #home_w += 100 * (hld - 1)
        home_w += 100
    #elif p_1 > hl and po >= 0 and p_1 - hl >= moe:
    elif p_1 > p_2 and po >= 0 and hld >= mld:
        home_p += 1
        #home_l += 100
        home_l += - 100 / (1 - hld)
    elif p_1 > p_2 and po > 0 and hld < mld:
        away_p += 1
        away_w += 100
    elif p_1 > p_2 and po <= 0 and hld < mld:
        away_p += 1
        away_l += 100 / (1 - ald)

    #if p_2 > al and po > 0 and p_2 - al >= moe:
    if p_2 > p_1 and po > 0 and ald >= mld:
        away_p += 1
        #away_w += 100 * (ald - 1)
        away_w += 100
    #elif p_2 > al and po <= 0 and p_2 - al >= moe:
    elif p_2 > p_1 and po <= 0 and ald >= mld:
        away_p += 1
        #away_l += 100
        away_l += - 100 / (1 - ald)
    elif p_2 > p_1 and po < 0 and ald < mld:
        home_p += 1
        home_w += 100
    elif p_2 > p_1 and po >= 0 and ald < mld:
        home_p += 1
        home_l += 100 / (1 - hld)

    #if d > dl and po == 0:
    if po == 0 and dl >= dp:
        draw_p += 1
        #draw_w += 100 * (dld - 1)
        draw_w += 20
    #elif d > dl and po != 0:
    elif dl >= dp and po != 0:
        draw_p += 1
        #draw_l += 20
        draw_l += - 20 / (1 - dld)

    #print(g, t_1, round((p_1 - hl), 3), t_2, round((p_2 - al), 3), str('Draw'), round((d - dl), 3),pos, sep=',')
    #print('Home', home_p, int(home_w), int(home_l), 'Draw', draw_p, int(draw_w), int(draw_l), 'Away', away_p, int(away_w), int(away_l), sep=',')

    if po < 0 and mm < 0:
        p_score_r += 1
    elif po > 0 and mm > 0:
        r_score_r += 1
    elif po <= 0 and mm > 0:
        r_score_w += 1
    elif po >= 0 and mm < 0:
        p_score_w += 1
    #if d > dl and po == 0:
    if po == 0 and dl >= dp:
        d_score_r += 1
    #elif d > dl and po != 0:
    elif po != 0 and dl >= dp:
        d_score_w += 1

    print(g, t_1, str(round(pp_1, 0))+'%', pos, t_2, str(round(pp_2, 0))+'%', 'Draw', str(round(dd, 0))+'%', sep=',')
    r += 1

total = home_w - home_l + away_w - away_l
per_bet = total / (home_p + away_p)
print('Home', home_p, int(home_w), int(home_l), 'Draw', draw_p, int(draw_w), int(draw_l), 'Away', away_p, int(away_w), int(away_l), 'Profit', int(total), 'ProfPerBet', int(per_bet), sep=',')
p_score = (p_score_r / (p_score_r + p_score_w))
r_score = (r_score_r / (r_score_r + r_score_w))
f1_score = ((p_score_r + r_score_r) / (p_score_r + p_score_w + r_score_r + r_score_w))
d_score = (d_score_r / (d_score_r + d_score_w))
print('f1_score', round(f1_score, 4), 'd_score', round(d_score, 4), sep=',')