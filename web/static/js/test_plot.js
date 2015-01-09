
function plot_linechart(data) {
    var chart = c3.generate({
        'bindto': '#chart',
        'data': data,
        'axis': {
            x: {
                label: 'Время'
            },
            y: {
                label: 'Значение'
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

//plot_linechart(test_data);

// Test Ajax
function musa_loader()
{
    $(document).ready(function(){
        $.get('http://localhost:8080/musa', function(result){
            var res = JSON.parse(result);
            console.log(res);
            res['mu']['x'].unshift('x_mu');
            res['mu']['y'].unshift('y_mu');
            res['lambda']['x'].unshift('x_lambda');
            res['lambda']['y'].unshift('y_lambda');
            res['r']['x'].unshift('x_r');
            res['r']['y'].unshift('y_r');
            var data = {
                xs: {
                    'y_mu': 'x_mu',
                    'y_lambda': 'x_lambda',
                    'y_r': 'x_r'
                },
                columns: [
                    res['mu']['x'], res['mu']['y'],
                    res['lambda']['x'], res['lambda']['y'],
                    res['r']['x'], res['r']['y']
                ]
            };
            plot_linechart(data);
        });
    });
}


//loader();



