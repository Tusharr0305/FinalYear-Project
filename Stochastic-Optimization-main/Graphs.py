import matplotlib.pyplot as plt
from multiprocessing import Process
import json
def pso_smo_hybrid():


    size=15


    # hybrid include
    with open('hybridout.json', 'r') as json_file: 
        data = json.load(json_file)
    print(data)
    # line PSO points
    # x1 = [1,2,3,4,5,6,7,8,9,10]
   
    y1=[]
    for i in range(size):
      y1.append(data[i])
    
    x1=[]
    for i in range(size):
      x1.append(i)





    # plotting the line PSO points
    plt.plot(x1, y1, label = "SMO Optimized Fitness Value")


    # line BFO points
    x2 = [1,2,3,4,5,6,7,8,9,10]
    y2 = [2.75069,2.74135,2.50453,2.75608,2.66378,2.74944,2.73456,2.75097,2.75590,2.74022]
    # plotting the line BFO points
    plt.plot(x2, y2, label = "BFO Optimized Fitness Value")

    # line Hybrid points
    x3 = [1,2,3,4,5,6,7,8,9,10]
    y3 = [2.75293,2.73321,2.74373,2.55376,2.70442,2.75257,2.68753,2.74894,2.76000,2.66990]
    # plotting the line Hybrid points
    plt.plot(x3, y3, label = "Hybrid Optimized Fitness Value")

    # line experimented points
    x4 = [1,2,3,4,5,6,7,8,9,10]
    y4 = [2.76,2.76,2.76,2.76,2.76,2.76,2.76,2.76,2.76,2.76]
    # plotting the line experimented points
    plt.plot(x4, y4, color='yellow', label = "Expected Optimized Fitness Value", markersize=0)

    # naming the x axis
    plt.xlabel('Iterations')
    # naming the y axis
    plt.ylabel('Optimized Fitness Value ')
    # giving a title to my graph
    plt.title('Optimized Fitness Values - SMO BFO and Hybrid')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()

def percentage_error():

    labels = ['PSO', 'BFO', 'Hybrid']
    predicted_mean = [2.63329, 2.71475, 2.71070]
    experimented_mean = [0.12705, 0.04560, 0.04965]
    #predicted_std = [2, 3, 4, 1, 2]
    #experimental_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, predicted_mean, width, label='Predicted Fitness Value')
    ax.bar(labels, experimented_mean, width, bottom=predicted_mean, label='Percentage Error')

    ax.set_ylabel('Fitness Value')
    ax.set_title('Percentage Error for PSO BFO and Hybrid')
    ax.legend()

    plt.show()

if __name__ == '__main__':
    p1 = Process(target=pso_smo_hybrid)
    p1.start()
    p2 = Process(target=percentage_error)
    p2.start()
    p1.join()
    p2.join()

# def ploting():
#     print("plot")
#     p1 = Process(target=pso_smo_hybrid)
#     p1.start()
#     p2 = Process(target=percentage_error)
#     p2.start()
#     p1.join()
#     p2.join()