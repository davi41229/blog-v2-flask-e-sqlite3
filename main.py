from app import app, db
from app.controllers import default


db.create_all()


if __name__ == "__main__":
    app.run(debug=True,port=1220)