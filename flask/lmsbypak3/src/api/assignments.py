from flask import Blueprint, jsonify, abort, request
from ..models import Teacher, Student, TeachAccount, Course, Assignment, db

bp = Blueprint('assignments', __name__, url_prefix='/assignments')

@bp.route('', methods=['GET'])
def index():
    assignments = Assignment.query.all()
    result =[]
    for a in assignments:
        result.append(a.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Assignment.query.get_or_404(id)
    return jsonify(a.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'title' not in request.json or 'course_id' not in request.json:
        return abort(400)
    
    a = Assignment(
        title=request.json['title'],
        course_id=request.json['course_id'],
        max_grade= request.json['max_grade']
    )

    db.session.add(a)
    db.session.commit()
    return jsonify(a.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a = Assignment.query.get_or_404(id)
    try:
        db.session.delete(a)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id: int):
    a = Assignment.query.get_or_404(id)

    #period, subject, teacher_id
    if 'title' not in request.json and 'course_id' not in request.json:
        return abort(400)
    
    if 'title' in request.json:
        a.title=request.json['title']
    
    if 'course_id' in request.json:
        a.course_id=request.json['course_id']
    
    if 'max_grade' in request.json:
        a.max_grade = request.json['max_grade']
    
    try:
        db.session.commit()
        return jsonify(a.serialize())
    except:
        return jsonify(False)