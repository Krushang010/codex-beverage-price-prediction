# ─────────────────────────────────────────────────────────────
# RUN THIS CELL IN YOUR NOTEBOOK to save the trained model
# ─────────────────────────────────────────────────────────────
import pickle

# Save the best model (tuned LightGBM)
# Replace 'search.best_estimator_' with your actual model variable
# Could be: lgbm, lgbm_reduced, search.best_estimator_

model_to_save = search.best_estimator_   # ← change if needed

with open('lgbm_model.pkl', 'wb') as f:
    pickle.dump(model_to_save, f)

print("✅ Model saved as lgbm_model.pkl")
print(f"   File size: {__import__('os').path.getsize('lgbm_model.pkl') / 1024:.1f} KB")
