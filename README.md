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
