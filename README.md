# FlowChatAI
ChatGPTを利用してフローチャートを作成する。
![image](https://user-images.githubusercontent.com/44220424/234575543-5e986ff6-11be-4270-b89f-7ee3f2a80f9a.png)

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
