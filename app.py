import streamlit as st

st.set_page_config(page_title="SẢN PHẨM ỨNG DỤNG KHCN & CĐS", layout="wide")

# Căn logo và tiêu đề trên cùng một dòng
col1, col2 = st.columns([1, 10])

with col1:
    st.image("logo.png", width=100)  # logo nằm cùng thư mục với app.py

with col2:
    st.markdown("## 📚 SẢN PHẨM ỨNG DỤNG KHCN & CĐS")
    st.markdown("Nền tảng chia sẻ học liệu phục vụ công tác **quản trị và giảng dạy** các cấp học.")



# Danh sách các mục và icon
items = [
    {"key": "dungchung", "label": "Sản phẩm dùng chung", "icon": "🗂️"},
    {"key": "quantri", "label": "Quản trị nhà trường", "icon": "🏫"},
    {"key": "mn", "label": "Dạy học Mầm non", "icon": "🧸"},
    {"key": "th", "label": "Dạy học Tiểu học", "icon": "📘"},
    {"key": "thcs", "label": "Dạy học THCS", "icon": "📙"},
    {"key": "thpt", "label": "Dạy học THPT", "icon": "📕"},
]

# Biến lưu lựa chọn
if "selected" not in st.session_state:
    st.session_state.selected = None

# Tạo layout dạng lưới 2 hàng x 3 cột
for i in range(0, len(items), 3):
    cols = st.columns(3)
    for j, item in enumerate(items[i:i+3]):
        with cols[j]:
            # Nút duy nhất có icon + tên
            if st.button(f"{item['icon']}  {item['label']}", key=item["key"]):
                st.session_state.selected = item["key"]

# Nội dung hiển thị theo lựa chọn
selected = st.session_state.selected

if selected == "dungchung":
    st.header("🗂️ Sản phẩm dùng chung")
    st.markdown("""
- [Chatbot: Tìm hiểu các Thông tư 09, 10, 11, 12, 13/2025 của Bộ GDĐT](https://chatgpt.com/g/g-687f7c5a432081919eb9bbec42354b31-tim-hieu-thong-tu-09-10-11-12-13-2025-cua-bo-gddt)
- [Tài liệu hướng dẫn giáo viên tích hợp sử dụng AI trong dạy học](https://byvn.net/pqqR) 
- [Video bài giảng “Làm chủ AI - Trở thành Super Teacher” do Đại học Bách khoa Hà Nội và Công ty TNHH STEAM for Vietnam đồng tổ chức](https://www.youtube.com/watch?v=5l4Uis5xzvc)                 
- [Ứng dụng AI trong tạo ảnh và video bài giảng](https://www.youtube.com/watch?v=uQ6URlXLGQA&list=PLKJ7b9uOx27YrBfRzC-Wz6GpvVmZlI-hz&index=4) 
- [Ứng dụng AI trong giảng dạy Đại học RMIT](https://www.youtube.com/watch?v=4f0kIVRZVn0&t=4950s) 
- [Ứng dụng AI trong thiết kế bài giảng STEM](https://www.youtube.com/watch?v=R53xuJG5xkk) 
""")


elif selected == "quantri":
    st.header("🏫 Sản phẩm quản trị nhà trường")
    cap = st.selectbox("🔽 Chọn cấp học", ["Mầm non", "Tiểu học", "THCS", "THPT"])
    if cap == "Mầm non":
        st.markdown("- ..........\n- ..........\n- ..........")
    elif cap == "Tiểu học":
        st.markdown("- ..........\n- ..........\n- ..........")
    elif cap == "THCS":
        st.markdown("- ..........\n- ..........\n- ..........")
    elif cap == "THPT":
        st.markdown("- ..........\n- ..........\n- ..........")

elif selected == "mn":
    st.header("🧸 Dạy học cấp Mầm non")
    st.markdown("""
    - ..........  
    - ..........
    - ..........  
    - ..........
    """)

elif selected == "th":
    st.header("📘 Dạy học cấp Tiểu học")
    st.markdown("""
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Toán](https://chatgpt.com/g/g-68217174ce408191b372e097cbb90c98-tq-toan-tieuhoc) 
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Tin học](https://chatgpt.com/g/g-684782cf55cc8191a6d81a16827294d0-tq-tin-hoc-tieu-hoc) 
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Lịch sử - Địa lí](https://chatgpt.com/g/g-683c1a3e83c88191ad0808c492d14c71-lich-su-dia-ly) 
    """)

elif selected == "thcs":
    st.header("📙 Dạy học cấp THCS")
    st.markdown("""
    - [iTeX: Phần mềm tự động tạo câu hỏi ngẫu nhiên môn Toán](https://www.youtube.com/@iTeX-Teams)  
    - ..........
    - ..........  
    - .......... 
    """)

elif selected == "thpt":
    st.header("📕 Dạy học cấp THPT")
    st.markdown("""
    - [iTeX: Phần mềm tự động tạo câu hỏi ngẫu nhiên môn Toán](https://www.youtube.com/@iTeX-Teams)  
    - ..........
    - ..........  
    - ..........  
    """)

elif selected is None:
    st.info("🎈 Hãy chọn một mục ở trên để xem nội dung chi tiết.")
