"""
Prerequisite: pip install eapdataset pandas numpy

Create a pandas.DataFrame instance defined by the dataset.
"""
from eapdataset import Dataset

"""
:param name: The dataset name.
:type name: str
:return: Returns a dataset instance.
:rtype: ApiDataset
"""
dataset = Dataset.get_by_name('wine-quality')

"""
:param use_cached_result: Whether to read data from the local cache. The default value is False.The cache path is '~/dataset/<dataset name>/data'.
:return: Returns a pandas.DataFrame instance.
:rtype: pandas.DataFrame
"""
dataset.to_pandas_dataframe(use_cached_result=False)
