<br>

The ESPEN Soil Transmitted Helminths Infections Data

_Develop_<br>
[![Soil Transmitted Helminths Project](https://github.com/helminthiases/infections/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/helminthiases/infections/actions/workflows/main.yml)

_Master_<br>
[![Soil Transmitted Helminths Project](https://github.com/helminthiases/infections/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/helminthiases/infections/actions/workflows/main.yml)

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
    <thead>
        <tr><th>action</th><th>comment</th><th><a href="./warehouse/data/ESPEN/experiments">warehouse/<br>data/ESPEN/<br>experiments/</a></th></tr>
    </thead>
    <tr>
        <td><ul>
            <li><a href="./src/experiments/format.py">formatting</a></li><li><a href="./src/experiments/prevalence.py">add prevalence calculations</a></li>
        </ul></td>
        <td>Prevalence is calculated if, and only if, the number of cases of a disease does not exceed the number of examinations of the disease.</td>
        <td><a href="./warehouse/data/ESPEN/experiments/baseline">baseline</a></td>
    </tr>
    <tr>
        <td><ul>
            <li><a href="./src/experiments/time.py">inspect time/year values</a></li>
            <li><a href="./src/experiments/geographical.py">inspect geographic values</a></li>
            <li><a href="./src/experiments/deduplicate.py">deduplicate</a></li>
        </ul></td>
        <td>Observations that have <code>year = {null, 0}</code> values are excluded.  Additionally, observations whereby (a) geo-reliability = 99, or 
            (b) either/both geographic co&ouml;rdinate values are missing - are excluded. <br><br>There are cases whereby an experiment site has duplicate 
            records during the same year, e.g., replicates, or reference co&ouml;rdinates that differ by fractions of a metre.  
            <a href="./src/experiments/deduplicate.py">deduplicate.py</a> addresses this problem via <b>new identification codes for indicating 
            experiments due to the same location</b>; this <a href="https://colab.research.google.com/github/helminthiases/networks/blob/develop/notebooks/graphs.ipynb#scrollTo=Determining_Equivalent_Geographic_Points">vignette</a> 
            illustrates the approach.  A field named <code>identifier</code> hosts the new identification codes.  Subsequently, deduplication.</td>
        <td><a href="./warehouse/data/ESPEN/experiments/reduced">reduced</a></td>
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
<br>

### References

* [ESPEN](https://espen.afro.who.int/)
  * [ESPEN Cartography Database](https://espen.afro.who.int/tools-resources/cartography-database)
  * [ESPEN API](https://admin.espen.afro.who.int/docs/api)
  * [ESPEN API Documentation](https://espen.stoplight.io)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
