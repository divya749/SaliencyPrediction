# SaliencyPrediction

INTRODUCTION

This work focuses on the prediction of visual attention, or, saliency, in a 360 degree signal. We
study the various methods used to represent a 360-degree i mage i nto i ts equivalent
two-dimensional format. The 360-degree i mage i s provided as an i nput i n the form of an
equirectangular i mage. Application of conventional saliency models to simple equirectangular
images results i n i naccurate saliency prediction. Therefore, we represent the i nput
equirectangular i mage to cube-map based form before predicting saliency. After saliency
prediction, we convert the cube-map i mage back to equirectangular format. In this way, the
problems arising due to distortions i n an equirectangular i mage are minimized. We perform our
experiments with two regular “flat” saliency predictors, namely, GBVS model and
Itti-Koch-Niebur model and evaluate saliency prediction performance with the use of metrics,
comparing the results obtained with the ground truth.

STEPS INVOLVED:
1. Conversion of equirectangular projection of 360-degree images to equivalent cubemap projection (2 formats of cubemap used-- horizon and dice)
2. Applying Saliency prediction using flat saliency predictors, GBVS and Itti-Koch-Neibur
3. Conversion of saliency map generated on cubemap image back to its equivalent equirectangular projection.
4. Comparing the final saliency maps obtained with the ground truth maps taken from the Salient360! dataset.
