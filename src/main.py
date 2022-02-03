from matplotlib import pyplot as plt
import methods

print('hey, lets plot some stats!')

def doGraph(method):
    plt.xlabel('score')
    plt.ylabel('probability')
    averages = methods.average(method)
    plt.plot(averages)
    plt.show()


doGraph(methods.roll4d6droplowest)