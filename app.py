    
import pandas as pd
from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app=Flask(__name__)

# Cargar el conjunto de datos (ajusta el nombre del archivo o la ruta según tu caso)
df = pd.read_csv('artifacts/train.csv')

# Obtener valores únicos de las categorías
cut = df['cut'].unique()
color = df['color'].unique()
clarity = df['clarity'].unique()


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/predictdata",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template('form.html',
                               cut=cut,
                               color=color,
                               clarity=clarity)
    
    else:
        data=CustomData(
            
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        # this is my final data
        final_data=data.get_data_as_dataframe()
        
        predict_pipeline=PredictPipeline()
        
        pred=predict_pipeline.predict(final_data)
        
        result=round(pred[0],2)
        
        return render_template('form.html',
                               results=result,
                               cut=cut,
                               color=color,
                               clarity=clarity)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)