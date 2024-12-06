import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def load_and_display_dicom_image(dicom_file_path, cmap='gray', vmin=50, vmax=200, scaling_factor=0.074):
    ds = pydicom.dcmread(dicom_file_path)
    pixel_array = ds.pixel_array
    if len(pixel_array.shape) == 3:
        pixel_array = rgb2gray(pixel_array)
    #Målepunkter
    #start_x1, start_y1, end_x1, end_y1 = 300, 300, 560, 300
    #start_x2, start_y2, end_x2, end_y2 = 430, 142, 430, 300

    #distance_mm_1 = np.sqrt((end_x1 - start_x1)**2 + (end_y1 - start_y1)**2) * scaling_factor
    #distance_mm_2 = np.sqrt((end_x2 - start_x2)**2 + (end_y2 - start_y2)**2) * scaling_factor

    plt.figure(figsize=(8, 8))
    plt.imshow(pixel_array, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.axis("off")
    #plt.plot([start_x1, end_x1], [start_y1, end_y1], color='red', linewidth=2, linestyle='--')
    #plt.text((start_x1 + end_x1) / 2, (start_y1 + end_y1) / 2, f'{distance_mm_1:.2f} mm', color='white', fontsize=12)
    #plt.plot([start_x2, end_x2], [start_y2, end_y2], color='blue', linewidth=2, linestyle='--')
    #plt.text((start_x2 + end_x2) / 2, (start_y2 + end_y2) / 2, f'{distance_mm_2:.2f} mm', color='white', fontsize=12)
    plt.show()

def process_dicom_folder(dicom_folder, cmap='gray', vmin=None, vmax=None, scaling_factor=0.074):
    dicom_files = os.listdir(dicom_folder)
    for dicom_file in dicom_files:
        dicom_path = os.path.join(dicom_folder, dicom_file)
        if os.path.isfile(dicom_path):
            load_and_display_dicom_image(dicom_path, cmap=cmap, vmin=vmin, vmax=vmax, scaling_factor=scaling_factor)

dicom_folder = "/Users/MarieMelhof/Desktop/Imaging/students_phantoms-2/B7__121402_selected"
process_dicom_folder(dicom_folder, cmap='gray', vmin=None, vmax=None, scaling_factor=0.074)
