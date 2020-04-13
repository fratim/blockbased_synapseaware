import os
import sys

from blockbased_synapseaware.utilities.constants import *
from blockbased_synapseaware.utilities.dataIO import ReadMetaData
from blockbased_synapseaware.makeflow_example.makeflow_helperfunctions import *

from blockbased_synapseaware.hole_filling.connect import ConnectLabelsAcrossBlocks


# read passed arguments
prefix,iz,iy,ix = ReadArguments(sys.argv)

# read in the data for this block
data = ReadMetaData(prefix)

# check that beforehand step has executed successfully
CheckSuccessFile(data.TempDirectory(), "HF", 1, iz, iy, ix)

# users must provide an output directory
assert (not data.HoleFillingOutputDirectory() == None)
os.makedirs(data.HoleFillingOutputDirectory(), exist_ok=True)

# compute the second step to find adjacencies between borders
ConnectLabelsAcrossBlocks(data, iz, iy, ix)

# Create and Write Success File
WriteSuccessFile(data.TempDirectory(), "HF", 2, iz, iy, ix)
