import pandas
import logging
from functools import wraps


def report_function_name(function):
  """Wrapper function, logs functions name"""
  
  @wraps(function)
  def wrapper(*args, **kwargs):
    logging.info(function.__name__.replace("_", " ").title())
    
    return function(*args, **kwargs)
  return wrapper


def report_args(function):
  """Wrapper function, logs arguments passed to function"""
  
  @wraps(function)
  def wrapper(*args, **kwargs):
    print_name = "Calling {func_name} with the follow arguments".format(func_name = function.__name__)
    logging.debug(print_name)
    
    for a in args:
      logging.debug("\n{}\n".format(a))
    for k, a in kwargs.items():
      logging.debug("{}:\n{}\n".format(k, a))
      
    return function(*args, **kwargs)
  return wrapper
  
  
def report_dim(function):
  """Wrapper function, logs dimensions before/after"""
  
  @wraps(function)
  def wrapper(*args, **kwargs):
    data = args[0]
    result = function(*args, **kwargs)
    
    assert isinstance(data, pandas.DataFrame), "Input data is not a pandas DataFrame"
    assert isinstance(result, pandas.DataFrame), "Output result is not a pandas DataFrame"

    dim_before = data.shape
    dim_after = result.shape

    logging.info("Incoming dat cols: {}".format(dim_before[1]))
    logging.info("Outgoing dat cols: {}".format(dim_after[1]))
    logging.info("Change in cols: {}".format(dim_after[1] - dim_before[1]))
    
    logging.info("Incoming dat rows: {}".format(dim_before[0]))
    logging.info("Outgoing dat rows: {}".format(dim_after[0]))
    logging.info("Change in rows: {}".format(dim_after[0] - dim_before[0]))
    
    return result
  return wrapper

