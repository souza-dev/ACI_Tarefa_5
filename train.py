import dlib

# Gerar arquivo xml de anotações
# https://imglab.in/

options = dlib.simple_object_detector_training_options()
options.add_left_right_image_flips = True
options.C = 100

dlib.train_simple_object_detector('treinamento/placas/pare/pare.xml', "paredetector.svm", options)
dlib.train_simple_object_detector('treinamento/placas/proibido/proibido.xml', "proibidodetector.svm", options)
dlib.train_simple_object_detector('treinamento/placas/contramao/contra.xml', "contradetector.svm", options)