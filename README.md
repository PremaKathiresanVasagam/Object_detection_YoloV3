# Object detection using YoloV3
## Classes:
- Person 
- Car
________
YoloV3 Simplified for training on Colab with custom dataset. 

You'll need to download the weights from the original source. 
1. Create a folder called weights in the root (YoloV3) folder
2. Download from: https://drive.google.com/open?id=1LezFG5g3BCW6iYaV89B2i64cqEUZD7e0
3. Place 'yolov3-spp-ultralytics.pt' file in the weights folder:
  * to save time, move the file from the above link to your GDrive
  * then drag and drop from your GDrive opened in Colab to weights folder
4. run this command
`python train.py --data data/customdata/custom.data --batch 10 --cache --epochs 25 --nosave`

For custom dataset:
1. Clone the repo : Change Annotations using process.py
2. Follow the installation steps as mentioned in the repo. 
3. For the assignment, let's use the images shared.
4. Annotate the images using the Annotation tool. 
```
data
  --customdata
    --images/
      --image_000000001.jpg
      --image_000000002.jpg
      --...
    --labels/
      --image_000000001.txt
      --image_000000002.txt
      --...
    custom.data #data file
    custom.names #your class names
    train.txt & test.txt #list of name of the images you want your network to be trained on and be tested.
```
5. As you can see above you need to create **custom.data** file. For 2 class example,our file will look like this:
```
  classes=2
  train=data/customdata/training.txt
  test=data/customdata/testing.txt 
  names=data/customdata/custom.names
```
6. As it a poor idea to keep test and train data same, we have split the data into train and test. custom.txt file should look like, 
```
./data/customdata/images/image_000000001.jpg
./data/customdata/images/image_000000002.jpg
./data/customdata/images/image_000000003.jpg
...
```
7. We need to add custom.names file as we can see above. For our example, we have images of person and car. Our custom.names file look like this:
```
Person
car
```
8. Person and car above will have a class index of 0 and 1
9. For COCO's 80 classes, VOLOv3's output vector has 255 dimensions ( (4+1+80)*3). Now we have 2 class, so we would need to change it's architecture.
10. Copy the contents of 'yolov3-spp.cfg' file to a new file called 'yolov3-custom.cfg' file in the data/cfg folder. 
11. Search for 'filters=255' (you should get entries entries). Change 255 to 21 = (4+1+2)*3
12. Search for 'classes=80' and change all three entries to 'classes=2'
13. We are working with very few samples. In such a case it is a good idea to change:
  * burn_in to 100
  * max_batches to 4000
  * steps to 3200,3600
14. Run this command `python train.py --data data/customdata/custom.data --batch 10 --cache --cfg cfg/yolov3-custom.cfg --epochs 3 --nosave`

**Results**
After training for 44 Epochs...
<br>
<br> 
![image](https://github.com/PremaKathiresanVasagam/Object_detection_YoloV3/blob/master/output/Output_test_img_1.jpg)


Reference and Credits:

Full credit goes to [this](https://github.com/ultralytics/yolov3)
For much more detailed explaination and features, please refer to the original [source](https://github.com/ultralytics/yolov3). 
