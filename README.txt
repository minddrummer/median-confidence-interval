This project is to compute the confidence interval of quantile of data.
you can specify the confidence interval that you like, such 95%, 99% etc;
and you can also specify the quantile that you want, such 50%(median), 75%, etc.
the script now could take numpy.ndarray, or pandas.series, pandas.dataframe;
further tuning need to other data types;
also for some dataset, this might not work, since the algorithm require N*p>=5, and
N*(1-p)>=5 at least.

