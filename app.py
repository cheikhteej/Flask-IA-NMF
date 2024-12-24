import os
from flask import Flask #, request, send_from_directory
# from extract import *
# import joblib



app = Flask(__name__,static_folder='templates')


from routes import *
#lancement du microservice flask

if __name__ == '__main__':
    app.run(debug=True)






# # Répertoire de quarantaine
# QUARANTAINE_DIR = 'quarantaine'

# ALLOWED_EXTENSIONS = {'.exe', '.dll'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/malware_test', methods=['POST'])
# def malware_test():
#     if 'file' not in request.files:
#         return 'No file part'
#     file = request.files['file']
    
#     if file.filename == '':
#         return 'Aucun fichier selectionné'
#     if file and allowed_file(file.filename):
#         filename = file.file.filename
#         file.save(os.path.join(QUARANTAINE_DIR, filename))
#         features = extract_malware_features(f"{QUARANTAINE_DIR/filename}")
        
#         model = joblib.load('model.pkl')
#         y_pred = model.predict(features)

#         return  {"y_pred": y_pred}
    
#     return {"message": "Type de fichier invalide"}