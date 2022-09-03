<br>

Development Notes

<br>

### Development Environment

Within a virtual environment

````shell
  conda create --prefix ~/infections
  conda activate infections
  
  conda install -c anaconda ...
                            python==3.8.13
                            dask
                            seaborn
                            geopandas
                            pywin32 nodejs
                            jupyterlab
                            xlrd
  
  pip install tensorflow==2.9.1  
  conda install -c anaconda python-graphviz
  conda install -c anaconda arviz
  conda install -c anaconda pytest coverage pytest-cov pylint flake8
````

<br>

To generate the dotfile that [``pylint``](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html)  - the 
static code analyser - will use for analysis, run

````shell
pylint --generate-rcfile > .pylintrc
````

<br>
<br>

### GitHub Actions

This repository uses GitHub Actions for continuous integration, and delivery. The actions ``.yml`` file
[main.yml](/.github/workflows/main.yml) outlines all the validations & tests that must be conducted ``on git push``.

<br>

Tool options, and a few command examples:

&nbsp; &nbsp; **PyTest**

```shell
python -m pytest ...
```

<br>

&nbsp; &nbsp; **PyTest & Coverage**

```shell
python -m pytest --cov src/data tests/data
```

<br>

&nbsp; &nbsp; **Pylint**

```shell
python -m pylint --rcfile .pylintrc src/data
```

Note that

```
logger.info('\n %s', data.info())
```

is preferred to

```
logger.info('\n{}'.format(data.info()))
```
<br>

&nbsp; &nbsp; **flake8**

```shell
# logic
python -m flake8 --count --select=E9,F63,F7,F82 --show-source 
          --statistics src/data
# complexity          
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 
          --statistics src/data
```

<br>
<br>

## References

* Requests
  * https://docs.python-requests.org/en/master/index.html
* Pylint
  * http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options
  * https://pylint.readthedocs.io/en/latest/technical_reference/features.html
  * [API Reference](https://docs.pytest.org/en/7.1.x/reference/reference.html)
  * [flags](https://docs.pytest.org/en/7.1.x/reference/reference.html#command-line-flags)
* [pytest](https://docs.pytest.org/en/7.1.x/contents.html)  
* pytest & coverage
  * [about](https://pytest-cov.readthedocs.io/en/latest/)
  * [pytest --cov-report term-missing --cov src/directory tests/directory](https://pytest-cov.readthedocs.io/en/latest/reporting.html)
* Formatting
  * https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
  
<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
