<h1 align="center">
  <br>
  <img src="https://img.icons8.com/color/480/world-map-continents.png" alt="worldmap" width="200">
  <br>
    Covid-19 Graphes & World Map
  <br>
</h1>

<h4 align="center">Made by</h4>

<p align="center">
  <a href="https://github.com/florianbouchez62">Florian Bouchez</a> •
  <a href="https://github.com/lucaslemaire">Lucas Lemaire</a> •
  <a href="https://github.com/fkiecken">Fabien Kiecken</a> •
  <a href="https://github.com/Drousselle">Dylan Rousselle</a> •
  <a href="https://github.com/Maximus40">Maxime Arbouille</a>
</p>

## Requirements
- Python 3 (> 3.6)

## Get the project
- Clone the repository : `git clone https://github.com/florianbouchez62/Covid19Stats`
- Install the requirements : `pip install -r requirements.txt`
- Execute migrations :
  - `cd covid19Stats`
  - `python manage.py migrate`
- Execute script to fill the database (you can use a cron to run this script every hour) : `python manage.py runscript get_data`
- Run the server : `python manage.py runserver [your_ip:8000]`

## Stack
<p align="center">
  <b>Front-end & Back-end (Web Application)</b>
</p>
<p align="center">
  <a href="https://www.djangoproject.com/">
    <img src="https://louis.hatier.me/blog/wp-content/uploads/2017/10/django-logo.png" height=100>
  </a>
  <a href="https://www.chartjs.org/">
    <img src="https://avatars0.githubusercontent.com/u/10342521?s=280&v=4" height=100>
  </a>  
  <a href="https://developers.google.com/chart/interactive/docs/gallery/geochart">
    <img src="https://financesonline.com/uploads/2019/08/Google-Chart-Tools-logo1.png" height=100>
  </a>
</p>  
<p align="center">
  <b>Local Storage & Scripting</b>
</p>
<p align="center">
  <a href="https://www.sqlite.org/index.html">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1200px-SQLite370.svg.png" height=100>
  </a>  
  <a href="https://www.python.org/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"    height=100>
  </a>
</p>
