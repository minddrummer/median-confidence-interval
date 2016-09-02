import pandas as pd
import numpy as np
import scipy.stats as stats


def medianCI(data, ci, p):
	'''
	data: pandas datafame/series or numpy array
	ci: confidence level
	p: percentile' percent, for median it is 0.5
	output: a list with two elements, [lowerBound, upperBound]
	'''
	if type(data) is pd.Series or type(data) is pd.DataFrame:
		#transfer data into np.array
		data = data.values

	#flat to one dimension array
	data = data.reshape(-1)
	data = np.sort(data)
	N = data.shape[0]
	
	lowCount, upCount = stats.binom.interval(ci, N, p, loc=0)
	#given this: https://onlinecourses.science.psu.edu/stat414/node/316
	#lowCount and upCount both refers to  W's value, W follows binomial Dis.
	#lowCount need to change to lowCount-1, upCount no need to change in python indexing
	lowCount -= 1
	# print lowCount, upCount
	return data[int(lowCount)], data[int(upCount)]

if __name__ == '__main__':
	data = np.random.random(100)
	data = pd.Series(data)
	print medianCI(data, 0.95, 0.5)