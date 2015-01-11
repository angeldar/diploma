  <!-- Static-Models template -->
  <h1 class="page-header">Статические модели</h1>
  <div class="row placeholders">
    <div class="col-xs-12">
      <div class="graph-container">
          <div id="halstead-chart"></div>
      </div>
      <div class="spoiler-description">
        <p>length - длина программы.</p>
        <p>volume - объем программы.</p>
        <p>difficulty - Сложность программы.</p>
        <p>bugs - Количество внесенных ошибок.</p>
        <!--<p>Effort - усилия на разработку - не репрезантативно</p>-->
        <!--<p>Time - время на разработку - не репрезентативнос</p>-->
      </div>
      <h4>Показатели надежности</h4>
      <span class="text-muted">по метрике Халстеда</span>
      <div class="graph-container">
          <div id="ciclomatic-chart"></div>
      </div>
      <div class="spoiler-description">
        <p>A - методы низкой сложности, простые. (1-5).</p>
        <p>B - методы низкой сложности, простые, структурированные(6-10).</p>
        <p>C - методы умеренной сложности. (11-20).</p>
        <p>D - методы повышенной сложности (21-30).</p>
        <p>E - опасные методы (31-40).</p>
        <p>F - очень опасные методы (41+).</p>
      </div>
      <h4>Количество методов</h4>
      <span class="text-muted">определенной цикломатической сложности</span>
      <form action="">
        <p><input type="text" id="link-to-git-repo"></p>
        <p><input type="button" value="Рассчитать" onclick="static_models_loader()"></p>
      </form>
    </div>
  </div>
  <!-- Jelinsky-Moranda template -->


