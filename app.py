import streamlit as st
import hashlib
import base64
from datetime import datetime

# =====================================================================
# LÕI MUỐI BÍ MẬT - GIỮ NGUYÊN 100% TỪ CODE GỐC CỦA CHỦ TỊCH NTS
# =====================================================================
# 1. Từ file: giai_tool_tool.py
SECRET_SALT_PRO = "NTS_SECRET_SUPER_SALT_999999_PRO_2026" 
SECRET_SALT_STD = "NTS_SECRET_SUPER_SALT_999999_STD_2026" 

# 2. Từ file: key_tiktok.py
SECRET_SALT_TIKTOK = "NTS_100_TY_PRO_MAX_WHITEHAT_2026_@#$%"
# =====================================================================

# Cấu hình giao diện chuẩn phong thái Đại Gia Công Nghệ
st.set_page_config(page_title="NTS Studio - VIP KeyGen", page_icon="🔥", layout="centered")

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #66fcf1; color: #0b0c10; font-weight: bold; border-radius: 8px; width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔥 NTS STUDIO - BỘ PHÁT HÀNH BẢN QUYỀN VIP")
st.write("Hệ thống Đúc Key Độc Quyền Tích Hợp Đa Nền Tảng")
st.divider()

# --- MENU CHỌN LÕI ĐÚC KEY ---
tool_choice = st.selectbox(
    "🛠️ CHỌN TOOL CẦN CẤP PHÁT:",
    ["1. Tool YouTube / Tool Đa Năng", "2. Tool TikTok Downloader"]
)

st.divider()

if tool_choice == "1. Tool YouTube / Tool Đa Năng":
    st.subheader("📺 LÕI CẤP PHÁT YOUTUBE / STD / PRO")
    
    # Giao diện y hệt giai_tool_tool.py
    hwid_input = st.text_input("💻 Nhập mã HWID của khách:").strip().upper()
    
    type_choice = st.radio(
        "📦 Chọn loại Key muốn cấp:",
        ["1. Bản Thường (Standard - 29k / Tải YT thường )", "2. Bản PRO (VIP - Mở khóa Bypass Video Hội Viên)"]
    )
    
    date_input = st.text_input("📅 Nhập ngày hết hạn (Định dạng: DD/MM/YYYY - VD: 30/08/2026):").strip()
    
    if st.button("🚀 ĐÚC KEY YOUTUBE"):
        if not hwid_input or not date_input:
            st.error("❌ Lỗi: Thiếu mã HWID hoặc Ngày hết hạn!")
        else:
            # Thuật toán gốc từ giai_tool_tool.py
            if '2' in type_choice:
                active_salt = SECRET_SALT_PRO
                package_name = "PRO (VIP)"
            else:
                active_salt = SECRET_SALT_STD
                package_name = "STANDARD (Thường)"
                
            try:
                date_obj = datetime.strptime(date_input, "%d/%m/%Y")
                date_str = date_obj.strftime("%Y%m%d")
                
                raw_str = f"{hwid_input}{date_str}{active_salt}"
                activation_key = hashlib.sha256(raw_str.encode()).hexdigest()[:20].upper()
                
                st.success(f"✅ ĐÃ CẤP PHÁT GÓI: {package_name}")
                st.code(activation_key, language="text")
                st.info(f"Hạn sử dụng: {date_obj.strftime('%d/%m/%Y')}")
                st.caption("👉 Copy Key trên gửi cho khách! Tiền đã vào túi 💸")
            except ValueError:
                st.error("❌ Lỗi: Sai định dạng ngày! Phải nhập chính xác kiểu Ngày/Tháng/Năm (VD: 15/09/2026).")

elif tool_choice == "2. Tool TikTok Downloader":
    st.subheader("🎬 LÕI CẤP PHÁT TIKTOK (BẢO MẬT BASE64)")
    
    # Giao diện y hệt key_tiktok.py
    khach_hwid = st.text_input("💻 Nhập HWID của khách:").strip()
    ngay_het_han = st.text_input("📅 Nhập ngày hết hạn (Định dạng: YYYY-MM-DD - VD: 2026-12-31):").strip()
    
    if st.button("🚀 ĐÚC KEY TIKTOK"):
        if not khach_hwid or not ngay_het_han:
            st.error("❌ Lỗi: Thiếu HWID hoặc Ngày hết hạn!")
        else:
            # Thuật toán gốc từ key_tiktok.py
            try:
                datetime.strptime(ngay_het_han, "%Y-%m-%d")
                
                raw_data = f"{khach_hwid}|{ngay_het_han}|{SECRET_SALT_TIKTOK}"
                signature = hashlib.sha256(raw_data.encode()).hexdigest()
                
                final_key_raw = f"{ngay_het_han}|{signature}"
                final_key = base64.b64encode(final_key_raw.encode()).decode()
                
                st.success("✅ ĐÚC KEY TIKTOK THÀNH CÔNG!")
                st.code(final_key, language="text")
                st.caption("👉 Done! Lụm lúa! 🤑")
            except ValueError:
                st.error("❌ LỖI: Ngày tháng không đúng định dạng YYYY-MM-DD")
