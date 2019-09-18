from pathlib import Path
from plyfile import PlyData
data = PlyData.read("pclouds/data/dense/fused.ply")
data.elements
data.x
data.vertex
data[vertex]
data['vertex']
data['vertex']['x']
data['vertex']['x'].shape
data['vertex']['y'].shape
xyz = np.vstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z']))
import numpy as np
xyz = np.vstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z']))
xyz.shaper
xyz.shape
xyz = np.vstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z'])).T
xyz.shape
xyz = np.hstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z'])).shape
xyz = np.hstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z'])).shape
xyz = np.hstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z']))
xyz.shape
xyz = np.dstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z']))
xyz.shape
xyz = np.vstack((data['vertex']['x'], data['vertex']['y'], data['vertex']['z'])).T
xyz.shape
normal = np.vstack((data['vertex']['nx'], ata['vertex']['ny'], ata['vertex']['nz'])).T
normal = np.vstack((data['vertex']['nx'], data['vertex']['ny'], data['vertex']['nz'])).T
normal.shape
np.savetxt?
q
np.savetxt("pclouds/data/dense/fused.xyz", xyz)
np.savetxt("pclouds/data/dense/fused.normals", normals)
np.savetxt("pclouds/data/dense/fused.normals", normal)
%hist -f ply2txt.pt
