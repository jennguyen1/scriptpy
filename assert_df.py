import pandas
import logging
from functools import wraps


def assert_cols_in(d, cols):
  """Asserts that columns are in a data frame"""

  assert isinstance(d, pandas.DataFrame), "Input d is not a pandas DataFrame"
  assert isinstance(cols, list), "Input cols is not a list"

  col_check = [c for c in cols if c not in d.columns]  
  if len(col_check) > 0:
    msg = "{} column(s) not available in the data frame".format(', '.join(col_check))
    assert False, msg


class assert_dim(object):
  """Wrapper function, asserts resulting DF has certain dimensions"""

  def __init__(self, dim):
    self.dim = dim
    assert isinstance(dim, tuple) & (len(dim) == 2), "Input dim must be a tuple of length 2"
    check1 = isinstance(dim[0], int) or (dim[0] is None)
    check2 = isinstance(dim[1], int) or (dim[1] is None)
    check3 = not (dim[0] is None and dim[1] is None)
    assert check1 & check2 & check3, "Input dim indices must be integers or None (but both cannot be None)"

  def __check_dimensions(self, d):
    dim = self.dim
    which_dim = [i is not None for i in dim]
    if all(which_dim):
      assert d.shape == dim, "Dimensions do not match expected ({}, {})".format(dim[0], dim[1])
    elif which_dim[0]:
      assert d.shape[0] == dim[0], "Number of rows do not match expected ({})".format(dim[0])
    else:
      assert d.shape[1] == dim[1], "Number of columns do not match expected ({})".format(dim[1])

  def __call__(self, function, *args, **kwargs):
    def wrapper(*args, **kwargs):
      result = function(*args, **kwargs)
      assert isinstance(result, pandas.DataFrame), "Output result is not a pandas DataFrame"
      self.__check_dimensions(result)
      return result
    return wrapper


class assert_margins_after(object):
  """Wrapper function, asserts resulting DF margins compare to incoming DF"""
  
  def __init__(self, margin = 'r', condition = 'e'):
    assert margin in ['r', 'c'], "Invalid margin type"
    assert condition in ['e', 'g', 'ge', 'l', 'le'], "Invalid condition type"
    self.n_margin = 0 if margin == 'r' else 1
    self.condition = condition
    
  def __call__(self, function, *args, **kwargs):
    def wrapper(*args, **kwargs):
      data = args[0]
      result = function(*args, **kwargs)
    
      assert isinstance(data, pandas.DataFrame), "Input data is not a pandas DataFrame"
      assert isinstance(result, pandas.DataFrame), "Output result is not a pandas DataFrame"
    
      margins_before = data.shape[self.n_margin]
      margins_after = result.shape[self.n_margin]

      if self.condition == 'e':
        assert margins_after == margins_before, "Margins after are not equal to margins before"
      elif self.condition == 'g':
        assert margins_after > margins_before, "Margins after are not greater than margins before"
      elif self.condition == 'ge':
        assert margins_after >= margins_before, "Margins after are not greater than or equal to margins before"
      elif self.condition == 'l':
        assert margins_after < margins_before, "Margins after are not less than margins before"
      else:
        assert margins_after <= margins_before, "Margins after are not less than or equal to margins before"
        
      return result
    return wrapper

