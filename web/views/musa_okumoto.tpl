  <!-- Musa-Okumoto template -->
  <h1 class="page-header">Модель Мусы-Oкумото</h1>
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
      <span class="text-muted">модели Мусы-Окумото</span>
      <form action="">
        <p><input type="button" value="Рассчитать" onclick="musa_okumoto_loader()"></p>
      </form>
    </div>
  </div>
  % include('table.tpl')
  <!-- Musa-Okumoto template -->