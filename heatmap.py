import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from pathlib import Path

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
# Reading the .xlsx file and storing it as a pandas Data Frame
# Lines-------------------------------------------

data_file = Path(__file__).with_name("births_brazil_datasus.xlsx")

df_births = pd.read_excel(data_file, 
                          header = 4, 
                          index_col = 0,
                          usecols = "B,I:AG",
                          skipfooter = 2)

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
# Making figures
#-------------------------------------------------------------------------------------
# Figure 1
# Heatmap
# Creates a figure object with size 15x8 inches
fig1, ax = plt.subplots(figsize = (15, 8))

sns.heatmap(df_births, cbar_kws = {'shrink': 0.8}) #, linewidths = 0.5, linecolor = 'white')

# Figure Title
fig1.suptitle('Birth seasonality in Brazil', fontsize = 16, x = 0.067, ha = 'left')

# Colorbar title
colorbar = ax.collections[0].colorbar
#colorbar.set_label('Number of births \n(Thousands)', labelpad = 10)

# Position of colorbar in figure coordinates (these are normalized from 0 to 1)
cbar_pos = colorbar.ax.get_position()

# Add text above the colorbar
fig1.text(x = 0.875, #cbar_pos.x0 + cbar_pos.width / 2, 
          y = cbar_pos.y1 + 0.01, 
          s = 'Number of births \n(Thousands)', 
          ha = 'center', 
          va = 'bottom')

# Formating the colorbar ticks
formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}')
colorbar.formatter = formatter
colorbar.update_ticks()

# Data source
fig1.text(x = 0.62, 
          y = -0.03, 
          s = 'Data source: http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinasc/cnv/nvuf.def', 
          ha = 'center', 
          va = 'bottom', 
          fontsize = 10)

# Axes
#ax.set_xlabel("Year", fontsize = 12)
#ax.set_ylabel("Month", fontsize = 12)
ax.set_ylabel("")
ax.set_title("Birth records by month in DataSUS", fontsize = 12, pad = 20, loc = 'left')

# Rotates the axis labels to horizontal
plt.xticks(rotation = 0)  
plt.yticks(rotation = 0)  

# Scales' ticks
ax.tick_params(axis = 'x', labelsize = 9)
ax.tick_params(which = "both", bottom = False, top = False, left = False, right = False)

# Adjusting the vertical and horizontal spacing, so there are no overlapings
plt.tight_layout()

# Saving
plt.savefig("brazil_births_heatmap.png", bbox_inches = "tight")
#plt.savefig("brazil_births_heatmap.eps", transparent = True, bbox_inches = "tight", transparent = True)
# Transparence will be lost in .eps, save in .svg or .pdf for transparences
#plt.savefig("brazil_births_heatmap.svg", format = "svg", transparent = True, bbox_inches = "tight")
#plt.savefig("brazil_births_heatmap.pdf", format = "pdf", transparent = True, bbox_inches = "tight")

# Showing figures-------------------------------------------------------------------------------------------
plt.show()  # You must call plt.show() to make graphics appear.