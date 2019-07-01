# Exercise 6
from pathlib import Path
import satpy
from pyresample.geometry import AreaDefinition
from utils import createResArea

input_dir  = Path("data")
input_dir.mkdir(parents=True,exist_ok=True)
plot_dir = Path("plots")
plot_dir.mkdir(parents=True,exist_ok=True)
# 1. Read the Scene that you downloaded from the data directory using SatPy. [2P]
files = satpy.find_files_and_readers(base_dir=input_dir)
scn = satpy.Scene(files)

# 2. Load the composites "natural_color" and "convection" [2P]
scn.load(["natural_color","convection"])

# 3. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5 

# resample to defined area (using function from utils)
def_area = createResArea(area_ID="Kongo",
                         description="The Kongo and neighbouring countries in Lambert Equal Area projection",
                         proj_id="LambertEqualArea",
                         proj_short="laea",
                         lon_0=23,lat_0=-3,
                         width=500,height=500,
                         llC=-15E5,urC=15E5)
scn_local = scn.resample(def_area)

# 4. Save both loaded composites of the resampled Scene as simple png images. [2P]
scn_local.show("natural_color").save(plot_dir / Path("natural_color.png"))
scn_local.show("convection").save(plot_dir / Path("convection.png"))
