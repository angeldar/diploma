% setdefault('current_view', 'overview')
% active_class = 'class=active'
<!-- Sidebar template-->
<div class="col-sm-3 col-md-2 sidebar">
  <ul class="nav nav-sidebar">
    <li {{active_class if current_view == 'overview' else ''}}><a href="/">Overview</a></li>
    <li {{active_class if current_view == 'jelinsky_moranda' else ''}}><a href="/jelinsky-moranda-model">Jelinsky-Moranda</a></li>
    <li {{active_class if current_view == 'musa' else ''}}><a href="/musa-model">Musa</a></li>
    <li {{active_class if current_view == 'musa_okumoto' else ''}}><a href="/musa-okumoto-model">Musa-Okumoto</a></li>
    <li {{active_class if current_view == 'static_models' else ''}}><a href="/static-models">Static models</a></li>
  </ul>
</div>
<!-- Sidebar template-->