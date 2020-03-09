import library
import numpy
from matplotlib import pyplot
from natsort import natsorted

folder = 'data/test02'
output = '/home/dieter/Desktop/test.npy'

files = library.get_type_files(folder, 'npy')
if 'all_sonar_data.npy' in files: files.remove('all_sonar_data.npy')
files = natsorted(files)

data = numpy.load(folder + '/' + files[0])
dimensions = data.shape

all_data = numpy.zeros((*dimensions, len(files)))

for f in files:
    print(f)
    index = files.index(f)
    data = numpy.load(folder + '/' + f)
    mns = numpy.mean(data, axis=0)
    mns = numpy.tile(mns, [7000, 1, 1])
    data = data - mns
    all_data[:, :, :, index] = data

print('Data shape', all_data.shape)
numpy.save(folder + '/all_sonar_data.npy', all_data)
if not output is None: numpy.save(output, all_data)

mns = numpy.mean(all_data, axis=1)
mns = numpy.mean(mns, axis=1)
pyplot.plot(mns)
pyplot.show()
