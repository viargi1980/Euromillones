from pathlib import Path

prediccion = {
    "fecha_generacion": "29/10/2026 17:09:58",
    "numeros": [3, 6, 11, 14, 45],
    "estrellas": [1, 7],
    "top_numeros": [
        {"numero": 3, "probabilidad": 0.5267},
        {"numero": 11, "probabilidad": 0.5067},
        {"numero": 14, "probabilidad": 0.4900},
        {"numero": 6, "probabilidad": 0.4800},
        {"numero": 45, "probabilidad": 0.4800},
        {"numero": 17, "probabilidad": 0.4667},
        {"numero": 49, "probabilidad": 0.4600},
        {"numero": 7, "probabilidad": 0.4500},
        {"numero": 28, "probabilidad": 0.4467},
        {"numero": 32, "probabilidad": 0.4467}
    ],
    "top_estrellas": [
        {"estrella": 7, "probabilidad": 0.5233},
        {"estrella": 1, "probabilidad": 0.4867},
        {"estrella": 3, "probabilidad": 0.4767},
        {"estrella": 9, "probabilidad": 0.4700},
        {"estrella": 4, "probabilidad": 0.4500}
    ]
}

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

h1, h2 {{
    text-align: center;
}}

.fecha {{
    text-align:center;
    color:#666;
    margin-bottom:25px;
}}

.numeros {{
    text-align:center;
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

.grid {{
    display:grid;
    grid-template-columns: 1fr 1fr;
    gap:20px;
    margin-top:20px;
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

@media (max-width: 768px) {{
    .grid {{
        grid-template-columns: 1fr;
    }}
}}

</style>

</head>

<body>

<div class="container">

<div class="card">

<h1>🎲 Predicción Euromillones IA</h1>

<div class="fecha">
📅 Última generación:
<strong>{prediccion["fecha_generacion"]}</strong>
</div>

<h2>Combinación Recomendada</h2>

<div class="numeros">
"""

for n in prediccion["numeros"]:
    html += f'<span class="numero">{n}</span>'

html += "</div><br><div class='numeros'>"

for e in prediccion["estrellas"]:
    html += f'<span class="estrella">⭐{e}</span>'

html += """
</div>

<div class="grid">

<div>

<h2>Top 10 números</h2>

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

</div>

<div>

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

</div>

</div>

</body>
</html>
"""

with open(
    "index.html",
    "w",
    encoding="utf-8"
) as f:
    f.write(html)

print("✅ index.html generado")