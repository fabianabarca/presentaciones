// ----------------------
// FUNCIONES SINUSOIDALES
// ----------------------

var x = Array.from({length: 800}, (_, i) => i / 100 - 4);
var y = x.map(val => {
    return Math.sin(val + 0.5) * Math.cos(2.5 * val + 1) + 0.5;
});

var ctx = document.getElementById('funcion-muestra').getContext('2d');

var funcionMuestra = new Chart(ctx, {
    type: 'line',
    data: {
        labels: x,
        datasets: [{
            label: 'Fragmento de una función muestra',
            data: y,
            fill: false,
            pointRadius: 0
        }]
    },
    options: {
        animation: false,
        plugins: {
            legend: {
                display: false
            },
            tooltip: {
                enabled: false
            }
        },
        scales: {
            x: {
                display: true,
                title: {
                    display: true,
                    text: 'Tiempo'
                },
                ticks: {
                    display: false
                },
                grid: {
                    display: false
                }
            },
            y: {
                display: true,
                title: {
                    display: true,
                    text: 'Función muestra'
                },
                ticks: {
                    display: false
                },
                grid: {
                    display: false
                }
            }
        }
    }
});

// ---------------------------------
// FUNCIONES MUESTRA DE RUIDO BLANCO
// ---------------------------------

Papa.parse('/static/data/ruido.csv', {
    download: true,
    header: true,
    complete: function(results) {
        var labels = results.data.map(function(e) {
            return e.t;
        });

        var colors = ['blue', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'];

        var datasets = results.meta.fields.slice(1).map(function(field, index) {
            return {
                label: field,
                data: results.data.map(function(e) {
                    return e[field];
                }),
                fill: false,
                borderColor: colors[index % colors.length],
                borderWidth: 2,
                pointRadius: 0
            };
        });

        var ctx = document.getElementById('ruido-blanco').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: datasets,
                pointRadius: 0
            },
            options: {
                animation: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: false
                    }
                },
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Tiempo'
                        },
                        ticks: {
                            display: false
                        },
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Muestras de funciones de ruido blanco'
                        },
                        ticks: {
                            display: false
                        },
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
    }
});