from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageOps
import io
import numpy as np

# Agora que alinhamos as versões (TF 2.15 + Keras 2.15), isso VAI funcionar
from tensorflow.keras.models import load_model

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CARREGAMENTO DA IA ---
model = None
class_names = []

def load_ai_model():
    global model, class_names
    try:
        print("🔄 Carregando modelo de IA... aguarde...")
        # compile=False evita erros de compatibilidade do otimizador
        model = load_model("keras_model.h5", compile=False)
        class_names = open("labels.txt", "r", encoding="utf-8").readlines()
        print("✅ Modelo carregado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao carregar modelo: {e}")

load_ai_model()

def predict_real_ai(image_bytes):
    if model is None:
        return {"error": "Modelo não carregado."}

    # 1. Tratamento
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # 2. Array e Normalização
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # 3. Formato
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # 4. Previsão
    prediction = model.predict(data)
    index = np.argmax(prediction)

    # 5. Nome da Classe
    if index < len(class_names):
        class_name = class_names[index].strip()
        if len(class_name) > 2 and class_name[1] == ' ':
            class_name = class_name[2:]
    else:
        class_name = f"Classe {index}"

    confidence_score = float(prediction[0][index])

    return {"class": class_name, "confidence": confidence_score}

@app.get("/")
def read_root():
    return {"message": "API Online"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        result = predict_real_ai(contents)
        return result
    except Exception as e:
        return {"error": str(e)}