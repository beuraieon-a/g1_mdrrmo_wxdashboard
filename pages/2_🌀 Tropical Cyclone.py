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

    tc_headline = st.container(border=True)
    tc_headline.write(
        '''
        ⚠️ ****Tropical Storm “PAENG” (*Nalgae*) slightly intensifies as it moves west-northwestward towards Northern Samar–Sorsogon–Albay area.****
        - Guiuan, Eastern Samar is currently under ****Tropical Cyclone Wind Signal No. 2**** due to “PAENG”. Gale-force to severe gale-force winds are prevailing or expected, posing minor to moderate threat to life and property.
        - Due to “PAENG”, Guiuan is also currently under ****Orange Heavy Rainfall Warning Level**** for the threat of long-duration intense rains that can trigger threatening floods and landslides and ****Gale Warning**** for rough to very rough seas that are hazardous to various vessels.
        '''
        )

    tcparams, tcgraphics = st.columns(2)

    with tcparams:
        st.write('*Tropical cyclone parameters as of 4:00 PM, 28 October 2022:*')

        st.write('###### Location of center')
        center_loc = st.container(border=True)
        center_loc.write.('180 km east of Catarman, Northern Samar (12.4°N, 126.3°E)')

    with tcgraphics:
        st.image('static/sample_tc_sat.gif')
        st.image('static/tctrack.png')
    
with fscttc_tab:
    st.write('### 24-hour tropical cyclone formation outlook')
    st.write('****as of 8:00 AM 10 September 2025****')

    st.image('static/24h_tc_formation_outlook.jpg')

    st.write('### Tropical cyclone threat potential forecast')
    st.write('****as of 10 September 2025****')

    st.image('static/tcthreatpotentialfcst.png')