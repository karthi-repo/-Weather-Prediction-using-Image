import os
import random
import shutil

dataOrgFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Original_dataset/"
dataBaseFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/"

dataDirList = os.listdir(dataOrgFolder)
print(dataDirList)

splitSize = .85

# build files array

def split_data (SOURCE , TRAINING , VALIDATION , SPLIT_SIZE):
    files = []

    for filename in os.listdir(SOURCE) :
        file = SOURCE + filename
        print(file)
        if os.path.getsize(file) > 0 :
            files.append(filename)
        else:
            print(filename + " has 0 length , will not copy this file !!")

    # print number of files :
    print(len(files))


    trainLength = int(len(files) * SPLIT_SIZE )
    validLength = int( len(files) - trainLength )

    suffleDataSet = random.sample(files, len(files))

    trainingSet = suffleDataSet[0:trainLength]
    validSet = suffleDataSet[trainLength:]

    # copy the train images 
    for filename in trainingSet:
        f = SOURCE + filename
        dest = TRAINING + filename
        shutil.copy(f, dest) 
    
    # copy the valid images 
    for filename in validSet:
        f = SOURCE + filename
        dest = VALIDATION + filename
        shutil.copy(f, dest) 



cloudySourceFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Original_dataset/cloudy/"
cloudyTrainFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/Train/cloudy/"
cloudyValidFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/validate/cloudy/"

foggySourceFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Original_dataset/foggy/"
foggyTrainFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/Train/foggy/"
foggyValidFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/validate/foggy/"

rainyySourceFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Original_dataset/rainy/"
rainyTrainFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/Train/rainy/"
rainyValidFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/validate/rainy/"

shineSourceFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Original_dataset/shine/"
shineTrainFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/Train/shine/"
shineValidFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/validate/shine/"

sunriseSourceFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/Original_dataset/sunrise/"
sunriseTrainFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/Train/sunrise/"
sunriseValidFolder = "C:/Users/Karthi/Desktop/All_FILE/master_mini_proj/dataset/validate/sunrise/"






split_data(cloudySourceFolder , cloudyTrainFolder , cloudyValidFolder , splitSize)
split_data(foggySourceFolder , foggyTrainFolder , foggyValidFolder , splitSize)
split_data(rainyySourceFolder , rainyTrainFolder , rainyValidFolder , splitSize)
split_data(shineSourceFolder , shineTrainFolder , shineValidFolder , splitSize)
split_data(sunriseSourceFolder , sunriseTrainFolder , sunriseValidFolder , splitSize)




