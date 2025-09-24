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
- [Vận dụng AI và sử dụng đồ dùng dạy học, học liệu để xây dựng kế hoạch giáo dục STEM](https://www.youtube.com/watch?v=LeWe0b23CCg) 
- [Prompt cơ bản cho người mới bắt đầu](https://docs.google.com/document/d/1qsz5tPttuDXoNSgzsyZ8sJhqTFZ-Vndd/edit?usp=drive_link&ouid=101989985365170136492&rtpof=true&sd=true) 
- [Hướng dẫn xuất file word không bị lỗi công thức toán](https://drive.google.com/file/d/1VDJX4O23MgZNZ96N1ewXQQqaqm_Ae1ke/view?usp=sharing) 
- [Hướng dẫn Tạo trò chơi củng cố kiến thức sau mỗi bài học](https://docs.google.com/document/d/1rk5SKak_MKnhiJ95rY9kJ5R-z_0ZWdMP/edit?usp=sharing&ouid=101989985365170136492&rtpof=true&sd=true) 
- [Tạo hình 3D có thể zoom, xoay](https://drive.google.com/file/d/1Besc2TaKXbExLphq8QGRwjMfzESblTK3/view?usp=drive_link) 
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
    - [Chatbot: Cô giáo mầm non](https://notebooklm.google.com/notebook/44149ea2-baf4-468b-8f70-fcdc48cd407c)  
    - [Chatbot: Hiệu trưởng mầm non](https://notebooklm.google.com/notebook/72ffe0d3-88cd-4eec-8758-dde7b112393b) 
    - [Chatbot: Trợ lý phương pháp dạy học](https://chatgpt.com/g/g-68479847d1a08191aeda9b517a389605-tro-ly-ve-phuong-phap-day-hoc)  
    - [Chatbot: Trợ lý soạn thảo văn bản](https://chatgpt.com/g/g-6846ecf00fac8191b427451f7e55437e-tro-ly-soan-thao-van-ban) 
    - [Kỹ năng chung tay bảo vệ môi trường](https://www.youtube.com/watch?v=OAi-52MPGN4&feature=youtu.be) 
    - [Kỹ năng Dũng cảm nói ra sự thật](https://www.youtube.com/watch?v=aEhupj_3KYk) 
    - [Làm quen chũ cái o](https://www.youtube.com/watch?v=KRx1IubT2_Y&pp=0gcJCa0JAYcqIYzv)      
    - [Thơ Dán hoa tặng mẹ](https://github.com/mamnonphulam/PhuLam-school/issues/6)  
    - [Thơ Bác Bầu bác Bí](https://github.com/mamnonphulam/PhuLam-school/issues/5)     
    - [Thơ Thăm nhà bà](https://github.com/mamnonphulam/PhuLam-school/issues/4)       
    - [Thơ Xe chữa cháy](https://github.com/mamnonphulam/PhuLam-school/issues/3)    
    - [Thơ em yêu nhà em](https://github.com/mamnonphulam/PhuLam-school/issues/2)  
    - [Bài thơ Đi dép](https://github.com/mamnonphulam/PhuLam-school/issues/12)    
    - [Bài thơ Cây bắp cải](https://github.com/mamnonphulam/PhuLam-school/issues/15)      
    - [Chào mừng nhóm 13-24 tháng tuổi](https://github.com/mamnonphulam/PhuLam-school/issues/19)    
    - [Truyện Cây táo](https://github.com/mamnonphulam/PhuLam-school/issues/21)   
    - [Truyện Quả trứng](https://github.com/mamnonphulam/PhuLam-school/issues/22)   
    - [Làm quen chữ cái e ê](https://github.com/mamnonphulam/PhuLam-school/issues/23)     
    - [Truyện Gấu con bị đau răng](https://github.com/mamnonphulam/PhuLam-school/issues/26)     
    - [Bài thơ Bạn mới](https://github.com/mamnonphulam/PhuLam-school/issues/27)     
    - [Truyện Ba từ kỳ diệu của Sóc nhí](https://github.com/mamnonphulam/PhuLam-school/issues/28)    
    - [Truyện Ai cũng được chơi cùng](https://github.com/mamnonphulam/PhuLam-school/issues/29)     
    - [Truyện Chú sâu háu ăn](https://www.youtube.com/watch?v=dqYmF225Fcc)   
    - [Truyện Cáo Thỏ Gà Trồng](https://www.youtube.com/watch?v=HVChdIfZjM4)    
    - [Truyện: Khu rừng bí ẩn](https://www.youtube.com/watch?v=J7BeWvyfLg0)  
    - [Truyện: Củ cải trắng](https://www.youtube.com/watch?v=XuZ33VmTpX8&feature=youtu.be)     
    - [Nhận biết khối cầu khối trụ](https://www.youtube.com/watch?v=66yuakIlb8M)  
    - [Cấu tạo chữ e](https://www.youtube.com/watch?v=vocVe6e9wjc)   
    - [Vòng đời của loài bướm](https://www.youtube.com/watch?v=AtQeLaNDH3M)         
    - [Phân biệt màu sắc toán](https://www.youtube.com/watch?v=MoeS33c8lyA)  
    - [Bài hát chữ cái k](https://www.youtube.com/watch?v=qjLrMeimcWw) 
    - [Bài hát số 8](https://www.youtube.com/watch?v=-Jd8_NgP6Xs&feature=youtu.be) 
    - [Bài thơ Cây đào](https://www.youtube.com/watch?v=SUFIGLl-9w8&feature=youtu.be) 
    - [Bài thơ Em yêu nhà em](https://www.youtube.com/watch?v=lsXge2TJHUk&feature=youtu.be) 
    - [Truyện Cây táo](https://www.youtube.com/watch?v=Rih8HJPESQo) 
    - [Truyện Chị ong nâu và em bé](https://www.youtube.com/watch?v=XNDqa4dBZq8)
    - [Vòng đời của loài bướm](https://www.youtube.com/watch?v=stWCR1IyPEc)
    - [Bài thơ chữ cái o, ô, ơ](https://www.youtube.com/watch?v=c-o-iGx8sA8)
    - [Bài thơ chữ cái a, ă, â](https://www.youtube.com/watch?v=wueSb9hTvro)
    - [Truyện: Chú cuội và cây đa trên cung trăng](https://www.youtube.com/watch?v=PqOnnMh1ep8)
    - [Truyện: Chuyến du lịch của chú gà trống choai](https://www.youtube.com/watch?v=8Kf3H1EjuFg)
    - [Giáo dục trẻ niềm tự hào dân tộc](https://www.youtube.com/watch?v=lR7RjLS8jvI)
    - [Bài thơ: Đồ dùng của bé](https://www.youtube.com/watch?v=FyP0R4vvLnE)
    - [Bài thơ: Lễ hội Thành tuyên](https://www.youtube.com/watch?v=toQvGPcihx8)
    - [Bài thơ: Rong và cá](https://www.youtube.com/watch?v=CeiKsIic4aI)
    - [Truyện: Quả thị](https://www.youtube.com/watch?v=raQXtwuv1Fk)
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
    - [Chatbot: Học sinh giỏi môn Tin học](https://chatgpt.com/g/g-688b68637db88191a7537adc8b4fe755-tro-ly-tin-hoc-hsg)  
    - [Chatbot: Học sinh giỏi môn Hóa học](https://chatgpt.com/g/g-688c16e1f338819198735dbadab0bb0b-tro-ly-hoa-hoc-chuyen-sau)   
    - [Chatbot: Học sinh giỏi môn Toán](https://chatgpt.com/g/g-688c7ff0165081919d6ebf35f7c7540b-on-luyen-hoc-sinh-gioi-quoc-gia-toan)    
    - [Chatbot: Học sinh giỏi môn Vật lí](https://chatgpt.com/g/g-688c88527ff081918a9a747c0597212f-tro-ly-vat-ly-chuyen-sau-bdhsgqg)  
    - [Chatbot: Học sinh giỏi môn Sinh học](https://chatgpt.com/g/g-688c894c97b48191bca4aaf2aef38510-sinh-hoc-hsg-quoc-gia-ai-tutor) 
    """)

elif selected is None:
    st.info("🎈 Hãy chọn một mục ở trên để xem nội dung chi tiết.")
