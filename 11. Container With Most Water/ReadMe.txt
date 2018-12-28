This solution is from CSDN: https://blog.csdn.net/aliceyangxi1987/article/details/50473826
The idea is making area of container lager while making the width of container smaller.
To make the area larger, the min height has to increase. Thus, the height of next point must be larger.

In the original code, only one point move in each loop. However, no matter the height increase or decrease after move, the area will calculate and compare. Thus, I tried to add 'while' loop to make sure the height increase. Although it have worse performance in testcase, I guess the 'while' loop will decrease calculating time while the dataset is huge. 
