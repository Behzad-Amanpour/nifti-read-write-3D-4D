"""
Inputs:
    You can use "fmri.nii" which I provided in the following google drive address:
    https://drive.google.com/file/d/1sLp4W8hiAvuv4XDZcnJbmfYREHFy-wfG/view?usp=sharing
"""

# Reading a NIfTI file ======================== Behzad Amanpour ==================
import nibabel as nib

Im_file=nib.load('fmri.nii')  # This file contains a "header" and an "image" 
Im= Im_file.get_fdata()       # Exctracting the image from the file (it's a 4D image)
print(Im.shape)               # it's (64, 64, 43, 100)

# Selecting some volumes ====================== Behzad Amanpour ==================
Im2=Im[:,:,:,49:99]           # We want to remove the first 50 volumes
Im_file2 = nib.Nifti1Image(Im2, Im_file.affine, Im_file.header)    # Creating a new NIfTI file 
nib.save(Im_file2, 'fmri_part2.nii')                               # Saving the new NIfTI on a drive

# Selecting one volume ======================== Behzad Amanpour ==================
Im2=Im[:,:,:,0]
Im_file2 = nib.Nifti1Image(Im2, Im_file.affine, Im_file.header)
nib.save(Im_file2, 'fmri_3D.nii')

# 4D to 3D Conversion ========================= Behzad Amanpour ==================
import numpy as np

s=np.shape(Im)
for i in range(s[3]):    # The 4D file contains 100 volumes, and after this loop we will have 100 separate 3D files
    print(i)
    Im2=Im[:,:,:,i]
    Im_file2 = nib.Nifti1Image(Im2, Im_file.affine, Im_file.header)
    name='fmri_3D_' + str(i+1) + '.nii'
    nib.save(Im_file2, name)

# Saving on disk as a numpy file ============== Behzad Amanpour ==================
Im2=np.int16(Im)    # you don't need necessarily converting to "integer". It reduces the files size on your disk compared to "float" format
np.save('path on disk\\fmri', Im2)

# loading numpy from disk ===================== Behzad Amanpour ==================
Im2=np.load('path on disk\\fmri.npy')
Im3=Im2[:,:,25,0]

import matplotlib.pyplot as plt
plt.imshow(Im3,cmap='gray')
np.save('path on disk\\fmri_2D',Im3)
