import firebase_admin
from firebase_admin import credentials, firestore

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials)

db = firestore.client()

def get_users():
  return db.collection('users').get()

def get_user(user_id):
  return db.collection('users').document(user_id).get()

def user_put(user_data):
  user_ref = db.collection('users').document(user_data.username)
  user_ref.set({ 'password': user_data.password })

def get_todos(user_id):
  return db.collection('users').document(user_id).collection('todos').get()

def todo_put(user_id, description):
  todo_ref = db.collection('users').document(user_id).collection('todos')
  todo_ref.add({ 'description': description, 'done': False })

def delete_todo(user_id, todo_id):
  # ref = db.collection('users').document(user_id).collection('todos').document(todo_id)
  todo_ref = _get_todo_ref(user_id, todo_id)
  todo_ref.delete()

def update_todo(user_id, todo_id, done):
  todo_done = not bool(done)
  todo_ref = _get_todo_ref(user_id, todo_id)
  todo_ref.update({ 'done': todo_done })

def _get_todo_ref(user_id, todo_id):
  return db.document(f'users/{user_id}/todos/{todo_id}')