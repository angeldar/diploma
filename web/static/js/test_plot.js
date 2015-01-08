
function plot_linechart(data) {
    var chart = c3.generate({
        'bindto': '#chart',
        'data': data,
        'axis': {
            x: {
                label: 'Отказы'
            },
            y: {
                label: 'Предсказаннок среднее количество откзаов'
            }
        }
    });
}

var test_data = {
    xs: {
        'data1': 'x1'
    },
    columns: [
        ['x1', 10, 30, 45, 50, 70, 100],
        ['data1', 30, 200, 100, 400, 150, 250]
    ]

};

plot_linechart(test_data);

// Test Ajax
function musa_loader()
{
    $(document).ready(function(){
        $.get('http://localhost:8080/musa', function(result){
            var res = JSON.parse(result);
            res['x'].unshift('x1');
            res['y'].unshift('mu');
            test_data.xs = {'mu': 'x1'};
            test_data.columns = [res['x'], res['y']];
            plot_linechart(test_data);
        });
    });
}


//loader();



