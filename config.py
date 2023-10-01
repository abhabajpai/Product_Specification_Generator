from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_TYPE"]="azure"
os.environ["OPENAI_API_VERSION"]="2023-03-15"
os.environ["OPENAI_API_BASE"]=os.getenv("OPENAI_API_BASE")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

BASE_URL=os.getenv("OPENAI_API_BASE")
API_KEY=os.getenv("OPENAI_API_KEY")
DEPLOYMENT_NAME="GPT3-5"

llm_azure=AzureChatOpenAI(
    openai_api_base=BASE_URL,
    openai_api_version="2023-05-15",
    deployment_name=DEPLOYMENT_NAME,
    openai_api_key=API_KEY,
    openai_api_type="azure",
    temperature=0.6,
   
)