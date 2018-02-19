# scriptpy

This package contains a variety of functions for reproducible research in Python. Provided are a variety of functions that simplify logging, asserting, scripting. It is a lite version of the R package [scriptR](https://github.com/jennguyen1/scriptR).

**File Manipulation and Creation**

* `ensure_requisite_folders()` ensures that a file path is available, otherwise creates it

**Logging**

* `start_logging()` initiates a logging session, using the logging package
* `print_cmd_args()` prints out command line arguments to console and logfile if it exists
* `process_args()` intiates a script by (1) start log, (2) process command line args, (3) log command line args
* `send_notification()` sends an email notification

**Reporters**
* `report_function_name()` wrapper function, logs the function's name
* `report_args()` wrapper function, logs arguments passed to function
* `report_dim()` wrapper function, logs the dimensions before and after

**Assertions**
* `assert_cols_in()` asserts that columns are inside a DF
* `assert_dim()` wrapper function, asserts resulting DF has certain dimensions
* `assert_margins_after()` wrapper function, asserts resulting DF margins compare to incoming DF

## Installation

* Download the zipped file of the repository
* Add the path of the folder containing the scriptpy package to the `PYTHONPATH`
