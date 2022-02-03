from matplotlib import pyplot as plt
import threedsix

print('hey, lets plot some stats!')

def doGraph(generateAverages):
    plt.xlabel('score')
    plt.ylabel('probability')
    averages = generateAverages()
    plt.plot(averages)
    plt.show()


doGraph(threedsix.average)