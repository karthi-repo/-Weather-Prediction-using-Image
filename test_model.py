from keras.models import load_model
import numpy as np
#from keras.preprocessing.image import 
from keras.utils import load_img , img_to_array
import pandas as pd


imgWidth= 256
imgHeight=256

classes = ["cloudy","foggy", "rainy", "shine", "sunrise"]

model = load_model("C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/bestWeatherModel.h5")

print(model.summary())

def prepareImage(ImagePath):
    image = load_img(ImagePath, target_size=(imgHeight,imgWidth))
    imgResult = img_to_array(image)
    imgResult = np.expand_dims(imgResult, axis = 0)
    imgResult - imgResult / 255.
    return imgResult

testImagesFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Test"
testImagesNamesDF = pd.read_csv("C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/test.csv")
testImagesList = []



testDFList = testImagesNamesDF['Image_id'].tolist()



for item in testDFList:
    tempName = testImagesFolder + "/" + str(item)
    testImagesList.append(tempName)


print("The list of the images : ")
print(testImagesList)


ImagesArray = prepareImage(testImagesList[0])


for imgName in testImagesList[1: ]:
    print("preparing image : " + imgName)
    processedImage = prepareImage(imgName)
    ImagesArray = np.append(ImagesArray,processedImage,axis=0)

print("Images shape: ")
print(ImagesArray.shape)


np.save("C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/ImagesArray.npy", ImagesArray)


resultArray = model.predict(ImagesArray, batch_size=16, verbose=1)
answers = np.argmax(resultArray, axis = 1)
print("Answers : ")
print(answers)

yTrue = testImagesNamesDF['labels']
yPred = answers

num = 0
for imgName in testImagesList: 
    print ("Image :" + imgName + "      True Value :" + classes[yTrue[num]] + "      Predictions: " + classes[yPred[num]] ) 
    num = num + 1

