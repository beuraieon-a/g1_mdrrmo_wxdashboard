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
    
    tstm_content = tstm.container(height=200, border=True)

    tstm_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/rainwarning_00_tstmadv.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )

    # tstm_content = tstm.container(height=200, border=True, horizontal_alignment="center")
    # tstm_content.image("static/rainwarning_00_tstmadv.png", width=145, caption="as of 10:00 AM 31 August 2025")

    with tstm.expander('Details'):
        st.write(
            '''
            Moderate to heavy rainshowers with possible isolated intense downpours, accompanied with lightning and strong winds, are ongoing or likely to occur within 1-2 hours.
            '''
            )
    
    # Light to moderate rainfall
    rain = wxrow1.container(width=300)
    rain.write('##### Light–moderate rainfall')
    rain_content = rain.container(height=200, border=True)
    
    rain_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/rainwarning_01_rainfalladvisory.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with rain.expander('Details'):
        st.write(
            '''
            Long-duration light to moderate rains with possible isolated heavy downpours are ongoing or likely to occur within 2-3 hours.
            '''
            )
    
    # Heavy rainfall
    heavyrainfall = wxrow1.container(width=300)
    heavyrainfall.write('##### Heavy rainfall')
    heavyrainfall_content = heavyrainfall.container(height=200, border=True)
    
    heavyrainfall_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/rainwarning_03_orangehrwl.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with heavyrainfall.expander('Details'):
        st.write(
            '''
            Long-duration intense rainfall ongoing or likely to occur within 2-3 hours. Severe flooding is threatening to occur in areas that are urbanized, low-lying, and/or near rivers or streams. Landslides are likely to occur in hilly or mountainous areas.
            '''
            )

    # Weather advisory (Heavy rainfall outlook)
    wahr = wxrow1.container(width=300)
    wahr.write('##### Weather advisory')
    wahr_content = wahr.container(height=200, border=True)
    
    wahr_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/hvyrainoutlook2.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with wahr.expander('Details'):
        st.write(
            '''
            24-hour (daily) accumulated rainfall of 100-200 millimeters is possible today (September 1) until tomorrow aftenoon (September 2). Numerous flooding events are likely, especially in areas that are urbanized, low-lying, and/or near rivers or streams. Landslide likely in moderate to highly susceptible areas.
            '''
            )
    
    # Setting row 2
    wxrow2 = st.container(horizontal=True, horizontal_alignment='center')

    # Marine gale
    gale = wxrow2.container(width=300)
    gale.write('##### Marine gale')
    gale_content = gale.container(height=200, border=True)
    
    gale_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/galewarning_beaufort8-9.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )

    with gale.expander('Details'):
        st.write(
            '''
            Strong to gale-force winds are prevailing or expected, causing rough to very rough seas. Sea travel is risky for small seacrafts (including all motor bancas of any type or tonnage). Mariners of these vessels are advised to remain in port or seek safe harbor. For larger vessels, operating in these conditions require experience and properly equipped vessels
            '''
            )

    # Tropical cyclone wind signal
    tcws = wxrow2.container(width=300)
    tcws.write('##### Tropical cyclone winds')
    tcws_content = tcws.container(height=200, border=True)
    
    tcws_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/TCcat_03_STS.png" width="70">
            <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
            <img src="app/static/tcws2.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )

    with tcws.expander('Details'):
        st.write(
            '''
            Gale-force winds are prevailing or expected to occur within 24 hours due to a tropical cyclone, posing minor to moderate threat to life and property.
            '''
            )

    # Storm surge
    stsurge = wxrow2.container(width=300)
    stsurge.write('##### Storm surge')
    stsurge_content = stsurge.container(height=200, border=True)
    
    stsurge_content.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
            <img src="app/static/stormsurgewarning2.png" width="145">
        </div>
        <div style="text-align: center; font-size: small;">
            as of 10:00 AM 31 August 2025
        </div>
        """,
        unsafe_allow_html=True
    )

    with stsurge.expander('Details'):
        st.write(
            '''
            There is a moderate to high risk of storm surge with heights of 2-3 meters within 24 hours due to a tropical cyclone. Severe damage is expected to communities and coastal/marine infrastructures, along with significant coastal erosion. Riverine flooding due to forced/induced upstream flow by the storm surge is also likely.
            '''
            )
    
    st.write('### Maps of the advisory/warning areas')
    

    st.write('##### Legend')

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

# End of program