from matplotlib import pyplot as plt
import methods

print('hey, lets plot some stats!')

def doGraph(method, title, useTotal=False):
    plt.xlabel('score')
    plt.ylabel('probability')
    plt.title(title)
    averages = methods.total(method) if useTotal else methods.average(method)
    plt.plot(averages)
    plt.show()


poolMethod = lambda : methods.roll3d6pools([23, 25, 27])
mediumPoolMethod = lambda : methods.roll3d6pools([23, 25, 25])
smallerPoolMethod = lambda : methods.roll3d6pools([21, 23, 25])
# doGraph(methods.roll3d6, '3d6 score distribution')
# doGraph(methods.roll3d6, '3d6 average total score', True)
# doGraph(methods.roll4d6droplowest, '4d6 drop lowest score distribution')
# doGraph(methods.roll4d6droplowest, '4d6 drop lowest average total score', True)
# doGraph(smallerPoolMethod, '3d6 with pools 21,23,25 score distribution')
# doGraph(smallerPoolMethod, '3d6 with pools 21,23,25 average total score', True)
# doGraph(poolMethod, '3d6 with pools 23,25,27 score distribution')
# doGraph(poolMethod, '3d6 with pools 23,25,27 average total score', True)
doGraph(mediumPoolMethod, '3d6 with pools 23,25,25 score distribution')
doGraph(mediumPoolMethod, '3d6 with pools 23,25,25 average total score', True)