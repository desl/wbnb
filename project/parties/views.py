from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.parties.models import Party
from project.parties.forms import PartyForm, JoinForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps
from IPython import embed
import json

parties_blueprint = Blueprint(
  'parties',
  __name__,
  template_folder='templates'
)

@parties_blueprint.route('/', methods=["GET",'POST'])
@login_required
def index():
    if request.method in ['POST',b'POST']:
        form = PartyForm()
        if form.validate():
            party = Party(
                    form.description.data,
                    current_user.id,
                    form.cost.data,
                    form.date.data,
                    form.time.data)
            if form.instructions.data:
                party.instructions = form.instructions.data
            db.session.add(party)
            db.session.commit()
            return redirect(url_for('parties.index'))
        else:
            return render_template('parties/new.html',form=form)
    parties = Party.query.all()
    # parties = User.query.filter(Party.username.like("%%%s%%" % search)).all()
    return render_template('parties/index.html', parties=parties )

@parties_blueprint.route('/new', methods=['GET'])
@login_required
def new():
    form = PartyForm()
    return render_template('parties/new.html', form=form)

@parties_blueprint.route('/<int:party_id>', methods=['GET','PATCH','DELETE'])
@login_required
def show(party_id):
    party = Party.query.get(party_id)
    if current_user.id != party.host_id and request.method in [b'PATCH','PATCH', b'DELETE','DELETE']:
        flash({ 'text': "Action not authorized!", 'status': 'danger'})
        return redirect(url_for('parties.index'))
    if request.method in ['PATCH',b'PATCH']:
        form = PartyForm(request.form)
        if form.validate():
            party.description = form.description.data
            party.instructions = form.instructions.data
            party.date = form.date.data
            party.time = form.time.data
            party.cost = form.cost.data
            db.session.add(party)
            db.session.commit()
            return redirect(url_for('parties.show',party_id=party_id))
    if request.method in ['DELETE',b'DELETE']:
        form = JoinForm(request.form)
        if form.validate():
            db.session.delete(party)
            db.session.commit()
            return redirect(url_for('root'))
    return render_template('parties/show.html',party=party,party_id=party_id)

@parties_blueprint.route('/<int:party_id>/edit', methods=['GET'])
@login_required
def edit(party_id):
    party = Party.query.get(party_id)
    if party.host_id == current_user.id:
        return render_template('parties/edit.html', form=PartyForm(obj=party), party_id=party_id)
    else:
        flash({ 'text': "Permission denied!", 'status': 'danger'})
        return redirect(url_for('root'))

@parties_blueprint.route('/join/<int:party_id>', methods=['POST'])
@login_required
def join(party_id):
    joinform = JoinForm(request.form)
    if joinform.validate():
        party = Party.query.get(party_id)
        if joinform.verb.data == 'join':
            party.attendee_id = current_user.id
            flash({ 'text': "Success! Laundry ahoy!", 'status': 'success'})
        else:
            if joinform.verb.data == 'leave' and party.attendee_id == current_user.id:
                party.attendee_id = None
                flash({ 'text': "Successfully abandoned your wearbnb", 'status': 'warning'})
            else:
                flash({ 'text': "Invalid request.", 'status': 'danger'})
        db.session.add(party)
        db.session.commit()
        return redirect('/')




