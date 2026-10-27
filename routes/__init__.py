
from routes.auth_routes import auth_bp
from routes.student_routes import student_bp
from routes.prediction_routes import prediction_bp
from routes.alert_routes import alert_bp
from routes.statistics_routes import statistics_bp
from routes.faculty_routes import faculty_bp
from routes.google_classroom_routes import classroom_bp
from .dataset_routes import dataset_bp
from .intervention_routes import intervention_bp

__all__ = [
    'auth_bp',
    'student_bp',
    'prediction_bp',
    'alert_bp',
    'statistics_bp',
    'faculty_bp',
    'classroom_bp',
    'dataset_bp',
    'intervention_bp'
]

