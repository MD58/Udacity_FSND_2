# /* ------------------------------------------------------- Imports ------------------------------------------------------- */

import os

from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

# /* --------------------------------------------------- Application Start ------------------------------------------------- */

ERROR_STATUS_CODE = 0
QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app)  

  @app.after_request
  def after_request(response):      
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response

# /* ------------------------------------------------------ Endpoints ------------------------------------------------------ */  
  
  @app.route('/api/categories', methods=['GET'])
  def get_categories():
    categories = get_formatted_categories()
    total_categories = len(categories)

    if total_categories == 0:
      abort(404)

    return jsonify({
      'success': True,
      'categories': categories,
      'total_categories': total_categories,
      })    



  @app.route('/api/questions', methods=['GET'])  
  def get_questions():
    page = request.args.get('page', 1, type=int)
    categoryId = request.args.get('categoryId', 0, type=int)
    category = Category.query.filter(Category.id == categoryId).first()
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
        
    if category:
      categoryName = category.format()["type"]    
      questions = Question.query.filter(Question.category == str(categoryId)).order_by(Question.id).all()
    else:
      categoryName = "all"   
      questions = Question.query.order_by(Question.id).all()   

    formatted_result = [question.format() for question in questions]  
    
    return jsonify({
      'success': True,
      'questions': formatted_result[start:end],
      'total_questions': len(formatted_result),
      'categories': get_formatted_categories(), 
      'current_category': categoryName.title(),    
      })  



  @app.route('/api/questions', methods=['POST'])
  def create_search_question():
    body = request.get_json()

    question_text = body.get('question', None)
    answer = body.get('answer', None)
    category = body.get('category', None)
    difficulty = body.get('difficulty', None)
    searchTerm = body.get('searchTerm', None)

    if searchTerm:
      questions = Question.query.filter(Question.question.ilike('%' + searchTerm + '%')).all()        
      formatted_result = [question.format() for question in questions]
      
      if len(formatted_result) > 0:
        return jsonify({
          'success': True,
          'searchTerm' : searchTerm,
          'questions': formatted_result,
          'total_questions': len(formatted_result)
        })
        
      else:
        return jsonify({
          'success': True,
          'searchTerm' : searchTerm,
          'questions': [],
          'total_questions': 0
        })
    
    elif question_text is None or answer is None or category is None or difficulty is None:
      abort(400)
    
    else:     
      question = Question(question=question_text, answer=answer, category=category, difficulty=difficulty)

      question.insert()
    
      return jsonify({
        'success': True,
        'created': question.id
      })


  @app.route('/api/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):   
    question = Question.query.filter(Question.id == question_id).first()

    if question:
      question.delete()        
    else:
      abort(404)

    return jsonify({
      'success': True,
      'deleted': question_id
    })



  @app.route('/api/categories/<int:category_id>/questions', methods=['GET'])  
  def get_questions_by_category(category_id):
    category = Category.query.filter(Category.id == category_id).first()
       
    categoryName = category.format()["type"]    
    questions = Question.query.filter(Question.category == str(category_id)).order_by(Question.id).all()

    formatted_result = [question.format() for question in questions]  
    
    return jsonify({
      'success': True,
      'questions': formatted_result,
      'total_questions': len(formatted_result),      
      'current_category': categoryName.title(),    
      })  



  @app.route('/api/quizzes', methods=['POST'])
  def quizzes():
    body = request.get_json()

    previous_questions = body.get('previous_questions', [None])
    category_id = body.get('quiz_category', None)
    
    if category_id and int(category_id) > 0:
      questions = Question.query.filter(Question.category == str(category_id)).order_by(Question.id).all()        
    else:        
      questions = Question.query.order_by(Question.id).all()        

    all_questions = [question.format() for question in questions]

    for question in all_questions[:]:
      if(question["id"] in previous_questions):
        all_questions.remove(question)
                
    if len(all_questions) > 0:
      selected_question = random.choice(all_questions)
    else: 
      selected_question = None

    return jsonify({
      'success': True,
      'question' : selected_question
    })

# /* ------------------------------------------------------- Helpers ------------------------------------------------------- */ 

  def get_formatted_categories():
    categories = Category.query.order_by(Category.id).all()
    return {category.id : category.type for category in categories}

# /* ---------------------------------------------------- Error Handler ---------------------------------------------------- */  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'bad request',
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'resource not found',
    }), 404

  @app.errorhandler(405)
  def not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'method not allowed',
    }), 405

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'unprocessable',
    }), 422

  # /* ---------------------------------------------------- Application End ---------------------------------------------------- */  

  return app