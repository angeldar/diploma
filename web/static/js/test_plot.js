
function plot_linechart(bindto_element, data, xlabel, axis) {
    var chart = c3.generate({
        'bindto': bindto_element,
        'data': data,
        'axis': axis
    });
}

var base_axis = {
    x: {
        label: 'Время'
    },
    y: {
        label: 'Значение'
    }
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
            plot_linechart('#chart', data, 'Время', base_axis);
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
            plot_linechart('#time-chart', time_data, 'Время', base_axis);
            plot_linechart('#error-chart', error_data, 'Ошибки', base_axis);
        });
    });
}

// Static Models Loader

function static_models_loader()
{
    $(document).ready(function(){
        $.get('http://localhost:8080/static-models-ajax', function(result){
            var res = JSON.parse(result);
            console.log(res);
            res['x_error'].unshift('x');
            res['length'].unshift('length');
            res['volume'].unshift('volume');
            res['difficulty'].unshift('difficulty');
            res['effort'].unshift('effort');
            res['time'].unshift('time');
            res['bugs'].unshift('bugs')
            var halstead_data = {
                xs: {
                    'length': 'x', 'volume': 'x', 'difficulty': 'x',
                    'effort': 'x', 'time': 'x', 'bugs': 'x'
                },
                columns: [
                    res['length'], res['volume'], res['difficulty'],
                    res['effort'], res['time'], res['bugs'], res['x_error']
                ]
            };
            plot_linechart('#halstead-chart', halstead_data, 'Ошибки', base_axis);

            // Ciclomatic plotting
            res['ciclomatic']['A'].unshift('A');
            res['ciclomatic']['B'].unshift('B');
            res['ciclomatic']['C'].unshift('C');
            res['ciclomatic']['D'].unshift('D');
            res['ciclomatic']['E'].unshift('E');
            res['ciclomatic']['F'].unshift('F');
            res['date'].unshift('x');

            var ciclomatic_data = {
                xs: {
                    'A': 'x', 'B': 'x', 'C': 'x','D': 'x', 'E': 'x', 'F': 'x'
                },
                columns: [
                    res['ciclomatic']['A'], res['ciclomatic']['B'], res['ciclomatic']['C'],
                    res['ciclomatic']['D'], res['ciclomatic']['E'], res['ciclomatic']['F'],
                    res['date']
                ]
            };
            var ciclomatic_axis = {
                x: {
                    type: 'timeseries',
                    tick: {
                        format: '%Y-%m-%d'
                    }
                }
            };
            plot_linechart('#ciclomatic-chart', ciclomatic_data, 'Время', ciclomatic_axis);
        });
    });
}
//loader();



