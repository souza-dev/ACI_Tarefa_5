import os
import dlib
import cv2
import glob

pareDetector = dlib.simple_object_detector("paredetector.svm")
proibidoDetector = dlib.simple_object_detector("proibidodetector.svm")
contraDetector = dlib.simple_object_detector("contradetector.svm")

for imagem in glob.glob(os.path.join("teste/placas", "*.jpeg")):
    print (imagem)
    img = cv2.imread(imagem)
    pareDetecteds = pareDetector(img, 2)
    proibidoDetecteds = proibidoDetector(img, 2)
    contraDetecteds = contraDetector(img, 2)

    for pare in pareDetecteds:
        l, t, r, b = (int(pare.left()), int(pare.top()), int(pare.right()), int(pare.bottom()))
        cv2.rectangle(img, (l,t), (r, b), (0, 255, 0), 2)
        cv2.putText(img, 'Pare', (l, b+30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0)) 
    for proibido in proibidoDetecteds:
        l, t, r, b = (int(proibido.left()), int(proibido.top()), int(proibido.right()), int(proibido.bottom()))
        cv2.rectangle(img, (l,t), (r, b), (0, 255, 0), 2)
        cv2.putText(img, 'Proibido Estacionar', (l, b+30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0)) 
    for contra in contraDetecteds:
        l, t, r, b = (int(contra.left()), int(contra.top()), int(contra.right()), int(contra.bottom()))
        cv2.rectangle(img, (l,t), (r, b), (0, 255, 0), 2)
        cv2.putText(img, 'Contramao', (l, b+30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0)) 
    #cv2.imwrite(imagem + '.jpg', img)
    cv2.imshow("Detector de placas", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
