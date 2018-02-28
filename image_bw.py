import cv2
import numpy as np
import heapq
import copy

img = cv2.imread('mario.png' , 0)
cv2.imshow('random-image',img)
print(img.shape)

population = []

iterations = 500

for k in range(10):
    t1 = []
    for i in range(len(img)):
        t2 = []
        for j in range(len(img[0])):
            t3 = np.random.randint(0,256)
            t2.append(t3)
        t1.append(t2)
    population.append(t1)

def calcCost(mainimg , pop):
    t1 = []
    for k in range(10):
        cost = 0
        for i in range(len(pop[0])):
            for j in range(len(pop[0])):
                cost = cost + (mainimg[i][j] - pop[k][i][j])**2
        t1.append(cost/400)
    return t1

def crossover(pop1 , pop2):
    temp1 = pop1[0:50,:]
    temp2 = pop2[50:100,:]
    temp3 = pop1[100:150,:]
    temp4 = pop2[150:200,:]

    t1 = np.concatenate((temp1,temp2),axis=0)
    t2 = np.concatenate((t1,temp3),axis=0)
    pop3 = np.concatenate((t2,temp4),axis=0)

    row = np.random.randint(200)
    for i in range(200):
        pop3[row][i] = np.random.randint(0,256)

    return pop3

population = np.array(population)
print(population.shape)


for i in range(iterations):

    cost = calcCost(img , population)
    print('Cost : ' , cost)

    temp_cost_list = copy.copy(cost)

    temp_cost_list.sort()

    pop3 = crossover(population[cost.index(temp_cost_list[0])] , population[cost.index(temp_cost_list[1])])

    population = np.delete(population , cost.index(temp_cost_list[9]) , 0)

    population = np.concatenate((population,pop3.reshape((1,200,200))) , axis=0)

    cv2.imwrite('random.png',population[0])
    rnd_img = cv2.imread('random.png')

    cv2.imshow('random-image',rnd_img)

print(population.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()

