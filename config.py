# 存放各项配置

# LLM
TASK_LLM_API = ""
JUDGE_LLM_API = ""
VLM_API = ""

# RAG
RAG_MODEL = "/home/xiao/.cache/huggingface/hub/models--sentence-transformers--all-mpnet-base-v2/snapshots/e8c3b32edf5434bc2275fc9bab85f82640a19130"
#RAG_MODEL = "/home/xiao/thesis_ws/rag_model/models--sentence-transformers--all-mpnet-base-v2/snapshots/e8c3b32edf5434bc2275fc9bab85f82640a19130"
RAG_SIMILARITY_THRESHOLD = 0.3
HISTORY_PATH = "big_brain/memory/rag_history.json"


# 物体默认长宽高(cm)
BOX_SIZE = (50, 50, 50)

