from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier

# 創建一個示例數據集（假設已經準備好了）
X, y = your_data, your_labels

# 創建一個隨機森林分類器（或您想要的模型）
model = RandomForestClassifier()

# 創建KFold交叉驗證對象，這裡選擇3折交叉驗證
kfold = KFold(n_splits=3, shuffle=True, random_state=42)

# 使用cross_val_score來執行交叉驗證，並計算準確率
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

# 輸出每一折的準確率
for i, score in enumerate(scores):
    print(f'Fold {i+1} Accuracy: {score:.2f}')

# 計算平均準確率
mean_accuracy = scores.mean()
print(f'Mean Accuracy: {mean_accuracy:.2f}')
