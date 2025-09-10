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

st.write('## Tropical Cyclone (TC) Updates')

# Setting tabs for weather-related and climate-related advisories and warnings
activetc_tab, fscttc_tab = st.tabs(['Active TCs', 'TC formation & threat potential'])

with activetc_tab:
    st.write('### Active tropical cyclones')
    
with fscttc_tab:
    st.write('### 24-hour tropical cyclone formation outlook')
    st.write('****as of 8:00 AM 10 September 2025****')

    st.image('static/24h_tc_formation_outlook.jpg')




    st.write('### Tropical cyclone threat potential forecast')