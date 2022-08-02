from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, TeachAccount, Course, Assignment, db
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('teachaccts', __name__, url_prefix='/teachaccts')

@bp.route('', methods=['GET'])
def index():
    teachaccts = TeachAccount.query.all()
    result = []
    for ta in teachaccts:
        result.append(ta.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    ta = TeachAccount.query.get_or_404(id)
    return jsonify(ta.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    
    #teacher with a teacher_id must exist
    Teacher.query.get_or_404(request.json['teacher_id'])
    
    ta = TeachAccount(
        username=request.json['username'],
        password=scramble(request.json['password']),
        teacher_id=request.json['teacher_id']

    )

    db.session.add(ta)
    db.session.commit()
    return jsonify(ta.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    ta = TeachAccount.query.get_or_404(id)
    try:
        db.session.delete(ta)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    ta = TeachAccount.query.get_or_404(id)

    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)
    
    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        else:
            ta.username=request.json['username']
    
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        else:
            ta.password=scramble(request.json['password'])
    
    try:
        db.session.commit()
        return jsonify(ta.serialize())
    except:
        return jsonify(False)