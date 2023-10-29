import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
from df_techniques import table
from descriptor_generator import descriptor


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i*10)
  time.sleep(0.1)

'...and now we\'re done!'