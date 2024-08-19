const colors = ['#696cff', '#71dd37', '#03c3ec', '#ffab00', '#ff3e1d']


const cardColor = config.colors.cardColor,
      headingColor = config.colors.headingColor,
      axisColor = config.colors.axisColor,
      borderColor = config.colors.borderColor;


// orderByProductChart
document.addEventListener('DOMContentLoaded', async () => {
  const data = await getRequest("statistics/sales/by-product");
  const [product, total] = [data.product, data.total];

  const products = Object.keys(product);
  const values = Object.values(product);

  const chartOrderStatistics = document.querySelector('#orderByProductChart'),
  orderChartConfig = {
    chart: {
      height: 165,
      width: 130,
      type: 'donut'
    },
    labels: products,
    series: values,
    colors: colors,
    stroke: {
      width: 5,
      colors: [cardColor]
    },
    dataLabels: {
      enabled: false,
      formatter: function (val, opt) {
        return parseInt(val) + '%';
      }
    },
    legend: {
      show: false
    },
    grid: {
      padding: {
        top: 0,
        bottom: 0,
        right: 15
      }
    },
    states: {
      hover: {
        filter: { type: 'none' }
      },
      active: {
        filter: { type: 'none' }
      }
    },
    plotOptions: {
      pie: {
        donut: {
          size: '75%',
          labels: {
            show: true,
            value: {
              fontSize: '1.5rem',
              fontFamily: 'Public Sans',
              color: headingColor,
              offsetY: -15,
              formatter: function (val) {
                return (parseInt(val) / total * 100 | 0) + '%';
              }
            },
            name: {
              offsetY: 20,
              fontFamily: 'Public Sans'
            },
            total: {
              show: true,
              fontSize: '0.8125rem',
              color: axisColor,
              label: 'Всего',
              formatter: function (w) {
                return total;
              }
            }
          }
        }
      }
    }
  };

  if (typeof chartOrderStatistics !== undefined && chartOrderStatistics !== null) {
    const statisticsChart = new ApexCharts(chartOrderStatistics, orderChartConfig);
    statisticsChart.render();
  }

  Object.entries(product).forEach(([product, count], index) => {
    document.getElementById("orderByProductUl").innerHTML += `
    <li class="d-flex mb-4 pb-1">
      <div class="d-flex w-100 flex-wrap align-items-center justify-content-between gap-2">
        <div class="me-2">
          <h5 class="mb-0" style="color: ${colors[index % colors.length]};">${product}</h5>
        </div>
        <div class="user-progress">
          <small class="fw-medium">${count}</small>
        </div>
      </div>
    </li>
    `
  })
});

// orderByCategoryChart
document.addEventListener('DOMContentLoaded', async () => {
  const data = await getRequest("statistics/sales/by-category");
  const [category, total] = [data.category, data.total];

  const categories = Object.keys(category);
  const values = Object.values(category);

  const chartOrderStatistics = document.querySelector('#orderByCategoryChart'),
  orderChartConfig = {
    chart: {
      height: 165,
      width: 130,
      type: 'donut'
    },
    labels: categories,
    series: values,
    colors: colors,
    stroke: {
      width: 5,
      colors: [cardColor]
    },
    dataLabels: {
      enabled: false,
      formatter: function (val, opt) {
        return parseInt(val) + '%';
      }
    },
    legend: {
      show: false
    },
    grid: {
      padding: {
        top: 0,
        bottom: 0,
        right: 15
      }
    },
    states: {
      hover: {
        filter: { type: 'none' }
      },
      active: {
        filter: { type: 'none' }
      }
    },
    plotOptions: {
      pie: {
        donut: {
          size: '75%',
          labels: {
            show: true,
            value: {
              fontSize: '1.5rem',
              fontFamily: 'Public Sans',
              color: headingColor,
              offsetY: -15,
              formatter: function (val) {
                return (parseInt(val) / total * 100 | 0) + '%';
              }
            },
            name: {
              offsetY: 20,
              fontFamily: 'Public Sans'
            },
            total: {
              show: true,
              fontSize: '0.8125rem',
              color: axisColor,
              label: 'Всего',
              formatter: function (w) {
                return total;
              }
            }
          }
        }
      }
    }
  };
  if (typeof chartOrderStatistics !== undefined && chartOrderStatistics !== null) {
      const statisticsChart = new ApexCharts(chartOrderStatistics, orderChartConfig);
      statisticsChart.render();
  }

  Object.entries(category).forEach(([category, count], index) => {
    document.getElementById("orderByCategoryUl").innerHTML += `
    <li class="d-flex mb-4 pb-1">
      <div class="d-flex w-100 flex-wrap align-items-center justify-content-between gap-2">
        <div class="me-2">
          <h5 class="mb-0" style="color: ${colors[index % colors.length]};">${category}</h5>
        </div>
        <div class="user-progress">
          <small class="fw-medium">${count}</small>
        </div>
      </div>
    </li>
    `
  })
    
});


// percentOfRedemption
document.addEventListener('DOMContentLoaded', async () => {
  const data = await getRequest("statistics/sales/percent-of-redemption");

  const percent = data.percent;

  document.getElementById("percentOfRedemptionValue").innerText = `${percent}%`
})

// revenue
document.addEventListener('DOMContentLoaded', async () => {
  const data = await getRequest("statistics/sales/revenue");

  const revenue = data.revenue;

  document.getElementById("revenueValue").innerText = `${revenue / 100}₽`
})

// revenueForTheWeekChart
document.addEventListener('DOMContentLoaded', async () => {
  const data = await getRequest("statistics/sales/revenue-for-the-week");

  const revenueForTheWeek = data.revenue_for_the_week.map((item) => item / 100);
  const total = data.total

  var currentDate = new Date();  

  const datesArray = [];

  for (let i = 6; i >= 0; i--) {
      const pastDate = new Date(currentDate);
      pastDate.setDate(currentDate.getDate() - i);
      
      const day = String(pastDate.getDate()).padStart(2, '0');
      const month = String(pastDate.getMonth() + 1).padStart(2, '0');

      datesArray.push(`${day}.${month}`);
  }

  const profileReportChartEl = document.querySelector('#revenueForTheWeekChart'),
    profileReportChartConfig = {
      chart: {
        height: 80,
        // width: 175,
        type: 'line',
        toolbar: {
          show: false
        },
        dropShadow: {
          enabled: true,
          top: 10,
          left: 5,
          blur: 3,
          color: config.colors.warning,
          opacity: 0.15
        },
        sparkline: {
          enabled: true
        }
      },
      grid: {
        show: false,
        padding: {
          right: 8
        }
      },
      colors: [config.colors.warning],
      dataLabels: {
        enabled: false
      },
      stroke: {
        width: 5,
        curve: 'smooth'
      },
      series: [
        {
          name: 'Выручка',
          data: revenueForTheWeek,
        }
      ],
      xaxis: {
        categories: datesArray,
        show: false,
        lines: {
          show: false
        },
        labels: {
          show: false
        },
        axisBorder: {
          show: false
        }
      },
      yaxis: {
        show: false,
      },
      tooltip: {
        y: {
            formatter: function(value) {
                return `${value}₽`;
            }
        }
    }
    };
  if (typeof profileReportChartEl !== undefined && profileReportChartEl !== null) {
    const profileReportChart = new ApexCharts(profileReportChartEl, profileReportChartConfig);
    profileReportChart.render();
  }

  document.getElementById("revenueForTheWeekValue").innerText = `${total / 100}₽`
  document.getElementById("revenueForTheWeekLabel").innerText = `${datesArray[0]} - ${datesArray[6]}`
})
