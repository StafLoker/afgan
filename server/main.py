from flask import Flask, jsonify, send_file, send_from_directory
import tensorflow as tf
import numpy as np
from io import BytesIO
from PIL import Image
import base64
import os
import logging
import signal
import sys
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

generator = None
LATENT_DIM = 100
PORT = int(os.getenv('PORT', 38880))

def signal_handler(sig, frame):
    logger.info('Shutting down server...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def load_generator():
    global generator
    logger.info('Loading generator model...')
    generator = tf.keras.models.load_model('model/afgan-generator.keras')
    logger.info('Generator loaded successfully')

def generate_image():
    noise = tf.random.normal([1, LATENT_DIM])
    generated = generator(noise, training=False)
    img_array = (generated[0].numpy() + 1) / 2.0
    img_array = (img_array * 255).astype(np.uint8)
    return Image.fromarray(img_array)

@app.route('/')
def index():
    return send_file('web/index.html')

@app.route('/logo.png')
def logo():
    return send_file('web/logo.png', mimetype='image/png')

@app.route('/favicon.ico')
def favicon():
    return send_file('web/favicon.ico', mimetype='image/x-icon')

@app.route('/generate')
def generate():
    logger.info('Generating new image')
    img = generate_image()
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    logger.info('Image generated successfully')
    return jsonify({'image': img_base64})

if __name__ == '__main__':
    logger.info('Starting AFGAN server')
    load_generator()
    logger.info(f'Server running on port {PORT}')
    app.run(host='0.0.0.0', port=PORT)