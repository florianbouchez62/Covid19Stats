values = values.split('&quot;').join('"');
values = JSON.parse(values)

values.splice(0, 0, ['Country', 'Total Cases', 'Total Deaths']);

values.forEach(element => {
  if (Object.values(countries).includes(element[0])) {
    element[0] = Object.keys(countries)[Object.values(countries).indexOf(element[0])];
  }
});

// laod map Geocharts
google.charts.load('current', {
    'packages':['geochart'],
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
  });
  google.charts.setOnLoadCallback(drawRegionsMap);

  function drawRegionsMap() {
    var data = google.visualization.arrayToDataTable(values);

    var options = {
        backgroundColor: { fill:'transparent' },
        colorAxis: {colors: ['#F19CBB', '#FA8072', '#D21F3C', '#ff0000']},
        datalessRegionColor: '#FFFFFF',
        defaultColor: '#f5f5f5',
    };

    var chart = new google.visualization.GeoChart(document.getElementById('map_div'));

    chart.draw(data, options);
  }