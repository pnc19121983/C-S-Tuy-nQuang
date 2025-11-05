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
- [Chatbot tạo ảnh thẻ học sinh](https://aistudio.google.com/apps/drive/1NUTm0yDHEX4lBsAM293OEyfmHUWuPC-I?fbclid=IwY2xjawNEQJ9leHRuA2FlbQIxMABicmlkETEydk5Cang3OTV5Z3dpVmY1AR6VWBt4USB3U-0NvSIalXphIIrsx35xhUUow7PvKQqt8CbKZIX8fxsjR9YU-Q_aem_ob-7SpkS3ApWSvmMUoDDQA&showPreview=true&showAssistant=true)
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
    - [ Ứng dụng tạo tranh tô màu cho các bé mầm non](https://aistudio.google.com/apps/drive/1Lz7TqbLl5bE60nm7fPd7Y-049t860odR?showPreview=true&showAssistant=true)
    - [STEAM 5E: Khám phá bắp ngô](https://www.youtube.com/watch?v=T8JbMQyKV-U)
    - [Chuyện Bé cho gà ăn GV Khúc Thị Ngọc Lan](https://www.youtube.com/watch?v=V00c-tBr2qM&feature=youtu.be)
    - [Kể truyện "Nhổ củ cải" (Cô giáo Nguyễn Thị Hoa Nhài)](https://www.youtube.com/watch?v=e-IVv86g3dw)  
    - [Giới thiệu chữ cái o, ô, ơ Lớp 5 6 tuổi](https://www.youtube.com/watch?v=XkCZsT-t888&feature=youtu.be)   
    - [Hoạt động Tạo hình ngôi nhà_GV Chu Thị Duyên](http://c0huongsen.tuyenquang.edu.vn/thu-vien/video-clip/hoat-dong-tao-hinh-ngoi-nha_gv-chu-thi-duyen.html?categoryId=3017781&gidzl=tnpEPDdn7nJM1iXYtkqT5jO6o6F6kqr7cbQSOC7jJKJALvbdpByTGyLGoJkPl1nBn5VECZO-sUP1q_GV50)                                      
    - [THƠ MÈO ĐI CÂU CÁ_GV NGUYỄN MINH NGUYỆT](https://www.youtube.com/watch?v=WTXx9jhEZUM&feature=youtu.be) 
    - [Trò chơi với các hình học lớp 3 4 tuổi](https://www.youtube.com/watch?v=QJRWyANaWC0) 
    - [Bài hát: Múa cho mẹ xem_GV Nguyễn Thị Ngọc](https://www.youtube.com/watch?v=qxO3fr2ySV0&feature=youtu.be)     
    - [Bài thơ Vì con_ GV Trần Thị Hảo](https://www.youtube.com/watch?v=2hQnLMEtpOw&feature=youtu.be) 
    - [Truyện Bác cấp dưỡng](https://www.youtube.com/watch?v=86UMsll7R_w)   
    - [Truyện Chiếc xe ô tô màu đỏ của bé Minh](https://www.youtube.com/watch?v=mj0sm08ZcIc) 
    - [Dạy trẻ kỹ năng rửa tay 6 bước](https://www.youtube.com/watch?si=b9nYuKvl1od5FiPc&v=TRSOMOfgr04&feature=youtu.be) 
    - [Gây hứng thú để tìm chữ cái đã học](https://www.youtube.com/watch?si=El9RVlmWqYsklSsS&v=osMd0LEOxXQ&feature=youtu.be) 
    - [Khám phá 1 số đồ dùng trong gia đình](https://www.youtube.com/watch?si=xqhmctr_R51nnUMK&v=H03Z-jApyZs&feature=youtu.be) 
    - [Trường Mầm non Phú Lâm](https://github.com/mamnonphulam/PhuLam-school/issues?q=is%3Aissue%20state%3Aopen%20author%3Amamnonphulam) 
    - [Chủ đề: Đồ dùng đồ chơi yêu thích của bé (ô tô, quả bóng, búp bê)](https://www.youtube.com/watch?v=w89DgVvUaGM) 
    - [KPKH: Ích lợi của các nhóm thực phẩm đối với cơ thể ( Chất bột đường, chất béo)](https://youtu.be/NuA_nrNARFI) 
    - [KPKH: Ích lợi của các nhóm thực phẩm đối với cơ thể (Chất đạm, vitamin và khoáng chất)](https://youtu.be/I5hCvGIeZLE) 
    """)

elif selected == "th":
    st.header("📘 Dạy học cấp Tiểu học")
    st.markdown("""
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Toán](https://chatgpt.com/g/g-68217174ce408191b372e097cbb90c98-tq-toan-tieuhoc) 
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Tin học](https://chatgpt.com/g/g-684782cf55cc8191a6d81a16827294d0-tq-tin-hoc-tieu-hoc) 
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Lịch sử - Địa lí](https://chatgpt.com/g/g-683c1a3e83c88191ad0808c492d14c71-lich-su-dia-ly) 
    - [Chuyển hình ảnh trong SGK thành video ](https://www.canva.com/design/DAGz5uviiso/tWWO8PeFqlOTBB_-ijTjfQ/edit) 
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Toán lớp 4](https://chatgpt.com/g/g-68ca708d8c0881919e6c6334d0c21320-tao-de-kiem-tra-mon-toan-lop-4) 
    - [Chatbot hỗ trợ tạo đề kiểm tra định kì môn Toán lớp 5](https://chatgpt.com/g/g-68cc9cceed888191be2ee01f2910ba3c-tao-de-kiem-tra-mon-toan-lop-5) 
    - [Trò chơi học tập trên nền tảng Canva](https://gameosomayman.my.canva.site/dagxlvtfz-o) 
    - [Xây dựng bộ trò chơi khởi động các môn học bằng AI](https://drive.google.com/file/d/1Z1zd4gKtpeR_AKrFsUDStCfv8NSJmv3K/view) 
    - [Chatbot hỗ trợ xây dựng KHBG Tin học](https://chatgpt.com/g/g-68ca911197008191bac90cdba85f593f-tro-ly-soan-khbd-mon-tin-hoc-tieu-hoc) 
    - [Chatbot hỗ trợ xây dựng KHBG Âm nhạc](https://gemini.google.com/gem/df4aa386946f?usp=sharing) 
    """)

elif selected == "thcs":
    st.header("📙 Dạy học cấp THCS")
    st.markdown("""
    - [iTeX: Phần mềm tự động tạo câu hỏi ngẫu nhiên môn Toán](https://www.youtube.com/@iTeX-Teams)  
    - [Tạo bảng theo dõi thi đua học sinh bằng AI ](https://docs.google.com/document/d/1nD1kp53I18KCCrhS1CHHMTlx2m66iQ8MtxX4fzIy7nQ/edit?usp=drive_link)  
    - [Hướng dẫn tạo slide bài giảng tự động bằng Gamma AI](https://drive.google.com/file/d/1vOjJZPHGzg4V67WJ27EM2EwEULGNKqnd/view) 
    - [Ứng dụng AI trong soạn bài và thiết kế nội dung học tập](https://docs.google.com/document/d/1oZwYV21kgAuw5ufkrNJrzkV2_NdQvPyQ/edit) 
    - [Hướng dẫn tạo Trợ lý AI tự động hóa bài soạn trên Gemini](https://docs.google.com/document/d/1bfJZauJgjGoTBvZ7wW0CQrCdn2qgX-vK/edit#heading=h.gj56e8mcine0) 
    - [Hướng dẫn tạo Chatbot hỗ trợ xây dựng kế hoạch bài dạy môn ngữ văn 8](https://docs.google.com/document/d/1H4ZsYL9qaBgmNlCkB4Ec0E8a8YglDQeHlZ83B6x9sNE/edit?tab=t.0) 
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
    - [Hướng dẫn sử dụng Google AI Studio trong soạn và thiết kế nội dung học tập](https://drive.google.com/file/d/1EiJX-Gt1o0fTY4UHgBEx63h8fHgtjyWp/view) 
    - [Tài liệu hướng dẫn khai thác và ứng dụng NotebookLM ](https://docs.google.com/document/d/1LQdDnU_jhZ2SPy-NitOlYEugZSJzytFs/edit) 
    """)

elif selected is None:
    st.info("🎈 Hãy chọn một mục ở trên để xem nội dung chi tiết.")
