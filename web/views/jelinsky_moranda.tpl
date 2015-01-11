  <!-- Jelinsky-Moranda template -->
  <h1 class="page-header">Модель Джелински-Моранды</h1>
  <div class="row placeholders">
    <div class="col-xs-12">
      <div id="graph-container">
          <div id="time-chart"></div>
          <div class="spoiler-description">
            <p>y_n - Среднее количество ошибок к заданному времени наработки.</p>
          </div>

        <div id="error-chart"></div>
        <div class="spoiler-description">
          <!--<p>y_r - Функция надежности // Не репрезентативна</p>-->
          <p>y_lambda - Интенсивность возникновения отказов после возникновения i-1 отказа.</p>
          <p>y_mttf - Среднее время работы между отказами.</p>
        </div>
      </div>
      <h4>Показатели надежности</h4>
      <span class="text-muted">модели Джелински-Моранды</span>
      <form action="">
        <p><input type="button" value="Рассчитать" onclick="jelinsky_moranda_loader()"></p>
      </form>

    </div>
  </div>

  % include('table.tpl')
  <!-- Jelinsky-Moranda template -->