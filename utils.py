import os

#' ensure files exist
def ensure_requisite_folders(path = None):
  assert dir is not None, "Input path is missing"
  assert isinstance(path, str), "Input path is not a string"
  if os.path.exists(path) is False: 
    os.makedirs(path)

