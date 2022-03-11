from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from ..models import Pitch
from .. import db
import json
views = Blueprint('views', __name__)
from .forms import PitchForm,CommentForm

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    pitchform = PitchForm()
    if request.method == 'POST':
        pitch = pitchform.content.data
        
        category = pitchform.category.data
        if len(pitch) < 1:
            flash('Pitch is too short!', category='error')
        else:
            new_pitch = Pitch(data=pitch, user_id=current_user.id,category=category)
            db.session.add(new_pitch)
            db.session.commit()
            flash('Comment added!', category='success')
            if category =='friendship':
                return redirect(url_for('views.friendship'))
            elif category=='Inspirational':
                return redirect(url_for('views.inspiration'))
            else:
                return redirect(url_for('views.discussion'))
  
    print(Pitch.query.all())
    return render_template("home.html", user=current_user,pitchform=pitchform)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Pitch.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/inspiration')
def inspiration():
    inspirational =Pitch.query.filter_by(category= 'Inspirational').all()
    print(inspirational)
    return render_template('inspiration.html', user=current_user,inspirational = inspirational)
    
@views.route('/friendship')
def friendship():
    friendships = Pitch.query.filter_by(category ='friendship').all()
    print(friendship)
    return render_template('friendship.html', user=current_user,friendship=friendships)


@views.route('/discussion')
def discussion():
    discussions =Pitch.query.filter_by(category ='discussion').all()
    return render_template('discussion.html', user=current_user,discussions=discussions)
    
