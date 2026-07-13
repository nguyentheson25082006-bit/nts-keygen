import streamlit as st
import hashlib
import base64
from datetime import datetime, timedelta

# =====================================================================
# CONFIG GIAO DIỆN CYBERPUNK (RED TEAM STYLE)
# =====================================================================
st.set_page_config(page_title="NTS KEYGEN CENTER", page_icon="🔥", layout="centered")

st.markdown("""
<style>
    .main-title { font-size: 3em; font-weight: 900; color: #38bdf8; text-align: center; text-transform: uppercase; text-shadow: 0 0 10px rgba(56, 189, 248, 0.5); }
    .sub-title { text-align: center; color: #94a3b8; font-size: 1.2em; margin-bottom: 30px; font-weight: 600; }
    .key-box { background-color: #111827; border: 1px solid #f59e0b; padding: 20px; border-radius: 10px; text-align: center; }
    .key-text { color: #f59e0b; font-size: 1.5em; font-weight: 900; letter-spacing: 2px; }
    div[data-baseweb="select"] > div { background-color: #1e293b; color: white; border: 1px solid #38bdf8; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
# LÕI 1: GHOST_HACK - HYBRID KEY GENERATOR V2.1 (TỪ SOURCE 3)
# =====================================================================
MASTER_KEY = "GHOST_HACK_NTS_9999"

def get_hybrid_key(hwid: str, expiry_date: str, is_pro: bool = False):
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
        
        keystream = hashlib.md5((hwid + MASTER_KEY).encode('utf-8')).digest()
        xored = bytes([raw_bytes[i] ^ keystream[i] for i in range(7)])
        short_key = base64.b32encode(xored).decode('utf-8').rstrip('=')
        
        return f"{short_key[:4]}-{short_key[4:8]}-{short_key[8:]}"
    except ValueError:
        return "❌ LỖI: Định dạng ngày không hợp lệ! Hãy nhập (dd/mm/yy) hoặc (dd/mm/yyyy)"
    except Exception as e:
        return f"❌ LỖI HỆ THỐNG: {str(e)}"

# =====================================================================
# LÕI 2: NTS ADMIN KEYGEN - MÁY IN TIỀN V1.0 (TỪ SOURCE 4)
# =====================================================================
class NTS_Admin_Forge:
    def __init__(self):
        self.secret_salt = "NTS_JOKER_SMILE_100B"

    def create_payload_string(self, hwid, plan, compact_date):
        return f"{hwid}|{plan}|{compact_date}|{self.secret_salt}"

    def forge_key(self, hwid, plan_choice, days_valid):
        try:
            hwid = hwid.strip().upper()
            exp_date = datetime.now() + timedelta(days=days_valid)
            compact_date = exp_date.strftime("%y%m%d")
            
            plan = "VIP" if plan_choice == 1 else "STANDARD"
            
            raw_payload = self.create_payload_string(hwid, plan, compact_date)
            encoded_payload = raw_payload.encode('utf-8')
            
            signature = hashlib.sha256(encoded_payload).hexdigest().upper()[:8]
            final_key = f"{plan}-{signature}-{compact_date}"
            
            return True, final_key, exp_date.strftime("%Y-%m-%d")
        except Exception as e:
            return False, str(e), None

# =====================================================================
# LÕI 3: THUẬT TOÁN TIKTOK NO-WATERMARK (TỪ SOURCE 5)
# =====================================================================
SECRET_SALT_TIKTOK = "NTS_100_TY_PRO_MAX_WHITEHAT_2026_@#$%"

def get_tiktok_key(hwid, expiry_date, *args):
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
        raw_data = f"{hwid}|{expiry_date}|{SECRET_SALT_TIKTOK}"
        signature = hashlib.sha256(raw_data.encode()).hexdigest()
        final_key_raw = f"{expiry_date}|{signature}"
        final_key = base64.b64encode(final_key_raw.encode()).decode()
        return final_key
    except ValueError:
        return "❌ LỖI ĐỊNH DẠNG: Yêu cầu ngày nhập kiểu YYYY-MM-DD (Ví dụ: 2026-08-30)"
    except Exception as e:
        return f"❌ LỖI HỆ THỐNG: {str(e)}"

# =====================================================================
# XÂY DỰNG GIAO DIỆN ĐIỀU KHIỂN
# =====================================================================
st.markdown("<div class='main-title'>NTS KEYGEN DASHBOARD</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Hệ thống đúc khóa bản quyền tập trung - Phân quyền tối cao</div>", unsafe_allow_html=True)

# Menu bẻ nhánh hiển thị hệ thống đúc Key
tool_choice = st.selectbox(
    "🔥 LỰA CHỌN CỖ MÁY IN TIỀN:", 
    ["1. NTS YouTube & General (Admin Forge V1.0)", 
     "2. Hệ thống Hybrid V2.1 (Bản cũ Fix)", 
     "3. TikTok No-Watermark Core"]
)

st.markdown("---")

# ---------------------------------------------------------------------
# GIAO DIỆN 1: ADMIN FORGE V1.0 (YouTube & General)
# ---------------------------------------------------------------------
if "Admin Forge V1.0" in tool_choice:
    st.subheader("🛠️ CẤU HÌNH YOUTUBE / APP V6.0")
    hwid_in = st.text_input("💻 Nhập Mã HWID của khách:")
    
    col1, col2 = st.columns(2)
    with col1:
        plan_str = st.radio("👑 Chọn Gói Cấp Phép:", ["VIP Premium (Mở khóa toàn bộ)", "STANDARD (Giới hạn)"])
        plan_code = 1 if "VIP" in plan_str else 2
    with col2:
        days_in = st.number_input("⏳ Số ngày sử dụng (Ví dụ: 30, 365):", min_value=1, value=30, step=1)
        
    if st.button("🚀 ĐÚC KEY NGAY", type="primary", use_container_width=True):
        if not hwid_in:
            st.error("Chưa nhập HWID kìa sếp ơi!")
        else:
            forge = NTS_Admin_Forge()
            success, key_out, real_date = forge.forge_key(hwid_in, plan_code, days_in)
            if success:
                st.success("✅ ĐÚC KEY THÀNH CÔNG! LƯỢM LÚA THÔI SẾP!")
                st.info(f"Ngày hết hạn thực tế: **{real_date}**")
                st.markdown(f"<div class='key-box'>🔑 BẢN QUYỀN KHÁCH HÀNG:<br><br><span class='key-text'>{key_out}</span></div>", unsafe_allow_html=True)
            else:
                st.error(f"LỖI: {key_out}")

# ---------------------------------------------------------------------
# GIAO DIỆN 2: HYBRID V2.1
# ---------------------------------------------------------------------
elif "Hybrid V2.1" in tool_choice:
    st.subheader("🛠️ CẤU HÌNH HYBRID TOOL")
    hwid_in = st.text_input("💻 Nhập Mã HWID của khách:")
    
    col1, col2 = st.columns(2)
    with col1:
        date_in = st.text_input("📅 Ngày hết hạn (VD: 01/02/2026):", placeholder="dd/mm/yyyy")
    with col2:
        is_pro = st.toggle("Kích hoạt bản PRO (Không giới hạn)")
        
    if st.button("🚀 ĐÚC KEY NGAY", type="primary", use_container_width=True):
        if not hwid_in or not date_in:
            st.error("Nhập thiếu dữ liệu rồi sếp!")
        else:
            key_out = get_hybrid_key(hwid_in, date_in, is_pro)
            if "❌" in key_out:
                st.error(key_out)
            else:
                st.success(f"✅ ĐÚC KEY BẢN [{'PRO VIP' if is_pro else 'THƯỜNG'}] THÀNH CÔNG!")
                st.markdown(f"<div class='key-box'>🔑 BẢN QUYỀN KHÁCH HÀNG:<br><br><span class='key-text'>{key_out}</span></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# GIAO DIỆN 3: TIKTOK NO-WATERMARK
# ---------------------------------------------------------------------
elif "TikTok" in tool_choice:
    st.subheader("🛠️ CẤU HÌNH TIKTOK CORE")
    hwid_in = st.text_input("💻 Nhập Mã HWID của khách:")
    date_in = st.text_input("📅 Ngày hết hạn (Bắt buộc format YYYY-MM-DD):", placeholder="2026-08-30")
    
    if st.button("🚀 ĐÚC KEY NGAY", type="primary", use_container_width=True):
        if not hwid_in or not date_in:
            st.error("Nhập thiếu dữ liệu kìa sếp!")
        else:
            key_out = get_tiktok_key(hwid_in, date_in)
            if "❌" in key_out:
                st.error(key_out)
            else:
                st.success("✅ ĐÚC KEY TIKTOK THÀNH CÔNG! ĐÃ MÃ HÓA BASE64.")
                st.markdown(f"<div class='key-box'>🔑 BẢN QUYỀN KHÁCH HÀNG:<br><br><span class='key-text' style='word-wrap: break-word;'>{key_out}</span></div>", unsafe_allow_html=True)
