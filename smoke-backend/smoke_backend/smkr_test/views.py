# -*- coding: utf-8 -*-
"""Creates view for JSON handling.

Attributes:
    blueprint (Flask Blueprint): The blueprint scheme for smoke. [fblueprint]_
"""

from flask import request, jsonify, Blueprint

# from smoke_backend.extensions import pwd_context, jwt  -- shouldnt need this because this shouldnt handle login
import subprocess


blueprint = Blueprint('JSON', __name__, url_prefix='/JSON')


@blueprint.route('/test', methods=['POST'])
def stringifyJSON():

    # request.jsonify() - something like this

    subprocess.call(['./run_smkr.sh']) 
    value = subprocess.check_output(['run_smkr.sh', echo])
    return value

@blueprint.route('/refresh', methods=['POST'])
def refresh():
    subprocess.call(['.run_smkr.sh'])
    value = subprocess.check_output(['run_smkr.sh', echo])
    return value
