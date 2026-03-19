"""
app.py — Corporación logistica H&R
Sitio web multi-página con Flask.

Uso:
    python app.py
    → http://127.0.0.1:5000
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Rutas ──────────────────────────────────────────

@app.route('/')
def inicio():
    return render_template('inicio.html', active='inicio')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', active='nosotros')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', active='servicios')

@app.route('/productos')
def productos():
    return render_template('productos.html', active='productos')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html', active='galeria')

@app.route('/cotizacion')
def cotizacion():
    return render_template('cotizacion.html', active='cotizacion')

@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html', active='contactanos')



# ── Archivos estáticos ─────────────────────────────

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'static'), filename)

# ── Inicio ─────────────────────────────────────────

if __name__ == '__main__':
    print('=' * 52)
    print('  Corporación logistica H&R — Servidor activo')
    print('  http://127.0.0.1:5000')
    print('  Ctrl+C para salir')
    print('=' * 52)
    app.run(debug=True, host='0.0.0.0', port=5000)