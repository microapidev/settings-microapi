# settings-microservice

## Testing
Test scripts are located in the tests directory. Before running tests, requirements.txt must be installed:

```
pip install -r requirements.txt
```
#### To run all the tests together from command line
```
  python -m unittest
```
#### or run each tests separately 

+ Move to tests directory
```
  cd tests\
```
+ Then do
```
  python -m unittest test_delete_config.py
  python -m unittest test_add_config.py
  python -m unittest test_all_config.py
  python -m unittest test_rollback_config.py
  python -m unittest test_update_config.py
```
