import numpy as np
from model_layer import WakeWordModel

X = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day58_Training\X_train.npy")
Y = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day58_Training\Y_train.npy")

model = WakeWordModel()

out = model.conv.forward(X)
out = model.relu.forward(out)
out = model.pool.forward(out)
features = model.flat.forward(out)

print("Features shape :",features.shape)
features = features / np.max(features)
Y = Y.reshape(-1, 1)

print("Features Shape:", features.shape)
print("Weights Shape:", model.dense.weights.shape)
print("Y Shape:", Y.shape)

for i in range(10000):
    pred = model.dense.forward(features)
    error = Y - pred
    model.dense.backward(error, 0.01)
    if i% 1000 == 0:
        print(f"mean at epoch {i} is {np.mean(np.abs(error))}")



# --- Verification ---
final_preds = model.dense.forward(features)

print("\n--- RESULTS ---")
for i in range(len(Y)):
    truth = Y[i][0]
    guess = final_preds[i][0]
    
    # Interpretation
    status = "CORRECT" if abs(truth - guess) < 0.5 else "WRONG"
    
    print(f"File {i}: Truth={truth:.0f}, Pred={guess:.4f} -> {status}")