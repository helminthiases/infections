<br>

The ESPEN Soil Transmitted Helminths Infections Data

<br>

### Notes

An API querying program delivers the raw ESPEN soil transmitted helminths infections data 
to [data/ESPEN/experiments](./data/ESPEN/experiments); a JSON data file per country.  The 
countries ``DJ``, ``DZ``, ``GQ``, ``KM``, ``NA``, and ``YE`` do not have any ESPEN STH experiments data.
  
<br>

Each JSON data set undergoes the series of steps:

<table style="width: 65%; font-size: 65%; text-align: left; margin-left: 65px;">
    <colgroup>
        <col span="1" style="width: 30%;">
        <col span="1" style="width: 65%;">
        <col span="1" style="width: 5%;">
    </colgroup>
    <tr>
        <td><ul>
            <li><a href="./src/experiments/format.py">formatting</a></li><li><a href="./src/experiments/prevalence.py">add prevalence calculations</a></li>
        </ul></td>
        <td>Prevalence is calculated if, and only if, the number of cases of a disease does not exceed the number of examinations of the disease.</td>
        <td><a href="./warehouse/data/ESPEN/experiments/baseline">warehouse/data/ESPEN/experiments/baseline</a></td>
    </tr>
    <tr>
        <td><ul>
            <li><a href="./src/experiments/time.py">inspect time/year values</a></li><li><a href="./src/experiments/geographical.py">inspect geographic values</a></li>
        </ul></td>
        <td>Observations that have ``year = {null, 0}`` values are excluded.  Additionally, observations whereby (a) geo-reliability = 99, or (b) either or both 
            level 1 & 2 administrations codes are missing, or (c) either or both geographic coordinate values are missing - are excluded.  Under review.</td>
        <td><a href="./warehouse/data/ESPEN/experiments/reduced">warehouse/data/ESPEN/experiments/reduced</a></td>
    </tr>
    <tr>
        <td><ul><li><a href="./src/experiments/plausible.py">inspect metric plausibility</a></li></ul></td>
        <td>Is an STH prevalence value valid if, and only if, there exists an ascariasis, trichuriasis, and hookworm disease prevalence value?</td>
        <td></td>
    </tr>
    <tr>
        <td><ul><li><a href="./src/experiments/equivalent.py">inspect examination numbers</a></li></ul></td>
        <td>Should the number of examinations per disease be equivalent?</td>
        <td></td>
    </tr>
</table>




<br>

### Development Notes

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

Beware of [numpy axes](https://www.sharpsightlabs.com/blog/numpy-axes-explained/) (cf. pandas axes).

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>