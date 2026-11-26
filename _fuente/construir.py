#!/usr/bin/env python3
"""Genera index.html de la página de enlaces de KpG (kpg-contadores.github.io).

Uso:  python3 _fuente/construir.py
La carpeta _fuente no se publica (GitHub Pages ignora las carpetas que empiezan con "_").
Textos aprobados (no cambiar sin pedirlo): frase principal, compromiso, pasos y lema.
"""
import pathlib
from urllib.parse import quote

RAIZ = pathlib.Path(__file__).resolve().parent.parent
WA = "56942652503"
SITIO = "https://kpg-asesorias.github.io/"
UF_RESPALDO = (41439.89, "2026-11-30")  # mismo respaldo que el sitio (assets/kpg.js)


def wa(texto):
    return f"https://wa.me/{WA}?text={quote(texto)}"


def ext(url, evento, clase, contenido, extra=""):
    return f'<a class="{clase}" data-evento="{evento}" href="{url}" target="_blank" rel="noopener"{extra}>{contenido}</a>'


# --- Íconos de línea (trazo 1.8, mismos del sitio) ---------------------------------
def svg(cuerpo, ancho="1.8"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{ancho}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{cuerpo}</svg>')


I = {
    "whatsapp": svg('<path d="M20.5 11.6a8.6 8.6 0 0 1-12.7 7.6L3.5 20.5l1.4-4.1a8.6 8.6 0 1 1 15.6-4.8Z"/>'
                    '<path d="M9 8.6c.2-.4.5-.4.8-.3l.9.7c.2.2.3.5.1.7l-.4.7c.6 1.1 1.4 1.9 2.6 2.5l.6-.5c.2-.2.5-.2.7 0l.9.9c.2.2.2.6 0 .8-.5.5-1.2.7-1.9.5-2.6-.8-4.3-2.4-5.2-4.8-.2-.6 0-1.1.4-1.4l.5-.5Z" fill="currentColor" stroke="none"/>', "1.7"),
    "globo": svg('<circle cx="12" cy="12" r="8.5"/><path d="M3.8 12h16.4M12 3.5c2.1 2.3 3.2 5.1 3.2 8.5s-1.1 6.2-3.2 8.5c-2.1-2.3-3.2-5.1-3.2-8.5S9.9 5.8 12 3.5Z"/>'),
    "flecha": svg('<path d="M5 12h14M13 6l6 6-6 6"/>', "2"),
    "calendario": svg('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M8 3v4M16 3v4M3.5 10h17M8 14h3M8 17h6"/>'),
    "libro": svg('<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5v-15Z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5M8 7.5h8M8 11h6"/>'),
    "personas": svg('<circle cx="9" cy="8" r="3.3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6M18 14.4a5.6 5.6 0 0 1 3 5.6"/>'),
    "renta": svg('<path d="M6 3h9l4 4v14H6z"/><path d="M14.5 3v4.5H19M9 12h7M9 15.5h7M9 19h4"/>'),
    "semilla": svg('<path d="M12 21v-8"/><path d="M12 13c0-4.4 3-7.5 8-7.5 0 4.6-3.2 7.5-8 7.5Z"/><path d="M12 15.5C12 12 9.6 9.5 5 9.5c0 3.7 2.6 6 7 6Z"/>'),
    "grafico": svg('<path d="M4 20h16"/><path d="M7 16v-4M12 16V8M17 16v-7"/><path d="m5 9 5-4 4 3 5-4"/>'),
    "reunion": svg('<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M8 3v4M16 3v4M3.5 10h17"/><path d="m9.5 15 2 2 3.5-4"/>'),
    "precio": svg('<path d="M3.5 12.6V5a1.5 1.5 0 0 1 1.5-1.5h7.6L21 11.9a1.5 1.5 0 0 1 0 2.1l-7 7a1.5 1.5 0 0 1-2.1 0Z"/><circle cx="8" cy="8" r="1.4"/>'),
    "pasos": svg('<path d="M4 6h3M4 12h3M4 18h3"/><path d="M10 6h10M10 12h10M10 18h7"/>'),
    "pregunta": svg('<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.4a2.5 2.5 0 0 1 4.8.9c0 1.7-2.4 2.2-2.4 3.7M12 17.2h.01"/>'),
    "casa": svg('<path d="M4 10.5 12 4l8 6.5V20H4z"/><path d="M9.5 20v-5.5h5V20"/>'),
    "instagram": svg('<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".9" fill="currentColor" stroke="none"/>'),
    "contacto": svg('<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/><path d="M19 4v5M16.5 6.5h5"/>'),
    "visto": svg('<path d="m5 12.5 4.5 4.5L19 7.5"/>', "2"),
}

MSJ_PRINCIPAL = "Hola KpG, vengo de su página. Quiero conversar sobre la contabilidad de mi empresa."

AYUDA = [
    ("contabilidad", "libro", "Contabilidad e impuestos", "F29, libros y balance, al día cada mes.",
     "Hola KpG, quiero consultar por contabilidad e impuestos para mi empresa."),
    ("remuneraciones", "personas", "Remuneraciones", "Liquidaciones, Previred, contratos y finiquitos.",
     "Hola KpG, quiero consultar por remuneraciones para mi empresa."),
    ("renta", "renta", "Operación Renta", "La declaración anual de su empresa y de sus socios.",
     "Hola KpG, quiero consultar por la Operación Renta."),
    ("empresa", "semilla", "Empezar mi empresa", "Tipo de sociedad, inicio de actividades y régimen tributario.",
     "Hola KpG, quiero crear una empresa y necesito asesoría."),
    ("asesoria", "grafico", "Asesoría para decidir", "Flujo de caja, planificación tributaria y reportes.",
     "Hola KpG, quiero consultar por asesoría para tomar decisiones en mi empresa."),
    ("reunion", "reunion", "Agendar una reunión", "Por videollamada o en persona, para conversar su caso con calma.",
     "Hola KpG, quiero agendar una reunión para conversar sobre mi empresa."),
]

CONOZCA = [
    ("planes", "precio", "Planes y precios", "Cinco packs en UF, con IVA incluido.", "planes.html"),
    ("como", "pasos", "Cómo trabajamos", "De la primera conversación al primer mes, todo por escrito.", "como-trabajamos.html"),
    ("consultas", "pregunta", "Consultas frecuentes", "Respuestas claras a las dudas de cada mes.", "consultas.html"),
    ("nosotros", "casa", "Sobre KpG", "Quiénes somos y por qué trabajamos así.", "nosotros.html"),
]

PASOS = [  # texto aprobado
    ("Conversamos", "Nos cuenta cómo funciona su empresa y qué necesita."),
    ("Propuesta por escrito", "Antes de empezar, recibe el detalle de cada cobro, línea por línea."),
    ("Mes a mes", "Su contabilidad al día, al menos una reunión al mes y factura por el servicio."),
]

COMPROMISO = [  # texto aprobado
    "Si su consulta necesita revisión, le decimos cuándo tendrá la respuesta.",
    "Si algo no lo sabemos, se lo decimos y lo averiguamos.",
    "Lo que acordamos en una reunión queda por escrito.",
]


def pesos(n):
    entero, dec = f"{n:,.2f}".split(".")
    return "$" + entero.replace(",", ".") + "," + dec


MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
uf_valor, uf_fecha = UF_RESPALDO
uf_texto = f"al {int(uf_fecha[8:])} de {MESES[int(uf_fecha[5:7]) - 1]}"

ayuda_html = "\n".join(
    f'      <li>{ext(wa(m), ev, "tema", f"""<span class="icono-caja">{I[ic]}</span><span class="tema-texto"><b>{t}</b><span>{d}</span></span><span class="tema-ir">Consultar {I["flecha"]}</span>""")}</li>'
    for ev, ic, t, d, m in AYUDA)

conozca_html = "\n".join(
    f'      <li>{ext(SITIO + url, "sitio-" + ev, "tarjeta-sitio", f"""<span class="icono-caja claro">{I[ic]}</span><b>{t}</b><span>{d}</span><span class="ver">Ver en el sitio {I["flecha"]}</span>""")}</li>'
    for ev, ic, t, d, url in CONOZCA)

pasos_html = "\n".join(f'      <li><span class="num">{i}</span><div><b>{t}</b><span>{d}</span></div></li>' for i, (t, d) in enumerate(PASOS, 1))
compromiso_html = "\n".join(f'      <li>{I["visto"]}<span>{c}</span></li>' for c in COMPROMISO)

CSS = (RAIZ / "_fuente/estilos.css").read_text(encoding="utf-8")
JS = (RAIZ / "_fuente/comportamiento.js").read_text(encoding="utf-8").replace("__UF_VALOR__", str(uf_valor)).replace("__UF_FECHA__", uf_fecha)

html = f"""<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>KpG · Contadores y asesores</title>
<meta name="description" content="Contadores y asesores para empresas. Trato directo, respuestas claras y su contabilidad al día.">
<meta name="theme-color" content="#0E2A47">
<link rel="icon" href="assets/kpg-app-icon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="KPG y Asesores SpA">
<meta property="og:locale" content="es_CL">
<meta property="og:title" content="KpG · Detrás de cada respuesta, un contador">
<meta property="og:description" content="Trato directo, respuestas claras y su contabilidad al día.">
<meta property="og:url" content="https://kpg-contadores.github.io/">
<meta property="og:image" content="https://kpg-contadores.github.io/assets/og-kpg.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="KpG, contadores y asesores: detrás de cada respuesta, un contador.">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fuentes/libre-caslon-text-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fuentes/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>
{CSS}</style>
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>
<div class="marco">

  <header class="lateral">
    <div class="lateral-contenido">
      <div class="identidad">
        <img class="avatar" src="assets/kpg-avatar.svg" width="72" height="72" alt="KpG, Contadores y Asesores">
        <div>
          <p class="nombre">KPG y Asesores SpA</p>
          <p class="usuario">@kpg.asesorias</p>
        </div>
      </div>
      <p class="kicker">Contadores y asesores · a distancia y en terreno</p>
      <h1>Detrás de cada respuesta, <em>un contador.</em></h1>
      <span class="raya-doble" aria-hidden="true"></span>
      <p class="bajada"><strong>Trato directo</strong>, respuestas claras y su contabilidad al día.</p>
      <nav class="acciones" aria-label="Contacto principal">
        {ext(wa(MSJ_PRINCIPAL), "whatsapp", "accion accion-whatsapp", f'<span class="accion-icono">{I["whatsapp"]}</span><span class="accion-texto"><b>Escribir por WhatsApp</b><small>Le respondemos directamente</small></span>{I["flecha"]}')}
        {ext(SITIO, "sitio", "accion accion-sitio", f'<span class="accion-icono">{I["globo"]}</span><span class="accion-texto"><b>Conozca KpG</b><small>Servicios, planes y cómo trabajamos</small></span>{I["flecha"]}')}
      </nav>
      <ul class="sellos" aria-label="Así trabajamos">
        <li>{I["visto"]}Propuesta por escrito</li>
        <li>{I["visto"]}Reunión mensual incluida</li>
        <li>{I["visto"]}Factura por el servicio</li>
      </ul>
    </div>
  </header>

  <main id="contenido" class="contenido">

    <section class="bloque fondo-gris" aria-labelledby="t-mes" data-revelar>
      <p class="kicker oscuro">Para que no se le pase</p>
      <h2 id="t-mes">Su mes tributario</h2>
      <span class="raya-doble" aria-hidden="true"></span>
      <div class="calendario">
        <div class="cal-cab">
          <b>Próximos vencimientos</b>
          <span class="uf">UF <strong data-uf>{pesos(uf_valor)}</strong> <small data-uf-fecha>{uf_texto}</small></span>
        </div>
        <div class="cal-linea" data-venc="f29">
          <div class="fecha"><b data-dia>20</b><small data-mes>c/mes</small></div>
          <div class="cal-texto"><b>F29 · IVA del mes</b><span data-detalle>Vence el día 20 de cada mes</span></div>
          <span class="faltan" data-faltan hidden></span>
        </div>
        <div class="cal-linea" data-venc="previred">
          <div class="fecha"><b data-dia>13</b><small data-mes>c/mes</small></div>
          <div class="cal-texto"><b>Previred · cotizaciones</b><span data-detalle>Vence el día 13 de cada mes</span></div>
          <span class="faltan" data-faltan hidden></span>
        </div>
        <p class="cal-nota">El F29 es la declaración mensual de IVA y vence el 20 si su empresa emite factura electrónica. En Previred se pagan las cotizaciones de sus trabajadores. Si una fecha cae en fin de semana o feriado, se corre al día hábil siguiente.</p>
        {ext(wa("Hola KpG, tengo una consulta sobre los impuestos de este mes."), "duda-mes", "enlace", f'¿Tiene una duda con su F29 o Previred? Escríbanos {I["flecha"]}')}
      </div>
    </section>

    <section class="bloque" aria-labelledby="t-ayuda" data-revelar>
      <p class="kicker oscuro">Su consulta, directo a WhatsApp</p>
      <h2 id="t-ayuda">¿En qué le ayudamos?</h2>
      <span class="raya-doble" aria-hidden="true"></span>
      <p class="intro">Elija un tema y se abre WhatsApp con su consulta lista para enviar.</p>
      <ul class="temas">
{ayuda_html}
      </ul>
    </section>

    <section class="bloque fondo-azul" aria-labelledby="t-conozca" data-revelar>
      <p class="kicker">Nuestro sitio</p>
      <h2 id="t-conozca">Conozca KpG antes de escribirnos</h2>
      <span class="raya-doble" aria-hidden="true"></span>
      <p class="intro">Los servicios, los planes y la forma en que trabajamos, explicados con calma.</p>
      <ul class="sitio-grilla">
{conozca_html}
      </ul>
      {ext(SITIO, "sitio-boton", "boton-sitio", f'Ir al sitio de KpG {I["flecha"]}')}
    </section>

    <section class="bloque" aria-labelledby="t-como" data-revelar>
      <p class="kicker oscuro">Paso a paso</p>
      <h2 id="t-como">Cómo trabajamos</h2>
      <span class="raya-doble" aria-hidden="true"></span>
      <ol class="pasos">
{pasos_html}
      </ol>
    </section>

    <section class="bloque fondo-gris" aria-labelledby="t-compromiso" data-revelar>
      <div class="compromiso">
        <span class="raya-doble clara" aria-hidden="true"></span>
        <h2 id="t-compromiso">Nuestro compromiso</h2>
        <ul>
{compromiso_html}
        </ul>
        <p class="firma">KpG · Contadores y Asesores</p>
      </div>
    </section>

    <section class="bloque lema" aria-label="Lema de KpG" data-revelar>
      <p class="antes">Soñar es fácil. Empezar, no.</p>
      <p class="frase">Ni más, ni menos:<br> lo justo.</p>
      <span class="raya-doble" aria-hidden="true"></span>
      {ext(wa(MSJ_PRINCIPAL), "whatsapp-final", "accion accion-whatsapp compacta", f'<span class="accion-icono">{I["whatsapp"]}</span><span class="accion-texto"><b>Conversemos su caso</b><small>Escríbanos por WhatsApp</small></span>{I["flecha"]}')}
    </section>

    <footer class="pie">
      <div class="pie-enlaces">
        <a class="pie-boton destacado" data-evento="contacto" href="assets/kpg.vcf" download="KpG Contadores y Asesores.vcf">{I["contacto"]}Guardar contacto</a>
        {ext(SITIO, "sitio-pie", "pie-boton", I["globo"] + "Sitio web")}
        {ext("https://www.instagram.com/kpg.asesorias/", "instagram", "pie-boton", I["instagram"] + "Instagram")}
      </div>
      <img class="pie-logo" src="assets/kpg-logo-horizontal.svg" width="150" height="56" alt="KpG, Contadores y Asesores">
      <p class="legal">KPG y Asesores SpA · RUT 78.366.703-7<br>Contabilidad, impuestos y remuneraciones para empresas.</p>
    </footer>
  </main>
</div>

{ext(wa(MSJ_PRINCIPAL), "whatsapp-barra", "barra-whatsapp", I["whatsapp"] + "<span>Escribir por WhatsApp</span>", ' aria-hidden="true" tabindex="-1"')}

<script>
{JS}</script>
</body>
</html>
"""
(RAIZ / "index.html").write_text(html, encoding="utf-8")
print("index.html generado")
