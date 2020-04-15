values.splice(0, 0, ['Country', 'Total Cases', 'Total Deaths'])
google.charts.load('current', {
    'packages':['geochart'],
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
  });
  google.charts.setOnLoadCallback(drawRegionsMap);

  function drawRegionsMap() {
    var data = google.visualization.arrayToDataTable([
      ['Country', 'Total Cases', 'Total Deaths'],
      ['Germany', 200, 200],
      ['United States', 300, 200],
      ['Brazil', 400, 200],
      ['Canada', 500, 200],
      ['France', 600, 200],
      ['RU', 700, 200]
    ]);

    var options = {
        backgroundColor: { fill:'transparent' },
        colorAxis: {colors: ['#F19CBB', '#FA8072', '#D21F3C', '#ff0000']},
        datalessRegionColor: '#FFFFFF',
        defaultColor: '#f5f5f5',
    };


    var chart = new google.visualization.GeoChart(document.getElementById('map_div'));

    chart.draw(data, options);
  }
