import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timezone
import pytz

# Page layout
st.set_page_config(
    page_title='Home',
    page_icon = '🏠',
    layout = 'wide'
)

### Clock ###
pst = pytz.timezone("Asia/Manila")

@st.fragment(run_every="1s")
def show_clock():
    now_local = datetime.now(pst)
    now_utc = now_local.astimezone(timezone.utc)
    clocks = st.container(horizontal=True, horizontal_alignment='center')
    
    clock1 = clocks.container(width=480, border=True)
    clock1_str = f"PhST: **{now_local.strftime('%B %d, %Y (%A)   %I:%M:%S %p | %H:%M:%SH')}**"
    clock1.markdown(clock1_str)
    
    clock2 = clocks.container(width=370, border=True)
    clock2_str = f"UTC: **{now_utc.strftime('%B %d, %Y (%A)   %H:%M:%S')}**"
    clock2.markdown(clock2_str)

show_clock()

########################
### Homepage content ###
########################

# Headers
st.write('### Local Government Unit of Guiuan, Eastern Samar – Municipal Disaster Risk Reduction and Management Office (MDRRMO)')
st.write('# WEATHER UPDATE DASHBOARD')
st.write('This dashboard contains various meteorological information, advisories and/or warnings from DOST-PAGASA and other reliable sources, especially those that are relevant to the municipality of Guiuan, Eastern Samar and including other important general/nationwide updates.')

# Setting tabs for nationwide and local weather synopses
guiuan_tab, nationwide_tab = st.tabs(['Guiuan', 'Nationwide'])

# Guiuan synopsis
with guiuan_tab:
    components.html(
        '<iframe width="1260" height="600" src="https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=mm&metricTemp=°C&metricWind=km/h&zoom=8&overlay=satellite&product=satellite&level=surface&lat=11.1&lon=125.7&pressure=true" frameborder="0"></iframe>',
        height=610
        )
    components.html(
        '<iframe width="100%" height="187" src="https://embed.windy.com/embed.html?type=forecast&location=coordinates&detail=true&detailLat=11.034096325792703&detailLon=125.7222905312513&metricTemp=°C&metricRain=mm&metricWind=km/h" frameborder="0"></iframe>',
        height=197
        )
    st.write('### Weather in Guiuan, Eastern Samar')
    
    wxsystem, generalfcst, impact = st.columns(3)
    with wxsystem:
        st.write('*Weather system:*')
        localwxsys = st.container(border=True)
        localwxsys.write('**Southwest monsoon (***Habagat***)**')
    with generalfcst:
        st.write('*General forecast of weather conditions:*')
        localwxsynop = st.container(border=True, horizontal_alignment='center')
        
        wxicon = localwxsynop.container(width=95)
        wxicon.image('static/Partly cloudy to cloudy skies with isolated thunderstorms.png',
                     width=90)
        
        localwxsynoptext = localwxsynop.container()    
        localwxsynoptext.write(
            '''
            Partly cloudy to cloudy skies with possible rainshowers and/or thunderstorms (especially in the afternoon and/or evening)
            '''
            )
    with impact:
        st.write('*Potential impacts:*')
        localwxsys = st.container(border=True)
        localwxsys.write(
            '''
            Localized thunderstorm activity may trigger urban and riverine flash floods and/or landslides due to moderate to at times heavy rains (isolated intense to torrential downpours possible)
            - Note: When thunderstorms become severe, impacts may also include damaging winds, hail, lightning strikes and/or tornadoes/waterspouts.
            ''')

    ### Summary of latest weather observation data ###
    st.write('### Data from the DOST-PAGASA Guiuan Weather Station')
    st.write('*As of 2:00 PM, 28 August 2025:*')
    
    # Setting up row 1
    wxdata1 = st.container(horizontal=True)
    wxdata1_icon = wxdata1.container(width=50, vertical_alignment='center')
    wxdata1_icon.image('static/temp.png',
                 width=50)
    
    # Temperature
    temp = wxdata1.container(border=True)
    temp.metric('Temperature', '31.2°C')
    
    # Heat index
    hi = wxdata1.container(border=True, horizontal=True,
                           vertical_alignment='center', width=280)
    himetric = hi.container()
    hi.metric('Feels like', '39.5°C')
    hibadge = hi.container()
    hi.badge('Extreme caution', icon='⚠️', color='orange')
    
    # Relative humidity
    rh = wxdata1.container(border=True)
    rh.metric('Humidity', '74%')
    
    # Setting up row 2
    wxdata2 = st.container(horizontal=True)
    wxdata2_icon = wxdata2.container(width=110, vertical_alignment='center')
    wxdata2_icon.image('static/wind.png',
                 width=110)
    
    # Wind
    wind = wxdata2.container(border=True, width=195)
    windspeed = wind.container()
    windspeed.metric('Wind speed', '30 km/h')
    winddir = wind.container(horizontal=True, vertical_alignment='center')
    winddir.metric('Wind direction', 'SW')
    winddir.image('static/Wind - 11 (SW).png', width=60)

# Nationwide synopsis
with nationwide_tab:
    components.html(
        '<iframe width="1260" height="600" src="https://embed.windy.com/embed.html?type=map&location=coordinates&metricRain=mm&metricTemp=°C&metricWind=km/h&zoom=5&overlay=satellite&product=satellite&level=surface&lat=14.6&lon=128&pressure=true" frameborder="0"></iframe>',
        height=610
        )
    st.write('### Synopsis')

    natlwxsynop = st.container(border=True)
    natlwxsynop.write(
        '''
        - At 3:00 AM today, the center of **Low Pressure Area “08i”** was estimated based on all available at 570 km East-northeast of Virac, Catanduanes or 695 km East of Daet, Camarines Norte (14.6°N, 129.4°E). It is affecting the Bicol Region and the eastern portions of Central Luzon and Calabarzon.
        - The **southwest monsoon (***Habagat***)** is affecting the western sections of Central and Southern Luzon, Visayas, and the northern section of Mindanao.
        '''
        )
    
    # Meteorological charts
    st.write('### Meteorological maps from DOST-PAGASA')
    synopchart1, synopchart2, streamline = st.columns(3)
    with synopchart1:
        st.write('Latest surface synoptic analysis chart')
        st.image('https://pubfiles.pagasa.dost.gov.ph/tamss/weather/surface_map.jpg')
    with synopchart2:
        st.write('Predicted mean sea level pressure analysis for 8:00 AM today, 29 September 2025')
        st.image('https://pubfiles.pagasa.dost.gov.ph/tamss/weather/chart.png')
    with streamline:
        st.write('Predicted mean sea level wind analysis for 8:00 AM today, 1 September 2025')
        st.image('https://pubfiles.pagasa.dost.gov.ph/tamss/weather/we98.png')


# End of program