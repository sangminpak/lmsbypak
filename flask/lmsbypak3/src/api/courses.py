from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, TeachAccount, Course, Assignment, db

bp = Blueprint('courses', __name__, url_prefix='/courses')

@bp.route('', methods=['GET'])
def index():
    courses = Course.query.all()
    result = []
    for c in courses:
        result.append(c.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Course.query.get_or_404(id)
    return jsonify(c.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'period' not in request.json or 'subject' not in request.json:
        return abort(400)
    
    c = Course(
        period=request.json['period'],
        subject=request.json['subject'],
        teacher_id = request.json['teacher_id']
    )

    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    c = Course.query.get_or_404(id)
    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    c = Course.query.get_or_404(id)

    #period, subject, teacher_id
    if 'subject' not in request.json and 'period' not in request.json and 'teacher_id' not in request.json:
        return abort(400)
    
    if 'subject' in request.json:
        c.subject=request.json['subject']
    
    if 'period' in request.json:
        c.period=request.json['period']
    
    if 'teacher_id' in request.json:
        c.teacher_id = request.json['teacher_id']
    
    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)