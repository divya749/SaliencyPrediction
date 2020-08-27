from saliency_models import gbvs, ittikochneibur
import cv2
import time
import numpy as np 
from matplotlib import pyplot as plt
from e2c import e2c, c2e, utils
import py360convert

if __name__ == '__main__':
    
    for i in range(1, 2):
        imname = "./images/{}.jpg".format(i)
        print("processing {}".format(imname))

        img = cv2.imread(imname)
        
        cm_img = e2c(img,'horizon')
        h, w = img.shape[:2]
        
        
        saliency_map_gbvs = gbvs.compute_saliency(cm_img)
        saliency_map_ikn = ittikochneibur.compute_saliency(cm_img)
        saliency_map_gbvs = utils.convert_gray2rgb(saliency_map_gbvs)
        saliency_map_ikn = utils.convert_gray2rgb(saliency_map_ikn)
        saliency_map_gbvs_cm = c2e(saliency_map_gbvs,h,w,'horizon')
        saliency_map_ikn_cm = c2e(saliency_map_ikn,h,w,'horizon' )



        oname = "./outputs/{}.jpg".format(i, time.time())
        cv2.imwrite(oname, saliency_map_ikn_cm)

        fig = plt.figure(figsize=(10, 6))

        fig.add_subplot(1, 6, 1)
        plt.imshow(img, cmap='gray')
        plt.gca().set_title("Equirectangular Input")
        plt.axis('off')

        fig.add_subplot(1, 6, 2)
        plt.imshow(cm_img, cmap='gray')
        plt.gca().set_title("Cubemap")
        plt.axis('off')
        
        fig.add_subplot(1, 6, 3)
        plt.imshow(saliency_map_gbvs, cmap='gray')
        plt.gca().set_title("GBVS-Cubemap")
        plt.axis('off')
    
        fig.add_subplot(1, 6, 4)
        plt.imshow(saliency_map_ikn, cmap='gray')
        plt.gca().set_title("IKN-Cubemap")
        plt.axis('off')

        fig.add_subplot(1, 6, 5)
        plt.imshow((saliency_map_gbvs_cm).astype(np.uint8), cmap='gray')
        plt.gca().set_title("GBVS")
        plt.axis('off')

        fig.add_subplot(1, 6, 6)
        plt.imshow((saliency_map_ikn_cm).astype(np.uint8), cmap='gray')
        plt.gca().set_title("Itti Koch Neibur")
        plt.axis('off')
        
        plt.show()


