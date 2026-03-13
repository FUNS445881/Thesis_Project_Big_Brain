# 存放各项配置

# LLM
# 智谱API
ZHIPU_API_KEY = "6b24fb599ed1496299e9917ef0dcb4c4.egZDcEBCZC4LUarc"
ZHIPU_BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"
ZHIPU_LLM_MODEL = "glm-4.7-flash"
ZHIPU_VLM_MODEL = "glm-4.6v-flash"

# 硅基流动API
SILICONFLOW_API_KEY = "sk-fhppghluvmkqikppmymzcqvwnekjqyfofleputyqosazejgf"
SILICONFLOW_BASE_URL = "https://api.siliconflow.cn/v1"
SILICONFLOW_LLM_MODEL = "Qwen/Qwen2.5-7B-Instruct"

TARGET_API_KEY = SILICONFLOW_API_KEY
TARGET_BASE_URL = SILICONFLOW_BASE_URL
TARGET_LLM_MODEL = SILICONFLOW_LLM_MODEL
# Planner LLM
TASK_LLM_API_KEY = TARGET_API_KEY
TASK_LLM_BASE_URL = TARGET_BASE_URL
TASK_LLM_MODEL = TARGET_LLM_MODEL

# Judge LLM
JUDGE_LLM_API_KEY = TARGET_API_KEY
JUDGE_LLM_BASE_URL = TARGET_BASE_URL
JUDGE_LLM_MODEL = TARGET_LLM_MODEL

# VLM
VLM_API_KEY = ZHIPU_API_KEY
VLM_API_BASE_URL = ZHIPU_BASE_URL
VLM_MODEL = ZHIPU_VLM_MODEL

MAX_REPLAN_TIMES = 3

# RAG
RAG_MODEL = "/home/xiao/.cache/huggingface/hub/models--sentence-transformers--all-mpnet-base-v2/snapshots/e8c3b32edf5434bc2275fc9bab85f82640a19130"
#RAG_MODEL = "/home/xiao/thesis_ws/rag_model/models--sentence-transformers--all-mpnet-base-v2/snapshots/e8c3b32edf5434bc2275fc9bab85f82640a19130"
RAG_SIMILARITY_THRESHOLD = 0.5
HISTORY_PATH = "big_brain/memory/rag_history_old.json"


# 物体默认长宽高(cm)
BOX_SIZE = (50, 50, 50)

# YOLO Detect Objects
YOLO_DETECT_OBJECTS = ["desk","chair","bottle","apple","banana"]