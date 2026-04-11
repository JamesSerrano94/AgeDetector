import os 
from PIL import Image
import cv2
import mediapipe as mp
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

faces = "UTKFace"
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
leftForehead = 21
rightForehead = 368
lip = 11
chin = 152

def distance(x1, y1, x2, y2):
    return (abs(x2 - x1) * abs(x2 - x1) + abs(y2 - y1) * abs(y2 - y1)) ** 0.5

X = []
Y = []

for file in os.listdir(faces):
    age = int(file.split("_")[0])
    filepath = os.path.join(faces, file)
    image = cv2.imread(filepath)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True) as face_mesh:
        results = face_mesh.process(image_rgb)
    if results.multi_face_landmarks is not None:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = image.shape
            #Don't include data that doesn't fit
            x1, x2, x3, x4, y1, y2, y3, y4 = -999, -999, -999, -999, -999, -999, -999, -999


            for i, landmark in enumerate(face_landmarks.landmark):
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                if i == leftForehead:
                    x1 = x
                    y1 = y
                elif i == rightForehead:
                    x2 = x
                    y2 = y
                elif i == lip:
                    x3 = x
                    y3 = y
                elif i == chin:
                    x4 = x
                    y4 = y
                
                    # print specific dots, optional
                    #     cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

                    # optional: label points
                    #cv2.putText(image, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)
            if x1 == -999 or x2 == -999 or x3 == -999 or x4 == -999: #in case something didn't work right
                continue
            if y1 == -999 or y2 == -999 or y3 == -999 or y4 == -999:
                continue
            X.append([distance(x1, y1, x2, y2)/distance(x3, y3, x4, y4)])
            Y.append(age)


X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
print("MAE:", mae)

            


        # image_rgb_display = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # img = Image.fromarray(image_rgb_display)
        # img.show()



        
