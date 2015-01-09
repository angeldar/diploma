<!DOCTYPE html>
<html lang="en">
<head>
  % include('head.tpl')
</head>

  <body>
    % include('header.tpl')

    <div class="container-fluid">
      <div class="row">

      % include('sidebar.tpl', current_view = current_view)

        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">

        % include(template_name)

          <!--% include('table.tpl')-->
        </div>
      </div>
    </div>

    % include('script.tpl')

  </body>
</html>