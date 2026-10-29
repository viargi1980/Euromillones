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

body {{
    font-family: Arial, sans-serif;
    background: #f3f4f6;
    margin: 0;
    padding: 30px;
}}

.container {{
    max-width: 1100px;
    margin: auto;
}}

.card {{
    background: white;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 2px 12px rgba(0,0,0,.15);
}}

.numero {{
    display:inline-block;
    width:60px;
    height:60px;
    line-height:60px;
    border-radius:50%;
    background:#2563eb;
    color:white;
    font-weight:bold;
    font-size:22px;
    margin:5px;
}}

.estrella {{
    display:inline-block;
    width:60px;
    height:60px;
    line-height:60px;
    border-radius:50%;
    background:#f59e0b;
    color:white;
    font-weight:bold;
    font-size:22px;
    margin:5px;
}}

table {{
    width:100%;
    border-collapse:collapse;
}}

th, td {{
    border:1px solid #ddd;
    padding:10px;
    text-align:center;
}}

th {{
    background:#e5e7eb;
}}

</style>
</head>
<body>

<div class="container">

<div class="card">

<h1>🎲 Predicción Euromillones IA</h1>

<p>
📅 Última generación:
<strong>{prediccion["fecha_generacion"]}</strong>
</p>

<h2>Combinación Recomendada</h2>

<div>
"""

for n in prediccion["numeros"]:
    html += f'<span class="numero">{n}</span>'

html += "</div><br><div>"

for e in prediccion["estrellas"]:
    html += f'<span class="estrella">⭐{e}</span>'

html += """
</div>

<h2>Top 10 números más probables</h2>

<table>
<tr>
<th>Número</th>
<th>Probabilidad</th>
</tr>
"""

for item in prediccion["top_numeros"]:
    html += f"""
<tr>
<td>{item["numero"]}</td>
<td>{item["probabilidad"]:.2%}</td>
</tr>
"""

html += """
</table>

<h2>Top estrellas</h2>

<table>
<tr>
<th>Estrella</th>
<th>Probabilidad</th>
</tr>
"""

for item in prediccion["top_estrellas"]:
    html += f"""
<tr>
<td>{item["estrella"]}</td>
<td>{item["probabilidad"]:.2%}</td>
</tr>
"""

html += """
</table>

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