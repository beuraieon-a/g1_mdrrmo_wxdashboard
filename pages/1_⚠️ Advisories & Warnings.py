import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timezone
import pytz

# Page layout
st.set_page_config(layout = 'wide')

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

st.write('### ⚠️ Advisories & Warnings over Guiuan, Eastern Samar')
st.write('Note: Available maps of the warning areas and the meanings of the advisory/warning icons can be found below the advisory/warning dashboard.')

# Setting tabs for weather-related and climate-related advisories and warnings
weather_tab, climate_tab = st.tabs(['Weather', 'Climate'])

# Weather advisories & warnings
with weather_tab:
    # Setting row 1
    wxrow1 = st.container(horizontal=True, horizontal_alignment='center')
    
    # Thunderstorm
    tstm = wxrow1.container(width=300)
    tstm.write('##### Thunderstorm')
    
    tstm_content = tstm.container(horizontal_alignment='center', vertical_alignment = 'center', border=True)

    tstm_content_icon = tstm_content.container(width=150)
    tstm_content_icon.image('static/rainwarning_00_tstmadv.png')

    tstm_content_caption = tstm_content.container()
    tstm_issuance_time = 'as of 10:00 AM 31 August 2025'
    tstm_content_caption.markdown(f"<p style='text-align: center;'><small>{tstm_issuance_time}</small></p>",
                                  unsafe_allow_html=True)

    with tstm.expander('Details'):
        st.write(
            '''
            Moderate to heavy rainshowers with possible isolated intense downpours, accompanied with lightning and strong winds, are ongoing or likely to occur within 1-2 hours.
            '''
            )
    
    # Long-duration rainfall (includes Rainfall Advisory and Heavy Rainfall Warning)
    rain = wxrow1.container(width=300)
    rain.write('##### Long-duration rainfall')
    
    rain_content = rain.container(horizontal_alignment='center', vertical_alignment = 'center', border=True)

    rain_content_icon = rain_content.container(width=150)
    rain_content_icon.image('static/rainwarning_03_orangehrwl.png')

    rain_content_caption = rain_content.container()
    rain_issuance_time = 'as of 10:00 AM 31 August 2025'
    rain_content_caption.markdown(f"<p style='text-align: center;'><small>{rain_issuance_time}</small></p>",
                                  unsafe_allow_html=True)
    
    with rain.expander('Details'):
        st.write(
            '''
            Long-duration intense rainfall is ongoing or likely to occur within 2-3 hours. Flooding is threatening, or severe flooding is about to occur, in areas that are urbanized, low-lying, and/or near rivers or streams. Landslides are likely to occur in hilly or mountainous areas.
            '''
            )

    # Weather advisory (3-day heavy rainfall outlook)
    wahr = wxrow1.container(width=300)
    wahr.write('##### Weather advisory')
    
    wahr_content = wahr.container(horizontal_alignment='center', vertical_alignment = 'center', border=True)

    wahr_content_icon = wahr_content.container(width=150)
    wahr_content_icon.image('static/hvyrainoutlook2.png')

    wahr_content_caption = wahr_content.container()
    wahr_issuance_time = 'as of 10:00 AM 31 August 2025'
    wahr_content_caption.markdown(f"<p style='text-align: center;'><small>{wahr_issuance_time}</small></p>",
                                  unsafe_allow_html=True)
    
    with wahr.expander('Details'):
        st.write(
            '''
            24-hour (daily) accumulated rainfall of 100-200 millimeters is possible today (September 1) until tomorrow aftenoon (September 2). Numerous flooding events are likely, especially in areas that are urbanized, low-lying, and/or near rivers or streams. Landslide likely in moderate to highly susceptible areas.
            '''
            )

    # Marine gale
    gale = wxrow1.container(width=300)
    gale.write('##### Marine gale')
    
    gale_content = gale.container(horizontal_alignment='center', vertical_alignment = 'center', border=True)

    gale_content_icon = gale_content.container(width=150)
    gale_content_icon.image('static/galewarning_beaufort8-9.png')

    gale_content_caption = gale_content.container()
    gale_issuance_time = 'as of 10:00 AM 31 August 2025'
    gale_content_caption.markdown(f"<p style='text-align: center;'><small>{gale_issuance_time}</small></p>",
                                  unsafe_allow_html=True)

    with gale.expander('Details'):
        st.write(
            '''
            Strong to gale-force winds are prevailing or expected, causing rough to very rough seas. Sea travel is risky for small seacrafts (including all motor bancas of any type or tonnage). Mariners of these vessels are advised to remain in port or seek safe harbor. For larger vessels, operating in these conditions require experience and properly equipped vessels
            '''
            )
    
    # Setting row 2
    wxrow2 = st.container(horizontal=True, horizontal_alignment='center')

    # Tropical cyclone wind signal
    tcws = wxrow2.container(width=300)
    tcws.write('##### Tropical cyclone winds')
    
    tcws_content = tcws.container(horizontal_alignment='center', vertical_alignment = 'center', border=True)

    tcws_content_icon = tcws_content.container(horizontal=True, horizontal_alignment='center', vertical_alignment = 'center')

    tcws_content_icon_tccat = tcws_content_icon.container(width=70)
    tcws_content_icon_tccat.image('static/TCcat_03_STS.png')

    tcws_content_icon_warn = tcws_content_icon.container(width=150)
    tcws_content_icon_warn.image('static/tcws2.png')

    tcws_content_caption = tcws_content.container()
    tcws_issuance_time = 'as of 10:00 AM 31 August 2025'
    tcws_content_caption.markdown(f"<p style='text-align: center;'><small>{tcws_issuance_time}</small></p>",
                                  unsafe_allow_html=True)

    with tcws.expander('Details'):
        st.write(
            '''
            Gale-force to severe gale-force winds are prevailing or expected to occur within 24 hours due to a tropical cyclone, posing minor to moderate threat to life and property.
            '''
            )

    # Storm surge
    stsurge = wxrow2.container(width=300)
    stsurge.write('##### Storm surge')
    
    stsurge_content = stsurge.container(horizontal_alignment='center', vertical_alignment = 'center', border=True)

    stsurge_content_icon = stsurge_content.container(width=150)
    stsurge_content_icon.image('static/stormsurgewarning2.png')

    stsurge_content_caption = stsurge_content.container()
    stsurge_issuance_time = 'as of 10:00 AM 31 August 2025'
    stsurge_content_caption.markdown(f"<p style='text-align: center;'><small>{stsurge_issuance_time}</small></p>",
                                     unsafe_allow_html=True)

    with stsurge.expander('Details'):
        st.write(
            '''
            There is a moderate to high risk of storm surge with heights of 2-3 meters within 24 hours due to a tropical cyclone. Severe damage is expected to communities and coastal/marine infrastructures, along with significant coastal erosion. Riverine flooding due to forced/induced upstream flow by the storm surge is also likely.
            '''
            )
    
    st.write('### Maps of the advisory/warning areas')

    # Setting row 1
    maprow1 = st.container(horizontal=True, horizontal_alignment='center')
    
    # Map: Thunderstorm
    map_tstm = maprow1.container(width=600)
    map_tstm.write('##### Thunderstorm')
    
    map_tstm_content = map_tstm.container(border=True)
    map_tstm_content.image('static/map_tstm.jpg')

    # Map: Long-duration rainfall (includes Rainfall Advisory and Heavy Rainfall Warning)
    map_rain = maprow1.container(width=600)
    map_rain.write('##### Long-duration rainfall')
    
    map_rain_content = map_rain.container(border=True)
    map_rain_content.image('static/map_rainadv.jpg')

    # Setting row 2
    maprow2 = st.container(horizontal=True, horizontal_alignment='center')
    
    # Map: Heavy rainfall
    map_hrw = maprow2.container(width=600)
    map_hrw.write('##### Heavy rainfall')
    
    map_hrw_content = map_hrw.container(border=True)
    map_hrw_content.image('static/map_hrw.png')

    # Map: Weather advisory (3-day heavy rainfall outlook)
    map_wahr = maprow2.container(width=600)
    map_wahr.write('##### Weather advisory')
    
    map_wahr_content = map_wahr.container(border=True, height=401)
    map_wahr_content.image('static/map_weatheradv1.jpg')
    map_wahr_content.image('static/map_weatheradv2.jpg')
    map_wahr_content.image('static/map_weatheradv3.jpg')

    # Setting row 3
    maprow3 = st.container(horizontal=True, horizontal_alignment='center')
    
    # Map: Tropical cyclone winds
    map_tcws = maprow3.container(width=600)
    map_tcws.write('##### Tropical cyclone winds')
    
    map_tcws_content = map_tcws.container(border=True)
    map_tcws_content.image('static/map_tcws.png')

    # Map: Storm surge
    map_stsurge = maprow3.container(width=600)
    map_stsurge.write('##### Storm surge')
    
    map_stsurge_content = map_stsurge.container(border=True)
    map_stsurge_content.image('static/map_stsurge.jpg')

    # Legend for the advisory/warning icons
    st.write('### Legend')

    col1, col2 = st.columns(2)

    with col1:
        # Legend: Thunderstorm Advisory
        legend_tstm = st.container(width = 600)
        legend_tstm.write('##### Thunderstorm')
        legend_tstm_content = legend_tstm.container(horizontal=True, horizontal_alignment='left',
                                                    vertical_alignment = 'center', border=True)

        legend_tstm_content_icon = legend_tstm_content.container(width=100)
        legend_tstm_content_icon.image('static/rainwarning_00_tstmadv.png')

        legend_tstm_content_text = legend_tstm_content.container()
        legend_tstm_content_text.write('##### Thunderstorm Advisory')
        legend_tstm_content_text.write(
            '''
            Moderate to heavy rainshowers with possible isolated intense downpours, accompanied with lightning and strong winds, ongoing or likely to occur within 30 minutes to 1-2 hours
            - WARNING: If PAGASA meteorologists assess the thunderstorm to have intensified into a "severe thunderstorm", or if forecasts indicate a likelihood of severe thunderstorm activity, the **Thunderstorm Advisory** can be expanded to include severe hazards such as intense to torrential rains, hail, damaging storm-force to typhoon-force winds (esp. when the thunderstorm produces downbursts), and/or tornadoes or waterspouts
            ''')
        
        # Legend: Long-duration rainfall

        legend_rain = st.container(width = 600)
        legend_rain.write('##### Long-duration rainfall')
        legend_rain_content = legend_rain.container(border=True)
        legend_rain_content.write('##### Rainfall Advisory')

        legend_rain_content_ra = legend_rain_content.container(horizontal=True, horizontal_alignment='left',
                                                                vertical_alignment = 'center')
        legend_rain_content_raicon = legend_rain_content_ra.container(width=100)
        legend_rain_content_raicon.image('static/rainwarning_01_rainfalladvisory.png')

        legend_rain_content_ratext = legend_rain_content_ra.container()
        legend_rain_content_ratext.write('Long-duration light to moderate rains, with possible isolated heavy downpours, ongoing or likely to occur within 2-3 hours')

        legend_rain_content.write('##### Heavy Rainfall Warning')

        legend_rain_content_hrw1 = legend_rain_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_rain_content_hrw1icon = legend_rain_content_hrw1.container(width=100)
        legend_rain_content_hrw1icon.image('static/rainwarning_02_yellowhrwl.png')

        legend_rain_content_hrw1text = legend_rain_content_hrw1.container()
        legend_rain_content_hrw1text.write('***Yellow Warning Level***')
        legend_rain_content_hrw1text.write(
            '''
            Long-duration heavy rainfall (rainfall intensity of 7.5-15 mm/h) ongoing or likely to occur within 2-3 hours
            - Flooding is possible in areas that are urbanized, low-lying, and/or near rivers or streams
            - Landslides are possible in hilly or mountainous areas
            ''')

        legend_rain_content_hrw2 = legend_rain_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_rain_content_hrw2icon = legend_rain_content_hrw2.container(width=100)
        legend_rain_content_hrw2icon.image('static/rainwarning_03_orangehrwl.png')

        legend_rain_content_hrw2text = legend_rain_content_hrw2.container()
        legend_rain_content_hrw2text.write('***Orange Warning Level***')
        legend_rain_content_hrw2text.write(
            '''
            Long-duration intense rainfall (rainfall intensity of 15-30 mm/h, or 3-hour rainfall accumulation of 45-65 mm) ongoing or likely to occur within 2-3 hours
            - Flooding is threatening, or serious flooding is about to occur, in areas that are urbanized, low-lying, and/or near rivers or streams
            - Landslides are likely in hilly or mountainous areas
            ''')

        legend_rain_content_hrw3 = legend_rain_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_rain_content_hrw3icon = legend_rain_content_hrw3.container(width=100)
        legend_rain_content_hrw3icon.image('static/rainwarning_04_redhrwl.png')

        legend_rain_content_hrw3text = legend_rain_content_hrw3.container()
        legend_rain_content_hrw3text.write('***Red Warning Level***')
        legend_rain_content_hrw3text.write(
            '''
            Long-duration torrential rainfall (rainfall intensity more than 30 mm/h, or 3-hour rainfall accumulation more than 65 mm) ongoing or likely to occur within 2-3 hours
            - Serious flooding is expected or ongoing in areas that are urbanized, low-lying, and/or near rivers or streams
            - Landslides are highly likely in hilly or mountainous areas
            ''')

    with col2:
        legend_tcws = st.container(width = 600)
        legend_tcws.write('##### Tropical cyclone winds')
        legend_tcws_content = legend_tcws.container(border=True)
        legend_tcws_content.write('##### Tropical Cyclone Wind Signals (TCWS)')

        legend_tcws_content_tcws1 = legend_tcws_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_tcws_content_tcws1icon = legend_tcws_content_tcws1.container(width=100)
        legend_tcws_content_tcws1icon.image('static/tcws1.png')

        legend_tcws_content_tcws1text = legend_tcws_content_tcws1.container()
        legend_tcws_content_tcws1text.write('***Wind Signal No. 1***')
        legend_tcws_content_tcws1text.write('Strong breeze to near gale-force winds prevailing or expected to occur within 36 hours due to a tropical cyclone, posing minimal to minor threat to life and property')

        legend_tcws_content_tcws2 = legend_tcws_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_tcws_content_tcws2icon = legend_tcws_content_tcws2.container(width=100)
        legend_tcws_content_tcws2icon.image('static/tcws2.png')

        legend_tcws_content_tcws2text = legend_tcws_content_tcws2.container()
        legend_tcws_content_tcws2text.write('***Wind Signal No. 2***')
        legend_tcws_content_tcws2text.write('Gale-force to severe gale-force winds prevailing or expected to occur within 24 hours due to a tropical cyclone, posing minor to moderate threat to life and property')

        legend_tcws_content_tcws3 = legend_tcws_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_tcws_content_tcws3icon = legend_tcws_content_tcws3.container(width=100)
        legend_tcws_content_tcws3icon.image('static/tcws3.png')

        legend_tcws_content_tcws3text = legend_tcws_content_tcws3.container()
        legend_tcws_content_tcws3text.write('***Wind Signal No. 3***')
        legend_tcws_content_tcws3text.write('Storm-force to violent storm-force winds prevailing or expected to occur within 18 hours due to a tropical cyclone, posing moderate to significant threat to life and property')

        legend_tcws_content_tcws4 = legend_tcws_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_tcws_content_tcws4icon = legend_tcws_content_tcws4.container(width=100)
        legend_tcws_content_tcws4icon.image('static/tcws4.png')

        legend_tcws_content_tcws4text = legend_tcws_content_tcws4.container()
        legend_tcws_content_tcws4text.write('***Wind Signal No. 4***')
        legend_tcws_content_tcws4text.write('Typhoon-force winds prevailing or expected to occur within 12 hours due to a tropical cyclone, posing significant to severe threat to life and property')

        legend_tcws_content_tcws5 = legend_tcws_content.container(horizontal=True, horizontal_alignment='left',
                                                                    vertical_alignment = 'center')

        legend_tcws_content_tcws5icon = legend_tcws_content_tcws5.container(width=100)
        legend_tcws_content_tcws5icon.image('static/tcws5.png')

        legend_tcws_content_tcws5text = legend_tcws_content_tcws5.container()
        legend_tcws_content_tcws5text.write('***Wind Signal No. 5***')
        legend_tcws_content_tcws5text.write('Extreme typhoon-force winds prevailing or expected to occur within 12 hours due to a tropical cyclone, posing extreme/catastrophic threat to life and property')

with climate_tab:
    # Setting row 1
    clrow1 = st.container(horizontal=True, horizontal_alignment='center')
    
    # MJO
    mjo = clrow1.container(width=300)
    mjo.write('##### MJO (Madden–Julian)')
    mjo_content = mjo.container(height=200, border=True)
    
    with mjo.expander('Details'):
        st.write(
            '''
            An active Madden–Julian oscillation (MJO) is currently in Phase 5, with the enhanced convection branch located over the Maritime Continent. Rainfall may become generally greater than climatological normals.'''
            )
    
    # ENSO
    enso = clrow1.container(width=300)
    enso.write('##### ENSO (El Niño / La Niña)')
    enso_content = enso.container(height=200, border=True)
    
    with enso.expander('Details'):
        st.write(
            '''
            ENSO-neutral conditions are likely to persist until Aug-Sep-Oct 2025, but climate model forecasts suggest an increasing probability (at least 55%) of short-lived La Niña conditions as early as Sept-Oct-Nov 2025 and persisting until Oct-Nov-Dec 2025. La Niña (and La Niña-like) conditions lead to greater rainfall and greater number of tropical cyclones compared to climatological normals.
            '''
            )
    
    # Drought
    drought = clrow1.container(width=300)
    drought.write('##### Drought assessment')
    drought_content = drought.container(height=200, border=True)
    
    with drought.expander('Details'):
        st.write(
            '''
            No dry conditions, dry spells nor drought conditions expected or ongoing.
            '''
            )
    
    st.write('### Maps of the advisory/warning areas')
    

    st.write('##### Legend')


    

# End of program