from django.shortcuts import render
from .main  import *
from .graph import *
from logging import *
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import os

def index(request):
    return render(request, 'index.html')

def upload(request):

    if request.method == 'POST' and request.FILES['imageUpload']:
        print("Hello! Upload")

        #intialize the save path for uploaded and segmented files
        init_save_path = os.getcwd()+"/graph_image_segmentation_app"
        
        # Save the uploaded file
        image_file = request.FILES['imageUpload']
        print(type(image_file))
        # image_path = init_save_path+"/assets/"+image_file.name
        
        # print("Uploaded Image file: ",image_file)
        # print("Uploaded Image path: ",image_path)
        
        # # Perform segmentation using main.py
        segmented_image_path = os.getcwd()+"/static/uploads/"+"seg_"+image_file.name
        print("Segmented image path: " , segmented_image_path)
        
        #subprocess.call(['python', 'get_segmented_image', image_path, segmented_image_path])
        
        params = {'sigma':1, 'nbd':8, 'min_comp_size':2000, 'k':100} # value of parameters
        
        ''' 
        sigma: Gaussian blur constant
        nbd: neighbourhood size (4 or 8)
        min_comp_size: a constant to remove all the components with fewer number of pixels
        k: threshold constant
        '''
        
        #Calling get_segmented_image function from main.py for segmentation 
        get_segmented_image(params['sigma'], params['nbd'], params['min_comp_size'],params['k'], image_file, segmented_image_path)

        # Return the path to the segmented image
        return JsonResponse({'segmentedImagePath': "/static/uploads/seg_"+image_file.name})

    return JsonResponse({'error': 'Invalid request'})

