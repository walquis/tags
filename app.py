from tag import Tag  # After app_init(), which sets db for the model
from flask import request, redirect, render_template, g
from IPython import embed
from datetime import datetime
from config import load_config, app_init
import sys
from os.path import join
sys.path.insert(1, sys.path[0])

app = app_init(__name__)


cfg = load_config(join(app.root_path, '../shared/config.yml'))


@app.route('/', methods=['GET'])
def show_tags():
    # Flask.g: a way to pass var to a template
    g.setdefault('image', cfg['awesome_image'])
    #embed()
    # Note tags=Tag.all() ... another way to pass var to a Jinja2 template
    return render_template('index.html', tags=Tag.all())


@app.route('/tags', methods=['POST'])
def add_tag():
    new_tag = request.form['tag-name']
    tag = Tag.where('tag', new_tag).first()
    if tag is None:
        tag = Tag.create(name=new_tag)

    return redirect('/')
