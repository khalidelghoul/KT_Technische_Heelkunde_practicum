#Install packages
pip install menpo
pip install menpo3d
pip install matplotlib
pip install numpy

#import packages
import menpo
import menpo3d
import matplotlib.pyplot as plt
import numpy as np

#set viewer
%matplotlib qt

#define path to meshes
path_to_meshes= ""

#import meshes 
meshes = menpo3d.io.import_meshes(path_to_meshes+'*.obj') #.ply bestanden kunnen ook worden gelezen

#generate PCA model
PCA_model = menpo.model.PCAModel(meshes) 

#generate mean mesh 
mean_mesh = PCA_model.mean()

#view mean mesh 
mean_mesh.view()

#export mean mesh
menpo3d.io.export_mesh(mean_mesh, os.path.join(path_to_meshes, 'mesh_mean.obj')) #kan ook als .ply worden gexporteerd
