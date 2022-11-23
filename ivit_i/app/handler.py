
import logging, os
from .common import get_application

APP_KEY = "application"
FRAMEWORK = "tensorrt"

def get_app_list():
    dir_path = os.path.dirname(__file__)    
    logging.warning(dir_path)
    ret = []
    for path in os.listdir(dir_path):
        
        full_path = os.path.join(dir_path, path)

        if os.path.isdir(full_path) and path!="__pycache__":

            for app in os.listdir(full_path):

                app_path = os.path.join(full_path, app)
                check_file = os.path.isfile(app_path)
                check_ext = os.path.splitext(app)[1]!=".pyc"
                check_name = app != "__init__.py"

                if check_file and check_ext and check_name:
                    ret.append(os.path.splitext(app)[0])
    ret.append("default")
    return ret

def get_tag_app_list():
    dir_path = os.path.dirname(__file__)    
    logging.warning(dir_path)
    ret = {}

    from ivit_i.app import APP_LIST
    for key, val in APP_LIST.items():
        APP_LIST[key].append("default")
        
    ret = APP_LIST

    return ret

# def get_application(config):
    
#     if not APP_KEY in config:
#         raise Exception("Could not find the {}".format(APP_KEY))
    
#     app_config = config[APP_KEY]
#     app_name = app_config['name']
#     depend_label = None

#     # logging.debug(config)

#     if not 'depend_on' in app_config:
#         # capture all label list
#         logging.info('Get all labels for {}'.format(APP_KEY))
#         try:
#             depend_label = get_labels(config)
#         except Exception as e:
#             logging.error(e)
        
#     else:
#         depend_label = app_config['depend_on'] if type(app_config['depend_on'])==list else [ app_config['depend_on'] ]

#     try:
#         if 'tracking' in app_name:
#             logging.warning("Got {} application".format("tracking"))
#             from .darknet.tracking import Tracking as trg

#         elif 'direction' in app_name:
#             logging.warning("Got {} application".format("moving direction"))
#             from .darknet.moving_direction import MovingDirection as trg
        
#         elif 'counting' == app_name:
#             logging.warning("Got {} application".format("pure counting"))
#             from .darknet.counting import Counting as trg
        
#         elif 'area' in app_name:
#             logging.warning("Got {} application".format("area detection"))
#             from .darknet.area_detection import AeraDetection as trg
        
#         elif 'heatmap' in app_name:
#             logging.warning("Got {} application".format("heatmap"))
#             from .darknet.heatmap import Heatmap as trg
        
#         else:
#             return None
#     except Exception as e:
#         logging.error(e)
#         raise e

#     app = trg(depend_label)

#     # other setting in certain application
#     if "area" in app_name:
#         if "area_points" in app_config:
#             app.set_area(app_config["area_points"])
#         else:
#             logging.error("Could not find 'area_points'")
    
#     return app
            
def get_labels(config) -> list:
    """ get the label file and capture all category in it """
    content = []
    
    label_path = config["label_path"] if "label_path" in config else config[FRAMEWORK]["label_path"]

    with open(label_path, 'r') as f:
        for line in f.readlines():
            content.append(line.strip('\n'))
    return content