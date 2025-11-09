import streamlit as st
# Safe import for load_model supports both tensorflow.keras and standalone keras
try:
    from tensorflow.keras.models import load_model
except Exception:  # fallback if TensorFlow isn't available in the editor env
    from keras.models import load_model
from streamlit.components.v1 import html
import numpy as np
import scipy.io
from src.visualization import plot_ecg
import google.generativeai as genai  # For the Gemini integration
import json
import html as html_lib  # for escaping user/assistant messages

# ---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(
    page_title='🫀 Phân loại ECG',
    page_icon="https://api.iconify.design/openmoji/anatomical-heart.svg?width=500",
    layout='wide',
    initial_sidebar_state="expanded"
)

#---------------------------------#
# Helper functions for localStorage

# Remove legacy get_from_local_storage/save_to_local_storage helpers (no longer used)

# Utility: escape HTML in chat messages
def escape_html(text: str) -> str:
    return html_lib.escape(str(text), quote=True)

#---------------------------------#
# Custom CSS for beautification
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    }
    
    .main-header {
        font-size: 2.5rem;
        color: #E63946;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #457B9D;
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        white-space: pre-wrap;
        background-color: #000000;
        border-radius: 4px 4px 0 0;
        gap: 1rem;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: #A8DADC;
        color: #1D3557;
        font-weight: 700;
    }
    .prediction-box {
        background-color: #F1FAEE;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .result-highlight {
        color: #E63946;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .footer-text {
        text-align: center;
        color: #1D3557;
        margin-top: 2rem;
        font-weight: 400;
    }
    .stSidebar {
        background-color: #000000;
    }
    .section-header {
        color: #1D3557;
        border-bottom: 2px solid #E63946;
        padding-bottom: 8px;
        margin-bottom: 16px;
        font-weight: 600;
    }
    .info-card {
        background-color: #F1FAEE;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* ChatGPT-style chat container */
    .chat-layout {
        display: flex;
        flex-direction: column;
        height: auto; /* was 70vh */
        min-height: 420px; /* reasonable minimum */
        max-height: 70vh; /* cap on very tall screens */
        border: 1px solid #2a2f33; /* darker to match dark theme */
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 6px rgba(0,0,0,0.4);
        background-color: #111418; /* dark background consistent with app */
    }

    .chat-container {
        background-color: transparent; /* remove white */
        padding: 0;
        margin: 0;
        flex: 1;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }
    
    .chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 18px 20px 12px 20px;
        display: flex;
        flex-direction: column;
        gap: 18px;
        background: linear-gradient(180deg, #161b20 0%, #13171b 100%);
        max-height: calc(70vh - 110px); /* allow scroll before growing too tall */
    }

    /* Standalone chat box (single-block, no empty wrappers) */
    .chat-box {
        background: linear-gradient(180deg, #161b20 0%, #13171b 100%);
        padding: 18px 20px 12px 20px;
        display: flex;
        flex-direction: column;
        gap: 18px;
        border: 1px solid #2a2f33;
        border-radius: 10px 10px 0 0;
        max-height: 60vh;
        overflow-y: auto;
        box-shadow: 0 2px 6px rgba(0,0,0,0.4);
    }
    
    /* Custom scrollbar for chat-box */
    .chat-box::-webkit-scrollbar { width: 6px; }
    .chat-box::-webkit-scrollbar-track { background: transparent; }
    .chat-box::-webkit-scrollbar-thumb { background: #cbd5e0; border-radius: 3px; }
    .chat-box::-webkit-scrollbar-thumb:hover { background: #a0aec0; }

    .chat-message {
        display: flex;
        gap: 12px;
        max-width: 100%;
        animation: fadeIn 0.3s ease-in;
    }
    
    .chat-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }
    
    .user-avatar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .bot-avatar {
        background: linear-gradient(135deg, #E63946 0%, #d62839 100%);
    }
    
    .chat-message-content {
        flex: 1;
        padding: 14px 18px;
        background: #1e242a;
        border: 1px solid #2d343b;
        border-radius: 12px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.4);
    }
    
    .chat-message-text { color: #e2e6ea; }
    .chat-message-role { color: #89b4fa; }
    
    .chat-input-container {
        border: 1px solid #2a2f33;
        border-top: none;
        padding: 14px 16px 16px 16px;
        background-color: #161b20;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.25);
    }
    
    /* Question button styling */
    .question-button {
        background-color: #f8f9fa;
        border: 1px solid #e0e5ec;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        display: block; /* added semicolon */
        width: 100%;
        text-align: left;
        font-weight: 500;
    }
    
    .question-button:hover {
        background-color: #F1FAEE;
        border-left: 3px solid #E63946;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Remove default padding/margin of Streamlit markdown containers */
    [data-testid="stMarkdownContainer"] {padding:0 !important; margin:0 !important;}
    .stMarkdown {padding:0 !important; margin:0 !important;}
    /* Tighten vertical space between consecutive markdown blocks */
    [data-testid="stMarkdownContainer"] + [data-testid="stMarkdownContainer"] {margin-top:0 !important;}
    /* Ensure chat layout not affected by markdown wrapper */
    .chat-layout [data-testid="stMarkdownContainer"] {padding:0 !important; margin:0 !important;}

    /* Tighten global layout spacing */
    section.main > div.block-container { padding-top: 6px !important; padding-bottom: 6px !important; }
    [data-testid="stVerticalBlock"] { padding: 0 !important; gap: 0.25rem !important; }
    [data-testid="stHorizontalBlock"] { gap: 0.5rem !important; }
    hr { margin: 6px 0 !important; }
    .stTabs { margin-bottom: 0 !important; }
    .stTabs [data-baseweb="tab-list"] { margin-bottom: 0 !important; }
    .stMarkdown p { margin: 0 !important; }
    .stButton button { margin-top: 0 !important; margin-bottom: 0 !important; }
</style>
""", unsafe_allow_html=True)

# Create tabs for different sections of the app
tabs = st.tabs(["📊 Phân loại ECG", "💬 Hỏi đáp Tim mạch"])

#---------------------------------#
# Data preprocessing and Model building

@st.cache_data
def read_ecg_preprocessing(uploaded_ecg):
    FS = 300
    maxlen = 30*FS

    uploaded_ecg.seek(0)
    mat = scipy.io.loadmat(uploaded_ecg)
    mat = mat["val"][0]

    uploaded_ecg = np.array([mat])

    X = np.zeros((1,maxlen))
    uploaded_ecg = np.nan_to_num(uploaded_ecg) # removing NaNs and Infs
    uploaded_ecg = uploaded_ecg[0,0:maxlen]
    uploaded_ecg = uploaded_ecg - np.mean(uploaded_ecg)
    uploaded_ecg = uploaded_ecg/np.std(uploaded_ecg)
    X[0,:len(uploaded_ecg)] = uploaded_ecg.T # padding sequence
    uploaded_ecg = X
    uploaded_ecg = np.expand_dims(uploaded_ecg, axis=2)
    return uploaded_ecg

model_path = 'models/weights-best.hdf5'
classes = ['Bình thường','Rung nhĩ','Khác','Nhiễu']
classes_en = ['Normal','Atrial Fibrillation','Other','Noise']

@st.cache_resource
def get_model(model_path):
    model = load_model(f'{model_path}')
    return model

@st.cache_resource
def get_prediction(data, _model):
    prob = _model(data)
    ann = np.argmax(prob)
    return classes[ann], prob

# Visualization --------------------------------------
@st.cache_resource
def visualize_ecg(ecg, FS):
    fig = plot_ecg(uploaded_ecg=ecg, FS=FS)
    return fig

#---------------------------------#
# Sidebar - Collects user input features into dataframe
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #ffffff;'>❤️ Công cụ Phân tích ECG</h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("### 1. Tải lên ECG của bạn")
    uploaded_file = st.file_uploader("Tải file ECG định dạng .mat", type=["mat"])

    st.markdown("<hr>", unsafe_allow_html=True)

    file_gts = {
        "A00001": "Bình thường",
        "A00002": "Bình thường",
        "A00003": "Bình thường",
        "A00004": "Rung nhĩ",
        "A00005": "Khác",
        "A00006": "Bình thường",
        "A00007": "Bình thường",
        "A00008": "Khác",
        "A00009": "Rung nhĩ",
        "A00010": "Bình thường",
        "A00015": "Rung nhĩ",
        "A00205": "Nhiễu",
        "A00022": "Nhiễu",
        "A00034": "Nhiễu",
    }
    
    valfiles = [
        'None',
        'A00001.mat','A00010.mat','A00002.mat','A00003.mat',
        "A00022.mat", "A00034.mat",'A00009.mat',"A00015.mat",
        'A00008.mat','A00006.mat','A00007.mat','A00004.mat',
        "A00205.mat",'A00005.mat'
    ]

    if uploaded_file is None:
        st.markdown("### 2. Hoặc chọn file mẫu")
        pre_trained_ecg = st.selectbox(
            'Chọn ECG mẫu',
            valfiles,
            format_func=lambda x: f'{x} ({(file_gts.get(x.replace(".mat","")))})' if ".mat" in x else x,
            index=1,
        )
        if pre_trained_ecg != "None":
            f = open("data/validation/"+pre_trained_ecg, 'rb')
            if not uploaded_file:
                uploaded_file = f
    else:
        st.info("Xóa file trên để sử dụng file mẫu.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div class='footer-text'>Phát triển bởi <a href='#'>BS. Nguyễn Lê Hoài Linh</a></div>", unsafe_allow_html=True)

#---------------------------------#
# Main panel - Tab 1: ECG Classification
with tabs[0]:
    st.markdown("<h1 class='main-header'>🫀 Phân loại ECG</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Phát hiện Rung nhĩ, Nhịp bình thường, Nhịp khác, hoặc Nhiễu từ ECG của bạn</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    if uploaded_file is not None:
        # Initialize model
        model = get_model(f'{model_path}')
        
        col1, col2 = st.columns([0.55, 0.45])

        with col1:  # visualize ECG
            st.markdown("### Hiển thị ECG")
            with st.spinner("Đang xử lý dữ liệu ECG..."):
                ecg = read_ecg_preprocessing(uploaded_file)
                fig = visualize_ecg(ecg, FS=300)
                st.pyplot(fig, use_container_width=True)

        with col2:  # classify ECG
            st.markdown("### Kết quả Phân tích")
            with st.spinner(text="Đang chạy mô hình..."):
                pred, conf = get_prediction(ecg, model)
            
            # st.markdown("<div class='prediction-box'>", unsafe_allow_html=True)
            st.markdown(f"<h3>ECG được phân loại là <span class='result-highlight'>{pred}</span></h3>", unsafe_allow_html=True)
            
            pred_confidence = conf[0, np.argmax(conf)]*100
            st.markdown(f"<p>Độ tin cậy: <b>{pred_confidence:.1f}%</b></p>", unsafe_allow_html=True)
            
            st.markdown("#### Phân bố Xác suất")
            
            # Create a bar chart for the confidence levels
            conf_data = {classes[i]: float(conf[0,i]*100) for i in range(len(classes))}
            chart_data = {"Loại Nhịp": list(conf_data.keys()), "Độ tin cậy (%)": list(conf_data.values())}
            
            st.bar_chart(chart_data, x="Loại Nhịp", y="Độ tin cậy (%)", use_container_width=True)
            
            # Create a table with detailed confidence levels
            st.markdown("#### Kết quả Chi tiết")
            mkd_pred_table = [
                "| Loại Nhịp | Độ tin cậy |",
                "| --- | --- |"
            ]
            for i in range(len(classes)):
                mkd_pred_table.append(f"| {classes[i]} | {conf[0,i]*100:3.1f}% |")
            mkd_pred_table = "\n".join(mkd_pred_table)
            st.markdown(mkd_pred_table)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Include interpretation info
            if pred == "Rung nhĩ":
                st.info("📌 Rung nhĩ được đặc trưng bởi nhịp tim không đều và nhanh. Tình trạng này làm tăng nguy cơ đột quỵ và suy tim.")
            elif pred == "Bình thường":
                st.success("✅ ECG của bạn cho thấy nhịp tim bình thường. Vẫn khuyến nghị kiểm tra sức khỏe tim mạch định kỳ.")
            elif pred == "Khác":
                st.warning("⚠️ ECG cho thấy nhịp bất thường không được phân loại là Rung nhĩ. Nên đánh giá lâm sàng thêm.")
            elif pred == "Nhiễu":
                st.error("❗ ECG chứa quá nhiều nhiễu để có thể phân tích chính xác. Nên thực hiện lại ECG trong môi trường kiểm soát tốt hơn.")
    else:
        st.info("👈 Vui lòng tải lên file ECG hoặc chọn mẫu từ thanh bên để bắt đầu.")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("https://api.iconify.design/openmoji/anatomical-heart.svg?width=300", use_container_width=True)
            
#---------------------------------#
# Tab 2: Ask the Cardio
with tabs[1]:
    st.markdown('<h1 class="main-header">💬 Trợ lý Tim mạch AI</h1>', unsafe_allow_html=True)
    
    # JavaScript for localStorage (chat history only). Also clear any old API key from previous versions.
    st.markdown("""
    <script>
      function saveChatHistory(history){localStorage.setItem('chat_history', JSON.stringify(history));}
      function getChatHistory(){const h=localStorage.getItem('chat_history');return h?JSON.parse(h):[];}
      function clearChatHistory(){localStorage.removeItem('chat_history');}
      try{localStorage.removeItem('gemini_api_key');}catch(e){}
    </script>
    """, unsafe_allow_html=True)
    
    # Initialize chat history
    if "cardio_chat_history" not in st.session_state:
        st.session_state.cardio_chat_history = []

    # Remove unused selected_cardio_question state
    if "user_gemini_api_key" not in st.session_state:
        st.session_state.user_gemini_api_key = ""
    
    # Initialize chat loaded flag
    if "chat_loaded_from_storage" not in st.session_state:
        st.session_state.chat_loaded_from_storage = False
    
    # Initialize main input state for binding with text_input
    if "cardio_assistant_query" not in st.session_state:
        st.session_state.cardio_assistant_query = ""
    if "auto_submit" not in st.session_state:
        st.session_state.auto_submit = False
    if "show_api_input" not in st.session_state:
        st.session_state.show_api_input = False
    if "reset_input" not in st.session_state:
        st.session_state.reset_input = False
    # Clear input BEFORE widget renders to avoid Streamlit restriction
    if st.session_state.reset_input:
        st.session_state.cardio_assistant_query = ""
        st.session_state.reset_input = False
    
    # API Key input section - Compact at top
    col_key1, col_key2, col_key3 = st.columns([5, 1, 1])
    
    with col_key1:
        if st.session_state.user_gemini_api_key:
            st.success("✅ API key đã nhập (chỉ lưu trong phiên, không lưu trình duyệt)")
        else:
            st.info("🔐 Nhập API key để dùng chatbot. Key KHÔNG lưu vào localStorage. Có thể cấu hình lâu dài trong .streamlit/secrets.toml hoặc biến môi trường GEMINI_API_KEY.")
    
    with col_key2:
        if st.session_state.user_gemini_api_key:
            if st.button("🗑️", help="Xóa API key phiên", use_container_width=True):
                st.session_state.user_gemini_api_key = ""
                st.rerun()
        else:
            if st.button("🔑", help="Nhập API key", use_container_width=True):
                st.session_state.show_api_input = True
    
    with col_key3:
        # Help button opens guide in a new tab
        if st.button("❓", help="Hướng dẫn lấy API key", use_container_width=True):
            st.markdown("<script>window.open('https://github.com/thienvdt/AI-ECG-Analyzer/blob/main/HUONG_DAN_API_KEY.md','_blank')</script>", unsafe_allow_html=True)
    
    # Show API input dialog if needed
    if not st.session_state.user_gemini_api_key:
        with st.expander("🔑 Cấu hình API Key", expanded=st.session_state.show_api_input):
            user_api_key_input = st.text_input(
                "Nhập Gemini API Key:",
                type="password",
                placeholder="AIzaSy...",
                help="Key chỉ lưu trong phiên (session), không lưu trình duyệt. Có thể cấu hình lâu dài trong .streamlit/secrets.toml hoặc biến môi trường GEMINI_API_KEY."
            )
            st.markdown("- 👉 Tạo key tại Makersuite: https://makersuite.google.com/app/apikey")
            st.markdown("- 📘 Hướng dẫn chi tiết (có hình): https://github.com/thienvdt/AI-ECG-Analyzer/blob/main/HUONG_DAN_API_KEY.md")
             
            if user_api_key_input:
                st.session_state.user_gemini_api_key = user_api_key_input  # keep only in session
                st.session_state.show_api_input = False
                st.rerun()
    
    # Set API key status
    if st.session_state.user_gemini_api_key:
        GEMINI_API_KEY = st.session_state.user_gemini_api_key
        has_api_key = True
    else:
        try:
            GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
            if GEMINI_API_KEY and GEMINI_API_KEY != "YOUR_API_KEY_HERE":
                has_api_key = True
            else:
                has_api_key = False
        except:
            has_api_key = False
            GEMINI_API_KEY = None
    
    st.markdown("---")
    
    # Function to generate responses about ECG and heart health
    def generate_cardio_response(prompt):
            if has_api_key:
                try:
                    genai.configure(api_key=GEMINI_API_KEY)
                    gemini_prompt = f"""
Bạn là trợ lý tim mạch chuyên về giải thích ECG, rối loạn nhịp tim và sức khỏe tim mạch.
Chỉ trả lời các câu hỏi liên quan đến tim mạch và ECG với thông tin y tế chính xác.
Nếu câu hỏi không liên quan đến tim mạch, hãy lịch sự thông báo rằng bạn chỉ có thể trả lời các câu hỏi về tim và ECG.

Đặc biệt tập trung vào các tình trạng và mẫu ECG sau:
- Nhịp xoang bình thường
- Rung nhĩ (Atrial Fibrillation)
- Cuồng nhĩ (Atrial Flutter)
- Nhịp nhanh thất
- Kéo dài khoảng QT
- ST chênh lên và chênh xuống
- Blốc tim (độ 1, độ 2, độ 3)
- Blốc nhánh bó
- Co thắt thất sớm
- Co thắt nhĩ sớm
- Vị trí chuyển đạo và giải thích ECG

**Câu hỏi của người dùng:** {prompt}
Hãy cung cấp câu trả lời rõ ràng, ngắn gọn và chính xác bằng tiếng Việt về tim mạch và giải thích ECG.
"""
                    model_names = ["gemini-pro-latest", "gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro", "gemini-1.0-pro"]
                    for model_name in model_names:
                        try:
                            model = genai.GenerativeModel(model_name)
                            response = model.generate_content(gemini_prompt)
                            break
                        except Exception as model_error:
                            if "not found" in str(model_error) and model_name != model_names[-1]:
                                continue
                            else:
                                raise model_error
                    return response.text
                except Exception as e:
                    error_msg = str(e)
                    lower_msg = error_msg.lower()
                    if "reported as leaked" in lower_msg or ("403" in lower_msg and "leak" in lower_msg):
                        st.session_state.user_gemini_api_key = ""
                        st.session_state.show_api_input = True
                        return "🔐 API key bị đánh dấu là lộ (403) và đã được xóa khỏi phiên. Nhập key mới hoặc cấu hình trong secrets.toml."
                    if "api_key_invalid" in lower_msg or "invalid api key" in lower_msg:
                        st.session_state.user_gemini_api_key = ""
                        st.session_state.show_api_input = True
                        return "❌ API key không hợp lệ/hết hạn. Nhập key mới hoặc thêm vào secrets.toml."
                    if "quota" in lower_msg:
                        return "⚠️ Đã vượt quá giới hạn sử dụng API. Vui lòng kiểm tra quota hoặc thử lại sau."
                    return f"❌ Lỗi: {error_msg}"
            else:
                cardio_knowledge = {
                    "atrial fibrillation": "Atrial fibrillation (AFib) is an irregular and often rapid heart rhythm that can increase risk of stroke, heart failure, and other heart-related complications. On an ECG, it's characterized by irregular R-R intervals and absence of P waves.",
                    "normal ecg": "A normal ECG typically shows regular rhythm with P waves, QRS complexes, and T waves in sequence. The P-R interval is usually 0.12-0.20 seconds, QRS duration 0.06-0.10 seconds, and Q-T interval 0.36-0.44 seconds.",
                    "heart rate": "Normal resting heart rate for adults ranges from 60-100 beats per minute (BPM). Athletes may have lower resting heart rates, sometimes as low as 40 BPM, which is usually not a concern.",
                    "ecg leads": "A standard 12-lead ECG uses electrodes placed on the limbs and chest to record electrical activity from different angles. These include leads I, II, III, aVR, aVL, aVF (limb leads) and V1-V6 (chest leads).",
                    "premature beats": "Premature beats can be atrial (PACs) or ventricular (PVCs). They appear as early beats on the ECG and are usually benign but can sometimes indicate underlying heart disease.",
                    "ventricular tachycardia": "Ventricular tachycardia is a rapid heart rhythm starting in the ventricles. On ECG, it appears as wide QRS complexes at a rate typically >100 BPM. It can be life-threatening and requires immediate treatment.",
                    "heart": "The heart is a muscular organ responsible for pumping blood throughout your body. An ECG records the electrical activity of your heart and helps detect various heart conditions like arrhythmias, heart attacks, and structural abnormalities.",
                    "ecg": "An electrocardiogram (ECG or EKG) is a test that records the electrical activity of your heart. It shows how fast your heart beats and whether its rhythm is steady or irregular. ECGs are used to detect heart problems like arrhythmias, heart attacks, and structural abnormalities.",
                    "arrhythmia": "Cardiac arrhythmias are abnormal heart rhythms that cause the heart to beat too fast, too slow, or irregularly. Common types include atrial fibrillation, atrial flutter, ventricular tachycardia, and bradycardia. ECGs are the primary tool for diagnosing arrhythmias.",
                    "bradycardia": "Bradycardia is a slower than normal heart rate, typically below 60 beats per minute. It may be normal in athletic individuals but can cause symptoms like fatigue, dizziness, and fainting in others. On an ECG, it appears as normally formed complexes that occur at a slow rate.",
                    "tachycardia": "Tachycardia is a faster than normal heart rate, typically above 100 beats per minute. It can be sinus tachycardia (normal response to exercise or stress) or pathological. On an ECG, it appears as normally formed complexes occurring at a rapid rate.",
                    "p wave": "The P wave on an ECG represents atrial depolarization (contraction of the atria). Normal P waves are rounded, upright in lead II, and less than 0.12 seconds in duration. Abnormal P waves can indicate atrial enlargement or ectopic atrial rhythms.",
                    "qrs complex": "The QRS complex represents ventricular depolarization (contraction of the ventricles). Normal QRS duration is 0.06-0.10 seconds. Wide QRS complexes can indicate bundle branch blocks, ventricular rhythms, or other conduction abnormalities.",
                    "t wave": "The T wave represents ventricular repolarization (recovery of the ventricles). Normal T waves are slightly asymmetric with a gradual upslope and faster downslope. Abnormal T waves can indicate ischemia, electrolyte disturbances, or other cardiac conditions.",
                    "bundle branch block": "Bundle branch blocks occur when there's a delay or obstruction in the electrical conduction pathway of the heart. On an ECG, they appear as wide QRS complexes (>0.12 seconds) with characteristic patterns depending on whether the right or left bundle is affected.",
                    "heart attack": "A heart attack (myocardial infarction) occurs when blood flow to part of the heart muscle is blocked. On an ECG, it can show ST segment elevation, Q waves, or T wave inversions depending on the timing and location of the infarction."
                }
                
                response = "Tôi không có thông tin cụ thể về điều đó trong cơ sở kiến thức tim mạch của mình. Vui lòng hỏi điều gì đó liên quan đến ECG hoặc tình trạng tim mạch."
                prompt_lower = prompt.lower()
                for keyword, info in cardio_knowledge.items():
                    if keyword.lower() in prompt_lower:
                        response = info
                        break
                if any(word in prompt_lower for word in ["ecg là gì", "điện tim đồ", "điện tâm đồ"]):
                    response = cardio_knowledge.get("ecg", response)
                if any(word in prompt_lower for word in ["rối loạn nhịp", "loạn nhịp tim", "arrhythmia"]):
                    response = cardio_knowledge.get("arrhythmia", response)
                if any(word in prompt_lower for word in ["rung nhĩ", "atrial fibrillation"]):
                    response = cardio_knowledge.get("atrial fibrillation", response)
                return response
            
    # ChatGPT-style interface (render chat in a single HTML block to avoid empty wrappers)
    messages_html_parts = []
    messages_html_parts.append('<div class="chat-box" id="chat-messages">')
    if len(st.session_state.cardio_chat_history) == 0:
        messages_html_parts.append('''
        <div class="chat-message">
            <div class="chat-avatar bot-avatar">🫀</div>
            <div class="chat-message-content">
                <div class="chat-message-role">Trợ lý Tim mạch AI</div>
                <div class="chat-message-text">
                    Xin chào! Tôi là trợ lý tim mạch AI của bạn. Tôi có thể giúp bạn:<br><br>
                    • Giải thích các mẫu ECG<br>
                    • Trả lời câu hỏi về rối loạn nhịp tim<br>
                    • Cung cấp thông tin về sức khỏe tim mạch<br><br>
                    Bạn có câu hỏi gì cho tôi không?
                </div>
            </div>
        </div>
        ''')
    else:
        for role, message in st.session_state.cardio_chat_history:
            safe_message = escape_html(message).replace('\n', '<br>')
            if role == "Bạn":
                messages_html_parts.append(f'''
                <div class="chat-message">
                    <div class="chat-avatar user-avatar">👨‍⚕️</div>
                    <div class="chat-message-content">
                        <div class="chat-message-role">Bạn</div>
                        <div class="chat-message-text">{safe_message}</div>
                    </div>
                </div>
                ''')
            else:
                messages_html_parts.append(f'''
                <div class="chat-message">
                    <div class="chat-avatar bot-avatar">🫀</div>
                    <div class="chat-message-content">
                        <div class="chat-message-role">Trợ lý Tim mạch AI</div>
                        <div class="chat-message-text">{safe_message}</div>
                    </div>
                </div>
                ''')
    messages_html_parts.append('</div>')
    st.markdown("".join(messages_html_parts), unsafe_allow_html=True)

    # Auto-scroll to bottom
    st.markdown("""
    <script>
        setTimeout(function() {
            var chatMessages = document.getElementById('chat-messages');
            if (chatMessages) {
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        }, 100);
    </script>
    """, unsafe_allow_html=True)
    
    # Input area (no HTML wrapper to prevent empty container)
    col_input1, col_input2, col_input3 = st.columns([6, 1, 1])
    
    with col_input1:
        user_query = st.text_input(
            "Tin nhắn",
            key="cardio_assistant_query",
            placeholder="Nhắn tin cho Trợ lý Tim mạch AI...",
            label_visibility="collapsed"
        )
    
    with col_input2:
        submit_button = st.button("➤ Gửi", use_container_width=True, type="primary")
    
    with col_input3:
        clear_chat_button = st.button("🗑️ Xóa", use_container_width=True, help="Xóa lịch sử chat")
        
    # Handle clear chat
    if clear_chat_button:
        st.session_state.cardio_chat_history = []
        st.markdown('<script>clearChatHistory();</script>', unsafe_allow_html=True)
        st.rerun()

    # Auto submit if triggered by suggestion button
    if st.session_state.auto_submit and st.session_state.cardio_assistant_query:
        submit_button = True  # force submission path
        st.session_state.auto_submit = False
        user_query = st.session_state.cardio_assistant_query

    # Handle question submission
    if submit_button and user_query:
        with st.spinner("🤔 Đang suy nghĩ..."):
            try:
                response = generate_cardio_response(user_query)
                st.session_state.cardio_chat_history.append(("Bạn", user_query))
                st.session_state.cardio_chat_history.append(("Trợ lý Tim mạch", response))
                chat_json = json.dumps(st.session_state.cardio_chat_history, ensure_ascii=False)
                chat_json_escaped = chat_json.replace("'", "\\'")
                save_script = f"""
                <script>
                    localStorage.setItem('chat_history', '{chat_json_escaped}');
                </script>
                """
                st.markdown(save_script, unsafe_allow_html=True)
                st.session_state.reset_input = True
                st.rerun()
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

    # Quick questions
    st.markdown("##### 💡 Hoặc thử các câu hỏi gợi ý")

    example_questions = [
        "ECG bình thường trông như thế nào?",
        "Làm thế nào để nhận biết rung nhĩ trên ECG?",
        "Nguyên nhân gây ST chênh lên trên ECG là gì?",
        "Khoảng QT là gì và tại sao nó quan trọng?",
    ]
    
    def ask_example(question):
        st.session_state.cardio_assistant_query = question
        st.session_state.auto_submit = True
        # ensure previous content removed next run if auto_submit triggers
        st.session_state.reset_input = False

    cols = st.columns(2)
    for i, question in enumerate(example_questions):
        with cols[i % 2]:
            st.button(
                f"💬 {question}", 
                key=f"q_{i}", 
                on_click=ask_example, 
                args=(question,),
                use_container_width=True
            )

    # Disclaimer
    st.markdown("""
    <div style='background-color: #fff3cd; padding: 12px; border-radius: 6px; margin-top: 12px; border-left: 4px solid #ffc107;'>
        <p style='color: #856404; margin: 0; font-size: 14px;'><strong>⚠️ Lưu ý:</strong> Trợ lý AI này chỉ cung cấp thông tin tham khảo. Luôn tham khảo ý kiến bác sĩ chuyên khoa để chẩn đoán và điều trị.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div class='footer-text'>Phát triển bởi BS. Nguyễn Lê Hoài Linh - Ứng dụng Machine Learning trong Y tế</div>", unsafe_allow_html=True)
