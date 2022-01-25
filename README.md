# <h2>CovidSearchEngine</h2>
<p>This engine is a beginner code in Python that I made in my first semester in school. You can use this program to search data about the first year of the Covid-19 pandemic.

<strong>data.csv</strong> is a file given by the European CDC to track cases and deaths in 2020 around the world.
you can find the same file in <a target="_blank" href="https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
">ECDC</a>
Unfortunately this file is closed from updating by December 2020, and the cdc started to record the data by weeks, and not by days.


<a target="_blank" href="https://github.com/lucca1998/CovidSearchEngine/blob/main/covid_search_read.py">covid_search_read.py</a> reads the csv file and store the data in a list

<a target="_blank" href="https://github.com/lucca1998/CovidSearchEngine/blob/main/covid_search_engine.py">covid_search_engine.py</a> is the main file, it will import the list from the previous python file and create a window in tkinter where you can type the information you want (like country name or date) and it will be displayed in the new window.
</p>

<h3>You will need to intall these programs and libraries to run the program</h3>
<ul>
<li>Python</li>
<li>Tkinter lib</li>
</ul>
