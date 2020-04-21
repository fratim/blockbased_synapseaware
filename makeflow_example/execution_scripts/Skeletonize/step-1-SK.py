import os
import sys

from blockbased_synapseaware.utilities.dataIO import ReadMetaData
from blockbased_synapseaware.makeflow_example.makeflow_helperfunctions import *

from blockbased_synapseaware.skeletonize.anchors import SaveAnchorWalls



# read passed arguments
meta_fp,iz,iy,ix = ReadArguments(sys.argv)

# read in the data for this block
data = ReadMetaData(meta_fp)

# check that beforehand step has executed successfully
CheckSuccessFile("HF", 4, iz, iy, ix)

# users must provide an output directory
assert (not data.SkeletonOutputDirectory() == None)
os.makedirs(data.SkeletonOutputDirectory(), exist_ok=True)

SaveAnchorWalls(data, iz, iy, ix)

# Create and Write Success File
WriteSuccessFile("SK", 1, iz, iy, ix)
