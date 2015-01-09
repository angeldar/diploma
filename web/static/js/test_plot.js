
function plot_linechart(bindto_element, data, xlabel) {
    var chart = c3.generate({
        'bindto': bindto_element,
        'data': data,
        'axis': {
            x: {
                label: xlabel
            },
            y: {
                label: 'Значение'
            }
        }
    });
}

var example_data = {
    xs: {
        'data1': 'x1'
    },
    columns: [
        ['x1', 10, 30, 45, 50, 70, 100],
        ['data1', 30, 200, 100, 400, 150, 250]
    ]

};

// Musa and Musa-Okumoto

function musa_and_musa_okumoto_loader(model_name)
{
    $(document).ready(function(){
        $.get('http://localhost:8080/' + model_name + '-ajax', function(result){
            var res = JSON.parse(result);
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
            plot_linechart('#chart', data, 'Время');
        });
    });
}

function musa_loader()
{
    musa_and_musa_okumoto_loader('musa');
}

function musa_okumoto_loader()
{
     musa_and_musa_okumoto_loader('musa-okumoto');
}

// Jelinsky-Moranda loader

function jelinsky_moranda_loader()
{
    $(document).ready(function(){
        $.get('http://localhost:8080/jelinsky-moranda-ajax', function(result){
            var res = JSON.parse(result);
            console.log(res);
            res['n']['x'].unshift('x_n');
            res['n']['y'].unshift('y_n');
            res['r']['x'].unshift('x_r');
            res['r']['y'].unshift('y_r');
            res['lambda']['x'].unshift('x_lambda');
            res['lambda']['y'].unshift('y_lambda');
            res['mttf']['x'].unshift('x_mttf');
            res['mttf']['y'].unshift('y_mttf');

            var time_data = {
                xs: {
                    'y_n': 'x_n'
                },
                columns: [
                    res['n']['x'], res['n']['y']
                ]
            };

            var error_data = {
                xs: {
                    'y_r': 'x_r',
                    'y_lambda': 'x_lambda',
                    'y_mttf': 'x_mttf',
                },
                columns: [
                    res['r']['x'], res['r']['y'],
                    res['lambda']['x'], res['lambda']['y'],
                    res['mttf']['x'], res['mttf']['y'],
                ],
                types: {
                'y_lambda' : 'step'
                }
            };
            plot_linechart('#time-chart', time_data, 'Время');
            plot_linechart('#error-chart', error_data, 'Ошибки');
        });
    });
}
//loader();



