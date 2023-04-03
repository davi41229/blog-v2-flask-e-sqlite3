from app import app, db
from app.controllers import default
import os


db.create_all()


if __name__ == "__main__":
    port = int(os.getenv("PORT"), "5000")
    app.run(host="0.0.0.0", port=port)
