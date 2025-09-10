import pandas as pd
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

st.write('## 🌀 Tropical Cyclone (TC) Updates')
st.write('Note: ***Actively-monitored TCs*** are those that are being intensively monitored by DOST-PAGASA such that they warrant the issuance of either a Tropical Cyclone Advisory (TCA) or a Tropical Cyclone Bulletin (TCB). Any TCs that are present within the PAGASA Monitoring Domain but are not actively monitored are still shown in the 24-Hour Tropical Cyclone Formation Outlook.')

# Setting tabs for weather-related and climate-related advisories and warnings
activetc_tab, fscttc_tab = st.tabs(['Active TCs', 'TC formation & threat potential'])

with activetc_tab:
    st.write('##### Actively-monitored tropical cyclones')

    st.write('### Tropical Storm “PAENG” (*Nalgae*)')
    st.write("*based on DOST-PAGASA's Tropical Cyclone Bulletin No. 11, issued at 5:00 PM, 28 October 2022*")

    tc_headline = st.container(border=True, horizontal=True,
                               horizontal_alignment='center', vertical_alignment = 'center')

    tc_icon = tc_headline.container(width=70)
    tc_icon.image('static/TCcat_02_TS.png')

    tc_headline_text = tc_headline.container()
    tc_headline_text.write(
        '''
        ⚠️ ****Tropical Storm “PAENG” (*Nalgae*) slightly intensifies as it moves west-northwestward towards Northern Samar–Sorsogon–Albay area.****
        - Guiuan, Eastern Samar is currently under ****Tropical Cyclone Wind Signal No. 2**** due to “PAENG”. Gale-force to severe gale-force winds are prevailing or expected, posing minor to moderate threat to life and property.
        - Due to “PAENG”, Guiuan is also currently under ****Orange Heavy Rainfall Warning Level**** for the threat of long-duration intense rains that can trigger threatening floods and landslides and ****Gale Warning**** for rough to very rough seas that are hazardous to various vessels.
        '''
        )

    satimg, tctrack = st.columns(2)

    with satimg:
        st.image('static/sample_tc_sat.gif')
    
    with tctrack:
        st.image('static/tctrack.png')

    "---"

    tcparams, fcstlocs = st.columns(2)

    with tcparams:
        st.write('#### Current tropical cyclone parameters')
        st.write('*as of 4:00 PM, 28 October 2022:*')

        st.write('##### Location of center')
        center_loc = st.container(border=True)
        center_loc.write('**180 kilometers East of Catarman, Northern Samar** (near 12.4°N 126.3°E)')

        st.write('##### Intensity')
        center_loc = st.container(border=True)
        center_loc.write(
            '''
            - 10-min maximum sustained winds near the center: **85 km/h**
            - Gustiness: **105 km/h**
            - Central pressure: **990 hPa**
            '''
            )
        
        st.write('##### Movement')
        center_loc = st.container(border=True)
        center_loc.write('**West-northwestward** at **25 km/h**')

        st.write('##### Extent of tropical cyclone wind field')
        center_loc = st.container(border=True)
        center_loc.write('Strong to gale-force winds extend outwards up to **480 km from the center**')

    with fcstlocs:
        st.write('#### Track and intensity forecast')
        forecast_locations = st.container(border=True)
        forecast_locations.image('static/tc_fcst_locations.png')
    
    "---"

    st.write('#### Tropical cyclone hazards threatening Guiuan, Eastern Samar')
    st.write('Note: To see all active warnings over Guiuan, go to ****⚠️ Advisories & Warnings****.')

    hazardsrow1 = st.container(horizontal=True, horizontal_alignment='center')

    hazard_rainfall = st.container(width=600)
    hazard_rainfall.write('##### Rainfall')

    hazard_rainfall_content = hazard_rainfall.container(horizontal_alignment='center', border=True)

    hazard_rainfall_icons = hazard_rainfall_content.container(horizontal=True)
    hrw_icon = hazard_rainfall_icons.container(width=150)
    hrw_icon.image('static/rainwarning_04_redhrwl.png')
    wahr_icon = hazard_rainfall_icons.container(width=150)
    wahr_icon.image('static/hvyrainoutlook3.png')

    hazard_rainfall_content.write(
        '''
        - Heavy to intense with at times torrential rains are likely this afternoon through tomorrow early morning, then gradually decreasing onwards. Tomorrow early morning through Sunday morning, light to moderate with at times heavy rains are still likely.
        '''
    )
    
with fscttc_tab:
    st.write('### 24-hour tropical cyclone formation outlook')
    st.write('****as of 8:00 AM 10 September 2025****')

    st.image('static/24h_tc_formation_outlook.jpg')

    st.write('### Tropical cyclone threat potential forecast')
    st.write('****as of 10 September 2025****')

    st.image('static/tcthreatpotentialfcst.png')