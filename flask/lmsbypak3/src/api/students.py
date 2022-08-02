from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, TeachAccount, Course, Assignment, db

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('', methods=['GET'])
def index():
    students = Student.query.all()
    result = []
    for s in students:
        result.append(s.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    s = Student.query.get_or_404(id)
    return jsonify(s.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'first_name' not in request.json or 'last_name' not in request.json:
        return abort(400)
    
    s = Student(
        first_name=request.json['first_name'],
        last_name=request.json['last_name']
    )

    db.session.add(s)
    db.session.commit()
    return jsonify(s.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    s = Student.query.get_or_404(id)
    try:
        db.session.delete(s)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    s = Student.query.get_or_404(id)

    if 'first_name' not in request.json and 'last_name' not in request.json:
        return abort(400)
    
    if 'first_name' in request.json:
        s.first_name=request.json['first_name']
    
    if 'last_name' in request.json:
        s.last_name=request.json['last_name']
    
    try:
        db.session.commit()
        return jsonify(s.serialize())
    except:
        return jsonify(False)