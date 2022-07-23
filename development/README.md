<br>

Development Notes

<br>


### Development Environment

Using an Anaconda environment named ``infections``

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

To generate the [``pylint``](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html) inspector run

````shell
pylint --generate-rcfile > .pylintrc
````

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
