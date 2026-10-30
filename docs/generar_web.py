from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

with open(
    BASE_DIR / "prediccion.json",
    "r",
    encoding="utf-8"
) as f:
    prediccion = json.load(f)

html = f"""
<!DOCTYPE html>
<html lang="es">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Euromillones IA</title>

<style>

:root {{
    --bg1:#0f172a;
    --bg2:#1e293b;
    --card:#ffffff;
    --primary:#2563eb;
    --secondary:#4f46e5;
    --star:#f59e0b;
    --text:#111827;
    --muted:#6b7280;
}}

* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body {{
    font-family: "Segoe UI", Arial, sans-serif;
    background: linear-gradient(135deg, var(--bg1), var(--bg2));
    min-height: 100vh;
    padding: 30px;
}}

.container {{
    max-width: 1200px;
    margin: auto;
}}

.header {{
    text-align:center;
    color:white;
    margin-bottom:30px;
}}

.header h1 {{
    font-size:48px;
    margin-bottom:10px;
}}

.header p {{
    color:#cbd5e1;
    font-size:18px;
}}

.card {{
    background:white;
    border-radius:24px;
    padding:35px;
    box-shadow:0 20px 50px rgba(0,0,0,.25);
}}

.info-grid {{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-bottom:35px;
}}

.info-box {{
    background:#f8fafc;
    border-left:5px solid var(--primary);
    padding:20px;
    border-radius:15px;
}}

.info-title {{
    color:var(--muted);
    font-size:14px;
    margin-bottom:5px;
}}

.info-value {{
    font-size:24px;
    font-weight:bold;
    color:var(--text);
}}

.section {{
    margin-bottom:40px;
}}

.section-title {{
    font-size:28px;
    margin-bottom:20px;
    color:var(--text);
}}

.numbers {{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:12px;
}}

.numero {{
    width:80px;
    height:80px;
    border-radius:50%;
    background:linear-gradient(
        135deg,
        var(--primary),
        var(--secondary)
    );
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:28px;
    font-weight:bold;
    box-shadow:0 8px 20px rgba(37,99,235,.35);
}}

.estrellas {{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:12px;
    margin-top:15px;
}}

.estrella {{
    width:80px;
    height:80px;
    border-radius:50%;
    background:linear-gradient(
        135deg,
        #f59e0b,
        #f97316
    );
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    font-weight:bold;
    box-shadow:0 8px 20px rgba(245,158,11,.35);
}}

table {{
    width:100%;
    border-collapse:collapse;
    overflow:hidden;
    border-radius:15px;
}}

thead {{
    background:linear-gradient(
        90deg,
        var(--primary),
        var(--secondary)
    );
    color:white;
}}

th {{
    padding:15px;
    text-align:center;
}}

td {{
    padding:14px;
    text-align:center;
    border-bottom:1px solid #e5e7eb;
}}

tbody tr:hover {{
    background:#f8fafc;
}}

.footer {{
    text-align:center;
    margin-top:30px;
    color:var(--muted);
    font-size:14px;
}}

@media (max-width:768px) {{

    .header h1 {{
        font-size:36px;
    }}

    .numero,
    .estrella {{
        width:65px;
        height:65px;
        font-size:22px;
    }}

}}

</style>

</head>

<body>

<div class="container">

<div class="header">
    <h1>🎯 Euromillones IA</h1>
    <p>Predicción basada en análisis estadístico e inteligencia artificial</p>
</div>

<div class="card">

<div class="info-grid">

<div class="info-box">
<div class="info-title">Generación</div>
<div class="info-value">{prediccion["fecha_generacion"]}</div>
</div>

<div class="info-box">
<div class="info-title">Números posibles</div>
<div class="info-value">50</div>
</div>

<div class="info-box">
<div class="info-title">Estrellas posibles</div>
<div class="info-value">12</div>
</div>

</div>

<div class="section">

<h2 class="section-title">
🏆 Combinación Recomendada
</h2>

<div class="numbers">
"""

for n in prediccion["numeros"]:
    html += f"""
<div class="numero">{n}</div>
"""

html += """
</div>

<div class="estrellas">
"""

for e in prediccion["estrellas"]:
    html += f"""
<div class="estrella">⭐ {e}</div>
"""

html += """
</div>

</div>

<div class="section">

<h2 class="section-title">
📈 Top 10 números más probables
</h2>

<table>

<thead>
<tr>
<th>Número</th>
<th>Probabilidad</th>
</tr>
</thead>

<tbody>
"""

for item in prediccion["top_numeros"]:
    html += f"""
<tr>
<td><strong>{item["numero"]}</strong></td>
<td>{item["probabilidad"]:.2%}</td>
</tr>
"""

html += """
</tbody>

</table>

</div>

<div class="section">

<h2 class="section-title">
⭐ Top estrellas
</h2>

<table>

<thead>
<tr>
<th>Estrella</th>
<th>Probabilidad</th>
</tr>
</thead>

<tbody>
"""

for item in prediccion["top_estrellas"]:
    html += f"""
<tr>
<td><strong>{item["estrella"]}</strong></td>
<td>{item["probabilidad"]:.2%}</td>
</tr>
"""

html += """
</tbody>

</table>

</div>

<div class="footer">
Generado automáticamente por Euromillones IA
</div>

</div>

</div>

</body>
</html>
"""

with open(
    BASE_DIR / "index.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("✅ index.html generado")