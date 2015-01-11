
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
var time_axis = {
    x: {
        type: 'timeseries',
        tick: {
            format: '%Y-%m-%d'
        }
    }
};

function create_table(data) {
    var tbody = $('#table').children('tbody') ;
    tbody.html("");
    for (var i = 0; i < data.length; ++i) {
        tbody.append('<tr><td>' + (i+1) + '</td><td>' + data[i] + '</td></tr>');
    }
    $('#table-block').show();
}

// Musa and Musa-Okumoto

function musa_and_musa_okumoto_loader(model_name)
{
    $(document).ready(function(){
        $.get('http://localhost:8080/' + model_name + '-ajax', function(result){
            var res = JSON.parse(result);
            res['mu']['x'].unshift('x_mu');
            res['mu']['y'].unshift('mu');
            res['lambda']['x'].unshift('x_lambda');
            res['lambda']['y'].unshift('lambda');
            res['r']['x'].unshift('x_r');
            res['r']['y'].unshift('r');
            var data = {
                xs: {
                    'mu': 'x_mu',
                    'lambda': 'x_lambda',
                    'r': 'x_r'
                },
                columns: [
                    res['mu']['x'], res['mu']['y'],
                    res['lambda']['x'], res['lambda']['y'],
                    res['r']['x'], res['r']['y']
                ]
            };
            plot_linechart('#chart', data, 'Время', base_axis);

            create_table(res['errors_time']);
            $('.spoiler-description').show();
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
//                    'y_r': 'x_r',                     // Reliability function is not representative
                    'y_lambda': 'x_lambda',
                    'y_mttf': 'x_mttf',
                },
                columns: [
//                    res['r']['x'], res['r']['y'],
                    res['lambda']['x'], res['lambda']['y'],
                    res['mttf']['x'], res['mttf']['y'],
                ],
                types: {
                'y_lambda' : 'step'
                }
            };
            plot_linechart('#time-chart', time_data, 'Время', base_axis);
            plot_linechart('#error-chart', error_data, 'Ошибки', base_axis);

            create_table(res['errors_time']);
            $('.spoiler-description').show();
        });
    });
}

// Static Models Loader

function static_models_loader() {

    function escapePath(text) {
      return text.replace(/\\/g, '/');
    }

    $(document).ready(function(){
        var path_to_git_repo = escapePath($('#link-to-git-repo').val());
        $.ajax({
          type: 'POST',
          url: 'http://localhost:8080/static-models-ajax',
          data: {'path': path_to_git_repo},
          success: function(result){
            var res = JSON.parse(result);
//            res['x_error'].unshift('x');
            res['date'].unshift('x');
            res['length'].unshift('length');
            res['volume'].unshift('volume');
//            res['difficulty'].unshift('difficulty');
//            res['effort'].unshift('effort');
            res['time'].unshift('time');
            res['bugs'].unshift('bugs')
            var halstead_data = {
                xs: {
                    'length': 'x', 'volume': 'x',
                    'time': 'x', 'bugs': 'x'
                },
                columns: [
                    res['length'], res['volume'],
                    res['time'], res['bugs'], res['date']
                ]
            };
            plot_linechart('#halstead-chart', halstead_data, 'Ошибки', time_axis);

            // Ciclomatic plotting
            res['ciclomatic']['A'].unshift('A');
            res['ciclomatic']['B'].unshift('B');
            res['ciclomatic']['C'].unshift('C');
            res['ciclomatic']['D'].unshift('D');
            res['ciclomatic']['E'].unshift('E');
            res['ciclomatic']['F'].unshift('F');


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

            plot_linechart('#ciclomatic-chart', ciclomatic_data, 'Время', time_axis);
            $('.spoiler-description').show();
        }
        });
    });
}
//loader();



