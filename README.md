# FlowChatAI
ChatGPTを利用してフローチャートを作成する。
## 準備

.envファイルを作成

```.env
OPENAI_API_KEY=[APIキー]
```

## 実行方法

```
pip install -r requirements.txt
```

```
uvicorn main:app --reload
```

127.0.0.1:8000にアクセス。