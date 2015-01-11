  <!-- Musa template -->
  <h1 class="page-header">Модель Мусы</h1>
  <div class="row placeholders">
    <div class="col-xs-12">
      <div id="graph-container">
        <div id="chart"></div>
      </div>
      <div class="spoiler-description">
          <p>mu - Среднее количество ошибок к заданному времени наработки.</p>
          <p>lambda - Интенсивность отказов.</p>
          <p>r - Функция надежности.</p>
      </div>
      <h4>Показатели надежности</h4>
      <span class="text-muted">модели Мусы</span>
      <form action="">
        <p><input type="text" id="link-to-data"></p>
        <p><input type="button" value="Рассчитать" onclick="musa_loader()"></p>
      </form>
    </div>
  </div>
  % include('table.tpl')
  <!-- Musa template -->