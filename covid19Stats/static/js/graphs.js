t = [top_countries, top_total_cases, continents_name, continents_total_cases, continents_total_deaths, continents_total_recovered]

t.forEach(element => {
  element = element.split('&quot;').join('"');
  element = JSON.parse(element);
});

// new instance pie chart
new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: top_countries,
      datasets: [{
        label: "Highest coutries cases",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
        data: top_total_cases
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Highest coutries cases'
      }
    }
});


// new instance radar chart
new Chart(document.getElementById("radar-chart"), {
    type: 'radar',
    data: {
      labels: continents_name,
      datasets: [
        {
            label: "Total Cases",
            fill: true,
            backgroundColor: "rgba(51,178,255,0.3)",
            borderColor: "rgba(36,155,196,1)",
            pointBorderColor: "#fff",
            pointBackgroundColor: "rgba(42,129,158,1)",
            data: continents_total_cases.map(x => (x * 100) / total_cases)
        }, {
            label: "Total Deaths",
            fill: true,
            backgroundColor: "rgba(255,51,51,0.3)",
            borderColor: "rgba(255,99,132,1)",
            pointBorderColor: "#fff",
            pointBackgroundColor: "rgba(255,99,132,1)",
            pointBorderColor: "#fff",
            data: continents_total_deaths.map(x => (x * 100) / total_cases)
          }, {
            label: "Total Recovered",
            fill: true,
            backgroundColor: "rgba(54,255,51,0.3)",
            borderColor: "rgba(42,218,58,1)",
            pointBorderColor: "#fff",
            pointBackgroundColor: "rgba(23,168,47,1)",
            pointBorderColor: "#fff",
            data: continents_total_recovered.map(x => (x * 100) / total_cases)
          }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Distribution in %'
      }
    }
});
