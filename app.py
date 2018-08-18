import base64

from flask import render_template, Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:abc123@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()
db.init_app(app)


@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()


class UserInfo(db.Model):
    """
    user info model
    """
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String)
    pic = db.Column(db.LargeBinary)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        _delete_data()

        user_name = request.form.get('user_name', '')
        pic = request.files['pic'].read() if request.files['pic'] else None
        user_info = UserInfo(
            user_name=user_name,
            pic=pic
        )
        db.session.add(user_info)
        db.session.commit()
        return redirect(url_for('.index'))
    user_info = UserInfo.query.first()
    return render_template('index.html',
                           user_name=user_info.user_name if user_info else None,
                           pic=base64.b64encode(user_info.pic).decode('UTF-8') if user_info and user_info.pic else None)


@app.route('/delete', methods=['POST'])
def delete():
    _delete_data()
    return redirect(url_for('.index'))


def _delete_data():
    old_user_info = UserInfo.query.first()
    if old_user_info:
        db.session.delete(old_user_info)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
