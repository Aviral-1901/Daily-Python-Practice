import numpy as np

x = 1.0
target = 1.0                    #yo code bata hamle 'x' input huda output 1 kasari auxa herxam
weight = np.random.rand()
bias = 0
learning_rate = 0.1

for i in range(10000):
    z = weight * x + bias #z is raw sum vaneko decision lina vanda paile inputs le k vanna khojiraxa
    prediction = 1 / (1 + np.exp(-z))  #yesle value lai 0 ra 1 ko bich ma lyauxa
    error_calculation = target - prediction #we know how far we are from target
    slope_sigmoid = prediction * (1 - prediction) #shows how sensitive the sigmoid is at this point

    common_gradient = error_calculation * slope_sigmoid # It tells us HOW MUCH the output needs to change.

    weight += common_gradient * x * learning_rate
    bias += common_gradient * learning_rate

    if (i % 1000 == 0):
        print(f'value of i : {i} ,prediction : {prediction} ,weight : {weight}, bias : {bias} ')

print("the final prediction is :",prediction)