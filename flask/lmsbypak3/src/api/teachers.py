from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, TeachAccount, Course, Assignment, db

bp = Blueprint('teachers', __name__, url_prefix='/teachers')

@bp.route('', methods=['GET'])
def index():
    teachers = Teacher.query.all()
    result = []
    for t in teachers:
        result.append(t.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Teacher.query.get_or_404(id)
    return jsonify(t.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'first_name' not in request.json or 'last_name' not in request.json:
        return abort(400)
    
    t = Teacher(
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        teachacct_id=request.json['teachacct_id']

    )

    db.session.add(t)
    db.session.commit()
    return jsonify(t.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Teacher.query.get_or_404(id)
    try:
        db.session.delete(t)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    t = Teacher.query.get_or_404(id)

    if 'first_name' not in request.json and 'last_name' not in request.json:
        return abort(400)
    
    if 'first_name' in request.json:
        t.first_name=request.json['first_name']
    
    if 'last_name' in request.json:
        t.last_name=request.json['last_name']
    
    try:
        db.session.commit()
        return jsonify(t.serialize())
    except:
        return jsonify(False)