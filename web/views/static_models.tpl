  <!-- Static-Models template -->
  <h1 class="page-header">Статические модели</h1>
  <div class="row placeholders">
    <div class="col-xs-12">
      <div class="graph-container">
          <div id="halstead-chart"></div>
      </div>
      <h4>Показатели надежности</h4>
      <span class="text-muted">по метрике Халстеда</span>
      <div class="graph-container">
          <div id="ciclomatic-chart"></div>
      </div>
      <h4>Количество методов</h4>
      <span class="text-muted">определенной цикломатической сложности</span>
      <form action="">
        <p><input type="button" value="Рассчитать" onclick="static_models_loader()"></p>
      </form>

    </div>
  </div>
  <!-- Jelinsky-Moranda template -->