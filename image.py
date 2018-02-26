import cv2
import numpy as np

img = cv2.imread('mario.png')
print(img.shape)

population = []

for k in range(10):
    t1 = []
    for i in range(len(img)):
        t2 = []
        for j in range(len(img[0])):
            t3 = [np.random.randint(0,256) , np.random.randint(0,256) , np.random.randint(0,256) ]
            t2.append(t3)

        t1.append(t2)
    population.append(t1)

def calcCost(mainimg , pop):
    t1 = []
    for k in range(10):
        temp = np.subtract(mainimg , pop[k])
        t1.append(temp)
    return t1


population = np.array(population)

print(population[0].shape)

cv2.imwrite('random.png',population[0])
rnd_img = cv2.imread('random.png')

cv2.imshow('random-image',rnd_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

