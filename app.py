import streamlit as st
import hashlib
import base64
from datetime import datetime

# ==============================================================================
# CONFIG GIAO DIỆN STREAMLIT - NTS STUDIO
# ==============================================================================
st.set_page_config(page_title="NTS Hacker Empire - Admin Panel", page_icon="🔥", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #ff4b4b;'>🔥 NTS STUDIO - TRUNG TÂM CẤP PHÁT BẢN QUYỀN 🔥</h1>
    <p style='text-align: center; color: gray;'>Hệ thống tự động hóa cấp Key đa nền tảng - Doanh thu tự động</p>
    <hr>
""", unsafe_allow_html=True)

# ==============================================================================
# LÕI THUẬT TOÁN 1: PDF MASTER TOOL
# ==============================================================================
MASTER_KEY_PDF = "GHOST_HACK_NTS_9999"

def generate_pdf_key(hwid: str, expiry_date: str, is_pro: bool = False):
    try:
        expiry_date = expiry_date.strip().replace("-", "/").replace(".", "/")
        parts = expiry_date.split("/")
        if len(parts) == 3 and len(parts[2]) == 4:
            parts[2] = parts[2][2:] 
            expiry_date = "/".join(parts)
            
        dt = datetime.strptime(expiry_date, "%d/%m/%y")
        date_str = dt.strftime("%d%m%y") 
        
        raw_data = date_str + ("1" if is_pro else "0")
        raw_bytes = raw_data.encode('utf-8')
        
        keystream = hashlib.md5((hwid + MASTER_KEY_PDF).encode('utf-8')).digest()
        xored = bytes([raw_bytes[i] ^ keystream[i] for i in range(7)])
        short_key = base64.b32encode(xored).decode('utf-8').rstrip('=')
        
        return f"{short_key[:4]}-{short_key[4:8]}-{short_key[8:]}"
    except Exception as e:
        return f"[!] LỖI HỆ THỐNG PDF: {str(e)}"

# ==============================================================================
# LÕI THUẬT TOÁN 2: YOUTUBE DOWNLOADER
# ==============================================================================
SECRET_SALT_PRO_YT = "NTS_SECRET_SUPER_SALT_999999_PRO_2026"
SECRET_SALT_STD_YT = "NTS_SECRET_SUPER_SALT_999999_STD_2026"

def generate_youtube_key(hwid, expiry_date, package="1"):
    hwid = hwid.strip().upper()
    if isinstance(expiry_date, datetime):
        expiry_date = expiry_date.strftime("%Y%m%d")
    else:
        if "-" in expiry_date:
            expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").strftime("%Y%m%d")
        elif "/" in expiry_date:
            expiry_date = datetime.strptime(expiry_date, "%d/%m/%Y").strftime("%Y%m%d")

    active_salt = SECRET_SALT_PRO_YT if str(package) == "2" else SECRET_SALT_STD_YT
    raw_str = f"{hwid}{expiry_date}{active_salt}"
    return hashlib.sha256(raw_str.encode()).hexdigest()[:20].upper()

# ==============================================================================
# LÕI THUẬT TOÁN 3: TIKTOK NO-WATERMARK
# ==============================================================================
SECRET_SALT_TIKTOK = "NTS_100_TY_PRO_MAX_WHITEHAT_2026_@#$%"

def generate_tiktok_key(hwid, expiry_date, *args):
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
        raw_data = f"{hwid}|{expiry_date}|{SECRET_SALT_TIKTOK}"
        signature = hashlib.sha256(raw_data.encode()).hexdigest()
        final_key_raw = f"{expiry_date}|{signature}"
        final_key = base64.b64encode(final_key_raw.encode()).decode()
        return final_key
    except Exception as e:
        return f"❌ LỖI HỆ THỐNG TIKTOK: {str(e)}"

# ==============================================================================
# XÂY DỰNG GIAO DIỆN CHIA TAB
# ==============================================================================
tab_pdf, tab_yt, tab_tiktok = st.tabs(["📄 GHOST HACK PDF", "🎥 YOUTUBE VIP", "🎵 TIKTOK NO-LOGO"])

# -----------------------------------
# TAB 1: PDF MASTER
# -----------------------------------
with tab_pdf:
    st.subheader("Trạm cấp Key PDF Master")
    hwid_pdf = st.text_input("Mã HWID (Khách gửi):", key="hwid_pdf").strip()
    date_pdf = st.date_input("Ngày hết hạn:", key="date_pdf")
    pkg_pdf = st.radio("Chọn gói kích hoạt:", ["Bản THƯỜNG (Giới hạn 32MB)", "Bản PRO VIP (Không giới hạn)"], key="pkg_pdf")
    
    if st.button("🚀 ĐÚC KEY PDF", type="primary", use_container_width=True):
        if not hwid_pdf:
            st.error("Chưa nhập HWID kìa sếp!")
        else:
            is_pro = True if "PRO" in pkg_pdf else False
            # Chuyển đổi datetime object sang string dd/mm/yyyy chuẩn của lõi PDF
            date_str_pdf = date_pdf.strftime("%d/%m/%Y") 
            key_result = generate_pdf_key(hwid_pdf, date_str_pdf, is_pro)
            
            st.success("✅ ĐÚC KEY THÀNH CÔNG!")
            st.info("Copy mã bên dưới gửi cho khách:")
            st.code(key_result, language="text")

# -----------------------------------
# TAB 2: YOUTUBE DOWNLOADER
# -----------------------------------
with tab_yt:
    st.subheader("Trạm cấp Key YouTube Downloader")
    hwid_yt = st.text_input("Mã HWID (Khách gửi):", key="hwid_yt").strip()
    date_yt = st.date_input("Ngày hết hạn:", key="date_yt")
    pkg_yt = st.radio("Chọn gói kích hoạt:", ["1. Bản Thường (29k / Tải YT thường)", "2. Bản PRO VIP (Bypass Video Hội Viên)"], key="pkg_yt")
    
    if st.button("🚀 ĐÚC KEY YOUTUBE", type="primary", use_container_width=True):
        if not hwid_yt:
            st.error("Chưa nhập HWID kìa sếp!")
        else:
            package_val = "2" if "PRO" in pkg_yt else "1"
            date_str_yt = date_yt.strftime("%Y-%m-%d")
            key_result = generate_youtube_key(hwid_yt, date_str_yt, package_val)
            
            st.success("✅ ĐÚC KEY THÀNH CÔNG!")
            st.info("Copy mã bên dưới gửi cho khách:")
            st.code(key_result, language="text")

# -----------------------------------
# TAB 3: TIKTOK NO-WATERMARK
# -----------------------------------
with tab_tiktok:
    st.subheader("Trạm cấp Key TikTok No-Logo")
    hwid_tt = st.text_input("Mã HWID (Khách gửi):", key="hwid_tt").strip()
    date_tt = st.date_input("Ngày hết hạn:", key="date_tt")
    
    if st.button("🚀 ĐÚC KEY TIKTOK", type="primary", use_container_width=True):
        if not hwid_tt:
            st.error("Chưa nhập HWID kìa sếp!")
        else:
            # Thuật toán TikTok bắt buộc format YYYY-MM-DD
            date_str_tt = date_tt.strftime("%Y-%m-%d")
            key_result = generate_tiktok_key(hwid_tt, date_str_tt)
            
            st.success("✅ ĐÚC KEY THÀNH CÔNG!")
            st.info("Copy mã bên dưới gửi cho khách:")
            st.code(key_result, language="text")

# Footer
st.markdown("<br><hr><p style='text-align: center; color: gray; font-size: 12px;'>© 2026 NTS Studio. All rights reserved.</p>", unsafe_allow_html=True)
