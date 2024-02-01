import subprocess
 
# Using system() method to
# execute shell commands
#  yolo task=<segment/detect> mode=predict save=True model=<trained_model> conf=0.25 source=<target_image_source>
def predict_xray():
    subprocess.Popen('yolo task=segment mode=predict save=True model=yolov8_localization_fractureAtlas.pt conf=0.25 source="/home/netchunk/practise/Datathaon/images"', shell=True)

def rem_dir(image_name):
    s = "/home/netchunk/practise/Datathaon/FracAtlas/runs/detect"
    subprocess.Popen('rmdir ', shell=True)
