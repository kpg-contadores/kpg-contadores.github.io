/* KpG · página de enlaces. Todo el contenido se ve igual sin JavaScript. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
  var CORTOS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];
  var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  var UF_RESPALDO = { valor: __UF_VALOR__, fecha: "__UF_FECHA__" };
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function pesos(n) { return "$" + n.toLocaleString("es-CL", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }

  /* Aparición suave al bajar */
  var revelar = $$("[data-revelar]");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("visible"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    revelar.forEach(function (el) { io.observe(el); });
  } else { revelar.forEach(function (el) { el.classList.add("visible"); }); }

  /* Barra de WhatsApp en celular: aparece cuando los botones de arriba ya no se ven */
  var barra = $(".barra-whatsapp"), acciones = $(".acciones"), pie = $(".pie");
  if (barra && acciones && "IntersectionObserver" in window) {
    var arribaVisible = true, pieVisible = false;
    var pintar = function () {
      var v = !arribaVisible && !pieVisible;
      barra.classList.toggle("visible", v);
      barra.setAttribute("tabindex", v ? "0" : "-1");
      barra.setAttribute("aria-hidden", v ? "false" : "true");
    };
    new IntersectionObserver(function (es) { arribaVisible = es[0].isIntersecting; pintar(); }).observe(acciones);
    if (pie) new IntersectionObserver(function (es) { pieVisible = es[0].isIntersecting; pintar(); }).observe(pie);
  }

  /* UF del día (si la fuente pública responde; si no, queda el último valor conocido) */
  function pintarUF(valor, fecha, enVivo) {
    var f = new Date(fecha + (fecha.length === 10 ? "T12:00:00" : ""));
    $$("[data-uf]").forEach(function (el) { el.textContent = pesos(valor); });
    $$("[data-uf-fecha]").forEach(function (el) { el.textContent = enVivo ? "hoy" : "al " + f.getDate() + " de " + MESES[f.getMonth()]; });
  }
  pintarUF(UF_RESPALDO.valor, UF_RESPALDO.fecha, false);
  if (window.fetch) {
    var control = window.AbortController ? new AbortController() : null;
    var reloj = setTimeout(function () { if (control) control.abort(); }, 5000);
    fetch("https://mindicador.cl/api", control ? { signal: control.signal } : {})
      .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) { clearTimeout(reloj); if (d && d.uf && d.uf.valor) pintarUF(d.uf.valor, String(d.uf.fecha).slice(0, 10), true); })
      .catch(function () { clearTimeout(reloj); });
  }

  /* Próximos vencimientos: F29 el 20 y Previred el 13; si cae en fin de semana pasa al lunes (feriados no incluidos) */
  function proximo(dia) {
    var hoy = new Date(); hoy.setHours(0, 0, 0, 0);
    var calc = function (m, a) { var d = new Date(a, m, dia); while (d.getDay() === 0 || d.getDay() === 6) d.setDate(d.getDate() + 1); return d; };
    var v = calc(hoy.getMonth(), hoy.getFullYear());
    if (v < hoy) v = calc(hoy.getMonth() + 1, hoy.getFullYear());
    var periodo = new Date(v.getFullYear(), v.getMonth() - 1, 1);
    return { fecha: v, faltan: Math.round((v - hoy) / 86400000), periodo: MESES[periodo.getMonth()] };
  }
  [["f29", 20], ["previred", 13]].forEach(function (par) {
    var caja = $("[data-venc='" + par[0] + "']");
    if (!caja) return;
    var p = proximo(par[1]);
    $("[data-dia]", caja).textContent = p.fecha.getDate();
    $("[data-mes]", caja).textContent = CORTOS[p.fecha.getMonth()];
    $("[data-detalle]", caja).textContent = (par[0] === "f29" ? "Declaración de " : "Cotizaciones de ") + p.periodo + " · " + DIAS[p.fecha.getDay()] + " " + p.fecha.getDate() + " de " + MESES[p.fecha.getMonth()];
    var f = $("[data-faltan]", caja);
    f.textContent = p.faltan === 0 ? "Vence hoy" : p.faltan === 1 ? "Vence mañana" : "Faltan " + p.faltan + " días";
    f.classList.toggle("urgente", p.faltan <= 5);
    f.hidden = false;
  });
})();
