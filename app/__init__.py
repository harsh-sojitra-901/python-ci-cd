from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return jsonify({
            "message": "Hello from Flask CI/CD demo!",
            "status": "ok",
        })

    @app.get("/health")
    def health_check():
        return jsonify({"status": "healthy"}), 200

    @app.get("/api/version")
    def version():
        return jsonify({
            "app": "flask-ci-cd-demo",
            "version": "1.0.0"
        })

    return app
