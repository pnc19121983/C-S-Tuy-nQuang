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

    # Danh sách các liên kết được chuyển đổi sang định dạng Python kèm icon
    dungchung_links = [
        {"icon": "▶️", "label": "Chatbot: Tìm hiểu các Thông tư 09-13/2025", "url": "https://chatgpt.com/g/g-687f7c5a432081919eb9bbec42354b31-tim-hieu-thong-tu-09-10-11-12-13-2025-cua-bo-gddt"},
        {"icon": "📁", "label": "Tài liệu hướng dẫn GV tích hợp AI", "url": "https://byvn.net/pqqR"},
        {"icon": "▶️", "label": "Video bài giảng “Làm chủ AI - Super Teacher”", "url": "https://www.youtube.com/watch?v=5l4Uis5xzvc"},
        {"icon": "▶️", "label": "Ứng dụng AI tạo ảnh và video bài giảng", "url": "https://www.youtube.com/watch?v=uQ6URlXLGQA&list=PLKJ7b9uOx27YrBfRzC-Wz6GpvVmZlI-hz&index=4"},
        {"icon": "▶️", "label": "Ứng dụng AI trong giảng dạy Đại học RMIT", "url": "https://www.youtube.com/watch?v=4f0kIVRZVn0&t=4950s"},
        {"icon": "▶️", "label": "Ứng dụng AI trong thiết kế bài giảng STEM", "url": "https://www.youtube.com/watch?v=R53xuJG5xkk"},
        {"icon": "▶️", "label": "Vận dụng AI xây dựng kế hoạch giáo dục STEM", "url": "https://www.youtube.com/watch?v=LeWe0b23CCg"},
        {"icon": "📁", "label": "Prompt cơ bản cho người mới bắt đầu (Google Docs)", "url": "https://docs.google.com/document/d/1qsz5tPttuDXoNSgzsyZ8sJhqTFZ-Vndd/edit?usp=drive_link&ouid=101989985365170136492&rtpof=true&sd=true"},
        {"icon": "📁", "label": "Hướng dẫn xuất file word không lỗi công thức toán", "url": "https://drive.google.com/file/d/1VDJX4O23MgZNZ96N1ewXQQqaqm_Ae1ke/view?usp=sharing"},
        {"icon": "📁", "label": "Hướng dẫn Tạo trò chơi củng cố kiến thức", "url": "https://docs.google.com/document/d/1rk5SKak_MKnhiJ95rY9kJ5R-z_0ZWdMP/edit?usp=sharing&ouid=101989985365170136492&rtpof=true&sd=true"},
        {"icon": "🌐", "label": "Tạo hình 3D có thể zoom, xoay", "url": "https://drive.google.com/file/d/1Besc2TaKXbExLphq8QGRwjMfzESblTK3/view?usp=drive_link"},
        {"icon": "▶️", "label": "Chatbot tạo ảnh thẻ học sinh", "url": "https://aistudio.google.com/apps/drive/1NUTm0yDHEX4lBsAM293OEyfmHUWuPC-I?fbclid=IwY2xjawNEQJ9leHRuA2FlbQIxMABicmlkETEydk5Cang3OTV5Z3dpVmY1AR6VWBt4USB3U-0NvSIalXphIIrsx35xhUUow7PvKQqt8CbKZIX8fxsjR9YU-Q_aem_ob-7SpkS3ApWSvmMUoDDQA&showPreview=true&showAssistant=true"},
    ]

    NUM_COLUMNS = 3  # Lưới 2 cột

    for i in range(0, len(dungchung_links), NUM_COLUMNS):
        cols = st.columns(NUM_COLUMNS)
        for j, link_item in enumerate(dungchung_links[i:i + NUM_COLUMNS]):
            with cols[j]:
                # Thêm icon vào trước tên liên kết
                st.markdown(f"* {link_item['icon']} [{link_item['label']}]({link_item['url']})")


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

    # Danh sách các liên kết được chuyển đổi sang định dạng Python kèm icon
    mn_links = [
        {"icon": "▶️", "label": "Chatbot: Cô giáo mầm non", "url": "https://notebooklm.google.com/notebook/44149ea2-baf4-468b-8f70-fcdc48cd407c"},
        {"icon": "▶️", "label": "Chatbot: Hiệu trưởng mầm non", "url": "https://notebooklm.google.com/notebook/72ffe0d3-88cd-4eec-8758-dde7b112393b"},
        {"icon": "▶️", "label": "Chatbot: Trợ lý phương pháp dạy học", "url": "https://chatgpt.com/g/g-68479847d1a08191aeda9b517a389605-tro-ly-ve-phuong-phap-day-hoc"},
        {"icon": "▶️", "label": "Chatbot: Trợ lý soạn thảo văn bản", "url": "https://chatgpt.com/g/g-6846ecf00fac8191b427451f7e55437e-tro-ly-soan-thao-van-ban"},
        {"icon": "▶️", "label": "Kỹ năng chung tay bảo vệ môi trường", "url": "https://www.youtube.com/watch?v=OAi-52MPGN4&feature=youtu.be"},
        {"icon": "▶️", "label": "Kỹ năng Dũng cảm nói ra sự thật", "url": "https://www.youtube.com/watch?v=aEhupj_3KYk"},
        {"icon": "▶️", "label": "Làm quen chũ cái o", "url": "https://www.youtube.com/watch?v=KRx1IubT2_Y&pp=0gcJCa0JAYcqIYzv"},
        {"icon": "📁", "label": "Thơ Dán hoa tặng mẹ (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/6"},
        {"icon": "📁", "label": "Thơ Bác Bầu bác Bí (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/5"},
        {"icon": "📁", "label": "Thơ Thăm nhà bà (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/4"},
        {"icon": "📁", "label": "Thơ Xe chữa cháy (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/3"},
        {"icon": "📁", "label": "Thơ em yêu nhà em (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/2"},
        {"icon": "📁", "label": "Bài thơ Đi dép (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/12"},
        {"icon": "📁", "label": "Bài thơ Cây bắp cải (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/15"},
        {"icon": "📁", "label": "Chào mừng nhóm 13-24 tháng tuổi", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/19"},
        {"icon": "📁", "label": "Truyện Cây táo (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/21"},
        {"icon": "📁", "label": "Truyện Quả trứng (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/22"},
        {"icon": "📁", "label": "Làm quen chữ cái e ê (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/23"},
        {"icon": "📁", "label": "Truyện Gấu con bị đau răng (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/26"},
        {"icon": "📁", "label": "Bài thơ Bạn mới (GitHub)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/27"},
        {"icon": "📁", "label": "Truyện Ba từ kỳ diệu của Sóc nhí", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/28"},
        {"icon": "📁", "label": "Truyện Ai cũng được chơi cùng", "url": "https://github.com/mamnonphulam/PhuLam-school/issues/29"},
        {"icon": "▶️", "label": "Truyện Chú sâu háu ăn (Video)", "url": "https://www.youtube.com/watch?v=dqYmF225Fcc"},
        {"icon": "▶️", "label": "Truyện Cáo Thỏ Gà Trồng (Video)", "url": "https://www.youtube.com/watch?v=HVChdIfZjM4"},
        {"icon": "▶️", "label": "Truyện: Khu rừng bí ẩn (Video)", "url": "https://www.youtube.com/watch?v=J7BeWvyfLg0"},
        {"icon": "▶️", "label": "Truyện: Củ cải trắng (Video)", "url": "https://www.youtube.com/watch?v=XuZ33VmTpX8&feature=youtu.be"},
        {"icon": "▶️", "label": "Nhận biết khối cầu khối trụ", "url": "https://www.youtube.com/watch?v=66yuakIlb8M"},
        {"icon": "▶️", "label": "Cấu tạo chữ e", "url": "https://www.youtube.com/watch?v=vocVe6e9wjc"},
        {"icon": "▶️", "label": "Vòng đời của loài bướm (Video 1)", "url": "https://www.youtube.com/watch?v=AtQeLaNDH3M"},
        {"icon": "▶️", "label": "Phân biệt màu sắc toán", "url": "https://www.youtube.com/watch?v=MoeS33c8lyA"},
        {"icon": "▶️", "label": "Bài hát chữ cái k", "url": "https://www.youtube.com/watch?v=qjLrMeimcWw"},
        {"icon": "▶️", "label": "Bài hát số 8", "url": "https://www.youtube.com/watch?v=-Jd8_NgP6Xs&feature=youtu.be"},
        {"icon": "▶️", "label": "Bài thơ Cây đào (Video)", "url": "https://www.youtube.com/watch?v=SUFIGLl-9w8&feature=youtu.be"},
        {"icon": "▶️", "label": "Bài thơ Em yêu nhà em (Video 1)", "url": "https://www.youtube.com/watch?v=lsXge2TJHUk&feature=youtu.be"},
        {"icon": "▶️", "label": "Truyện Cây táo (Video)", "url": "https://www.youtube.com/watch?v=Rih8HJPESQo"},
        {"icon": "▶️", "label": "Truyện Chị ong nâu và em bé", "url": "https://www.youtube.com/watch?v=XNDqa4dBZq8"},
        {"icon": "▶️", "label": "Vòng đời của loài bướm (Video 2)", "url": "https://www.youtube.com/watch?v=stWCR1IyPEc"},
        {"icon": "▶️", "label": "Bài thơ chữ cái o, ô, ơ (Video 1)", "url": "https://www.youtube.com/watch?v=c-o-iGx8sA8"},
        {"icon": "▶️", "label": "Bài thơ chữ cái a, ă, â", "url": "https://www.youtube.com/watch?v=wueSb9hTvro"},
        {"icon": "▶️", "label": "Truyện: Chú cuội và cây đa trên cung trăng", "url": "https://www.youtube.com/watch?v=PqOnnMh1ep8"},
        {"icon": "▶️", "label": "Truyện: Chuyến du lịch của chú gà trống choai", "url": "https://www.youtube.com/watch?v=8Kf3H1EjuFg"},
        {"icon": "▶️", "label": "Giáo dục trẻ niềm tự hào dân tộc", "url": "https://www.youtube.com/watch?v=lR7RjLS8jvI"},
        {"icon": "▶️", "label": "Bài thơ: Đồ dùng của bé", "url": "https://www.youtube.com/watch?v=FyP0R4vvLnE"},
        {"icon": "▶️", "label": "Bài thơ: Lễ hội Thành tuyên", "url": "https://www.youtube.com/watch?v=toQvGPcihx8"},
        {"icon": "▶️", "label": "Bài thơ: Rong và cá", "url": "https://www.youtube.com/watch?v=CeiKsIic4aI"},
        {"icon": "▶️", "label": "Truyện: Quả thị", "url": "https://www.youtube.com/watch?v=raQXtwuv1Fk"},
        {"icon": "🎨", "label": "Ứng dụng tạo tranh tô màu cho các bé", "url": "https://aistudio.google.com/apps/drive/1Lz7TqbLl5bE60nm7fPd7Y-049t860odR?showPreview=true&showAssistant=true"},
        {"icon": "▶️", "label": "STEAM 5E: Khám phá bắp ngô", "url": "https://www.youtube.com/watch?v=T8JbMQyKV-U"},
        {"icon": "▶️", "label": "Chuyện Bé cho gà ăn (GV Khúc Thị Ngọc Lan)", "url": "https://www.youtube.com/watch?v=V00c-tBr2qM&feature=youtu.be"},
        {"icon": "▶️", "label": "Kể truyện 'Nhổ củ cải' (Cô giáo Nguyễn Thị Hoa Nhài)", "url": "https://www.youtube.com/watch?v=e-IVv86g3dw"},
        {"icon": "▶️", "label": "Giới thiệu chữ cái o, ô, ơ Lớp 5 6 tuổi", "url": "https://www.youtube.com/watch?v=XkCZsT-t888&feature=youtu.be"},
        {"icon": "▶️", "label": "Hoạt động Tạo hình ngôi nhà (GV Chu Thị Duyên)", "url": "http://c0huongsen.tuyenquang.edu.vn/thu-vien/video-clip/hoat-dong-tao-hinh-ngoi-nha_gv-chu-thi-duyen.html?categoryId=3017781&gidzl=tnpEPDdn7nJM1iXYtkqT5jO6o6F6kqr7cbQSOC7jJKJALvbdpByTGyLGoJkPl1nBn5VECZO-sUP1q_GV50"},
        {"icon": "▶️", "label": "THƠ MÈO ĐI CÂU CÁ (GV NGUYỄN MINH NGUYỆT)", "url": "https://www.youtube.com/watch?v=WTXx9jhEZUM&feature=youtu.be"},
        {"icon": "▶️", "label": "Trò chơi với các hình học lớp 3 4 tuổi", "url": "https://www.youtube.com/watch?v=QJRWyANaWC0"},
        {"icon": "▶️", "label": "Bài hát: Múa cho mẹ xem (GV Nguyễn Thị Ngọc)", "url": "https://www.youtube.com/watch?v=qxO3fr2ySV0&feature=youtu.be"},
        {"icon": "▶️", "label": "Bài thơ Vì con (GV Trần Thị Hảo)", "url": "https://www.youtube.com/watch?v=2hQnLMEtpOw&feature=youtu.be"},
        {"icon": "▶️", "label": "Truyện Bác cấp dưỡng", "url": "https://www.youtube.com/watch?v=86UMsll7R_w"},
        {"icon": "▶️", "label": "Truyện Chiếc xe ô tô màu đỏ của bé Minh", "url": "https://www.youtube.com/watch?v=mj0sm08ZcIc"},
        {"icon": "▶️", "label": "Dạy trẻ kỹ năng rửa tay 6 bước", "url": "https://www.youtube.com/watch?si=b9nYuKvl1od5FiPc&v=TRSOMOfgr04&feature=youtu.be"},
        {"icon": "▶️", "label": "Gây hứng thú để tìm chữ cái đã học", "url": "https://www.youtube.com/watch?si=El9RVlmWqYsklSsS&v=osMd0LEOxXQ&feature=youtu.be"},
        {"icon": "▶️", "label": "Khám phá 1 số đồ dùng trong gia đình", "url": "https://www.youtube.com/watch?si=xqhmctr_R51nnUMK&v=H03Z-jApyZs&feature=youtu.be"},
        {"icon": "📁", "label": "Trường Mầm non Phú Lâm (GitHub Issues)", "url": "https://github.com/mamnonphulam/PhuLam-school/issues?q=is%3Aissue%20state%3Aopen%20author%3Amamnonphulam"},
        {"icon": "▶️", "label": "Chủ đề: Đồ dùng đồ chơi yêu thích của bé", "url": "https://www.youtube.com/watch?v=w89DgVvUaGM"},
        {"icon": "▶️", "label": "KPKH: Ích lợi thực phẩm (Bột đường, chất béo)", "url": "https://youtu.be/NuA_nrNARFI"},
        {"icon": "▶️", "label": "KPKH: Ích lợi thực phẩm (Chất đạm, vitamin)", "url": "https://youtu.be/I5hCvGIeZLE"},
        {"icon": "▶️", "label": "Bài thơ: Nắng bốn mùa", "url": "https://youtu.be/eT7VifAyNdw"},
        {"icon": "▶️", "label": "Múa: Mẹ yêu ơi", "url": "https://youtu.be/Q9O_M3WSekg"},
        {"icon": "▶️", "label": "Bài thơ: Cô dạy", "url": "https://youtu.be/VovjfBvq_z4"},
        {"icon": "▶️", "label": "Bài hát: Chú voi con ở bản đôn", "url": "https://youtu.be/ISjLadS-sT4"},
        {"icon": "▶️", "label": "Công tác đảm bảo bữa ăn bán trú cho trẻ Trường MN Hương Sen", "url": "https://youtu.be/BAeCvRJKFos"},
        {"icon": "▶️", "label": "Tạo hình: Nặn viên bi (25-36 tháng)", "url": "https://youtu.be/6a0sALTJjSc"},
        {"icon": "▶️", "label": "Toán: Đếm đến 2, nhận biết nhóm có 2 đối tượng, nhận biết số 2, đếm theo khả năng (4-5 tuổi)", "url": "https://youtu.be/sahLFt7J1Wg"},
        {"icon": "▶️", "label": "Kể chuyện: Bác cấp dưỡng- Nhóm trẻ 25-36 tháng", "url": "https://youtu.be/haOlNB4Nc9s"},
        {"icon": "▶️", "label": "Truyện: Mỗi người 1 việc", "url": "https://youtu.be/SbEU-KyuYsM"},
        {"icon": "▶️", "label": "Truyện: Cháu ngoan của bà", "url": "https://youtu.be/i5_oMpzMdpc"},
        {"icon": "▶️", "label": "Khám phá sự kỳ diệu của nước và giấy", "url": "https://youtu.be/hzZz5HOtNFc"},
        {"icon": "▶️", "label": "KPKH: Ích lợi của các nhóm thực phẩm đối với cơ thể (Chất đạm, vitamin và khoáng chất)", "url": "https://youtu.be/I5hCvGIeZLE"},
        {"icon": "▶️", "label": "Truyện: Thỏ con đi học", "url": "https://youtu.be/Ui3hm-Fp40g"},
        {"icon": "▶️", "label": "KPKH: Ích lợi của các nhóm thực phẩm đối với cơ thể ( Chất bột đường, chất béo)", "url": "https://youtu.be/NuA_nrNARFI"},
        {"icon": "▶️", "label": "Truyện: Chiếc ấm sành nở hoa", "url": "https://youtu.be/8Bimx01fgsA"},
        {"icon": "▶️", "label": "Tiết dạy KPXH Cảm xúc của bé - 5 tuổi - MN Hoa Phượng", "url": "https://youtu.be/0k19FbO0BBc"},
        {"icon": "▶️", "label": "Tiết dạy NBPB Màu xanh - Màu đỏ - 25-36 tháng - MN Hoa Phượng", "url": "https://youtu.be/MNVClsXYnoU"},
        {"icon": "▶️", "label": "Bải giảng Âm nhạc Gọi tên cảm xúc - 3 tuổi - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1Bim2EM0tHpNKhmFkTdxRG7UdO14aF3J7/edit?usp=sharing&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng Truyện Gấu con bị đau răng - 3 tuổi - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1Dlj4tH8BCx9yhMhAs0za4RnvdMTxw26K/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng KPXH Cảm xúc của bé - 5 tuổi - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/11DzTR7A0ZrWmycMJZZu8m_KdFkyiTWsU/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng Truyện Cây rau của thỏ út - 4 tuổi - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1_3_P9_pTnygISOIjcJ7h3AjGxZvg-9ND/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng Nhận biết bộ phận trên cơ thể - 25-36 tháng - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1SRPsfTa8-VCUgi7pPFM8MvjX3nMy7EyJ/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng Trò chơi với chữ cái o, ô, ơ - 5 tuổi - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1bjpRj_P2m63tk5wU07cBh6GqqoJ2py0N/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng Thơ Cảm ơn - 4 tuổi - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1dprEDdxloz5Y-VrmZi-dekH5laq5xpOL/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng Thơ Trăng sáng - 18-24 tháng - MN Hoa Phượng", "url": "https://youtu.be/MNVClsXYnoU"},
        {"icon": "▶️", "label": "Tiết dạy NBPB Màu xanh - Màu đỏ - 25-36 tháng - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/1jCpfNWkXvJF03nNk_YbfAu6WpsfwuS76/edit?usp=drive_link&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Bài giảng TD Bước qua vật cản - 24 -36 tháng - MN Hoa Phượng", "url": "https://docs.google.com/presentation/d/11PnzvLTh5nMGYKxyEQS0HT159vDRW8sH/edit?usp=sharing&ouid=110455070676402034101&rtpof=true&sd=true"},
        {"icon": "▶️", "label": "Hoạt động ngoại khóa: Thăm quan xưởng may trang phục dân tộc Hiển Phan", "url": "https://youtu.be/RbolqEaJv_8"},
        {"icon": "▶️", "label": "Các bé 5 - 6 tuổi C2 tri ân các chú bộ đội nhân ngày 22/12", "url": "https://youtu.be/yh39OwUSygk"},
        {"icon": "▶️", "label": "nội dung bài hát: Chú bộ đội và cơn mưa", "url": "https://youtu.be/N_6E_y4kxt0"},
        {"icon": "▶️", "label": "Nội dung bài hát: Cháu thương chú bộ đội", "url": "https://youtu.be/q9_vQgt-Nqk"},
        {"icon": "▶️", "label": "Hoạt động: Nhận biết gọi tên hình tam giác, hình chữ nhật_Gv Nguyễn Thu Trang, lớp 3-4 tuổi", "url": "https://youtu.be/pMkz3lv4MLs"},
        {"icon": "▶️", "label": "Hoạt động trải nghiệm “Khám phá, tìm hiểu một số nghề địa phương", "url": "https://youtu.be/eUQUeqTgOCo"},
        {"icon": "▶️", "label": "Câu truyện “Cậu bé Tích Chu”", "url": "https://youtu.be/tvokwpYn2TY"},
        {"icon": "▶️", "label": "Bài hát Hình học vui nhộn", "url": "https://youtu.be/DJrlDCdtK7k"},
        {"icon": "▶️", "label": "Truyện Cá chép con", "url": "https://youtu.be/fhKJyxMuAP8"},
        {"icon": "▶️", "label": "Hoạt động ngoại khóa Thực hành kỹ năng PCCC", "url": "https://youtu.be/OFMngDaq4D4"},
        {"icon": "▶️", "label": "Thơ: Bạn mới. (MN Tú Thịnh)", "url": "https://github.com/MNTuThinhSDTQ/MNTT2025/issues/3"},
        {"icon": "▶️", "label": "Thơ: Giờ chơi. (MN Tú Thịnh)", "url": "https://github.com/MNTuThinhSDTQ/MNTT2025/issues/4"},
        {"icon": "▶️", "label": "Bài hát: Gà trống mèo con và cún con. (MN Tú Thịnh)", "url": "https://github.com/MNTuThinhSDTQ/MNTT2025/issues/2"},
        {"icon": "▶️", "label": "Truyện: Vì sao Thỏ cụt đuôi (MN Tú Thịnh)", "url": "https://youtu.be/uiwgjJfktwk?si=lYoVI5bRCc-jzX-T"},
        {"icon": "▶️", "label": "Thực đơn của bé", "url": "https://youtu.be/Jdx2-BBP7zY"},
        {"icon": "▶️", "label": "Chung tay phòng chống bệnh chân-tay-miệng", "url": "https://youtu.be/k-tHLLxdkDA"},
        {"icon": "▶️", "label": "Muá: Âm vang núi rừng, dân tộc Dao", "url": "https://youtu.be/pvUa1ZfW80I"},
        {"icon": "▶️", "label": "HĐTN: Tham quan trường tiểu học của các bé 5-6 tuổi", "url": "https://youtu.be/kax6CodLtLI"},
        {"icon": "▶️", "label": "HĐNK: Bé với an toàn giao thông", "url": "https://youtu.be/e4A-vGC0iwc"},
        {"icon": "▶️", "label": "Thực hành: Tham gia giao thông trên ngã tư đường phố", "url": "https://youtu.be/ivAvZ_jCrgA"},
        {"icon": "▶️", "label": "Ngày hội non sông", "url": "https://youtu.be/6KB6m_H3csk"},
        {"icon": "▶️", "label": "HĐNK: Thực hành kỹ năng PCCC", "url": "https://youtu.be/OFMngDaq4D4"},
    ]

    NUM_COLUMNS = 3 # Giữ 3 cột để hiển thị dưới dạng lưới

    for i in range(0, len(mn_links), NUM_COLUMNS):
        cols = st.columns(NUM_COLUMNS)
        for j, link_item in enumerate(mn_links[i:i + NUM_COLUMNS]):
            with cols[j]:
                # Thêm icon vào trước tên liên kết
                st.markdown(f"* {link_item['icon']} [{link_item['label']}]({link_item['url']})")

elif selected == "th":
    st.header("📘 Dạy học cấp Tiểu học")
    
    th_links = [
        {"icon": "▶️", "label": "Chatbot tạo đề kiểm tra Toán", "url": "https://chatgpt.com/g/g-68217174ce408191b372e097cbb90c98-tq-toan-tieuhoc"}, 
        {"icon": "▶️", "label": "Chatbot tạo đề kiểm tra Tin học", "url": "https://chatgpt.com/g/g-684782cf55cc8191a6d81a16827294d0-tq-tin-hoc-tieu-hoc"}, 
        {"icon": "▶️", "label": "Chatbot tạo đề kiểm tra Lịch sử - Địa lí", "url": "https://chatgpt.com/g/g-683c1a3e83c88191ad0808c492d14c71-lich-su-dia-ly"}, 
        {"icon": "▶️", "label": "Chuyển hình ảnh trong SGK thành video (Canva)", "url": "https://www.canva.com/design/DAGz5uviiso/tWWO8PeFqlOTBB_-ijTjfQ/edit"}, 
        {"icon": "▶️", "label": "Chatbot tạo đề kiểm tra Toán lớp 4", "url": "https://chatgpt.com/g/g-68ca708d8c0881919e6c6334d0c21320-tao-de-kiem-tra-mon-toan-lop-4"}, 
        {"icon": "▶️", "label": "Chatbot tạo đề kiểm tra Toán lớp 5", "url": "https://chatgpt.com/g/g-68cc9cceed888191be2ee01f2910ba3c-tao-de-kiem-tra-mon-toan-lop-5"}, 
        {"icon": "🎮", "label": "Trò chơi học tập trên nền tảng Canva", "url": "https://gameosomayman.my.canva.site/dagxlvtfz-o"}, 
        {"icon": "📁", "label": "Xây dựng bộ trò chơi khởi động bằng AI", "url": "https://drive.google.com/file/d/1Z1zd4gKtpeR_AKrFsUDStCfv8NSJmv3K/view"}, 
        {"icon": "▶️", "label": "Chatbot hỗ trợ xây dựng KHBG Tin học", "url": "https://chatgpt.com/g/g-68ca911197008191bac90cdba85f593f-tro-ly-soan-khbd-mon-tin-hoc-tieu-hoc"}, 
        {"icon": "▶️", "label": "Chatbot hỗ trợ xây dựng KHBG Âm nhạc (Gemini)", "url": "https://gemini.google.com/gem/df4aa386946f?usp=sharing"}, 
        {"icon": "▶️", "label": "Chatbot hỗ trợ học sinh học tập", "url": "https://ndduy100592.github.io/tieuhoc/"}, 
        {"icon": "▶️", "label": "Nhận xét,đánh giá thường xuyên, định kỳ môn Âm nhạc cấp Tiểu học:", "url": "https://notebooklm.google.com/notebook/85efc050-85c1-41a8-bb6f-b88cd81049ba?authuser=1"}, 
        {"icon": "▶️", "label": "Nhận xét,đánh giá thường xuyên, định kỳ môn Tin học cấp Tiểu học:", "url": "https://notebooklm.google.com/notebook/ae16ce5e-9bc1-4ea8-994b-454b5a78eb7a?authuser=1"}, 
        {"icon": "▶️", "label": "Chatbot soạn giáo án môn Tin học lớp 3", "url": "https://gemini.google.com/gem/e172aa044d29?usp=sharing"}, 
        {"icon": "▶️", "label": "Chatbot soạn giáo án môn Tin học lớp 4", "url": "https://gemini.google.com/gem/1LrrYMhn2yvcOKPG3oe_sWtzaatp2PhFP?usp=sharing"}, 
        {"icon": "▶️", "label": "Chatbot soạn giáo án môn Tin học lớp 5", "url": "https://gemini.google.com/gem/1G7vG2Psr9MMKGM22G98_Acse6E2xDoxn?usp=sharing"}, 
        {"icon": "▶️", "label": "Chatbot soạn giáo án môn Âm nhạc lớp 3", "url": "https://gemini.google.com/gem/1v87O1ajZR4sBELcKwHIZNdJyCz8BWjSP?usp=sharing"}, 
        {"icon": "▶️", "label": "Chatbot soạn giáo án môn Âm nhạc lớp 4", "url": "https://gemini.google.com/gem/1i_2m41Wc_T0iyn3p-uBjVSCr9JGvyZdc?usp=sharing"}, 
        {"icon": "▶️", "label": "Chatbot soạn giáo án môn Âm nhạc lớp 5", "url": "https://gemini.google.com/gem/1QRS4gmTXXemJzJkhhr-rkg4m6tlhex0E?usp=sharing"}, 
    ]

    NUM_COLUMNS = 3


    for i in range(0, len(th_links), NUM_COLUMNS):
        cols = st.columns(NUM_COLUMNS)
        for j, link_item in enumerate(th_links[i:i + NUM_COLUMNS]):
            with cols[j]:
                st.markdown(f"* {link_item['icon']} [{link_item['label']}]({link_item['url']})")

elif selected == "thcs":
    st.header("📙 Dạy học cấp THCS")
    
    thcs_links = [
        {"icon": "▶️", "label": "iTeX: Phần mềm tự động tạo câu hỏi Toán", "url": "https://www.youtube.com/@iTeX-Teams"}, 
        {"icon": "📁", "label": "Tạo bảng theo dõi thi đua học sinh bằng AI", "url": "https://docs.google.com/document/d/1nD1kp53I18KCCrhS1CHHMTlx2m66iQ8MtxX4fzIy7nQ/edit?usp=drive_link"}, 
        {"icon": "📁", "label": "Hướng dẫn tạo slide bài giảng tự động Gamma AI", "url": "https://drive.google.com/file/d/1vOjJZPHGzg4V67WJ27EM2EwEULGNKqnd/view"}, 
        {"icon": "📁", "label": "Ứng dụng AI trong soạn bài và thiết kế nội dung", "url": "https://docs.google.com/document/d/1oZwYV21kgAuw5ufkrNJrzkV2_NdQvPyQ/edit"}, 
        {"icon": "▶️", "label": "Hướng dẫn tạo Trợ lý AI tự động hóa bài soạn trên Gemini", "url": "https://docs.google.com/document/d/1bfJZauJgjGoTBvZ7wW0CQrCdn2qgX-vK/edit#heading=h.gj56e8mcine0"}, 
        {"icon": "▶️", "label": "Hướng dẫn tạo Chatbot xây dựng KHBG Ngữ văn 8", "url": "https://docs.google.com/document/d/1H4ZsYL9qaBgmNlCkB4Ec0E8a8YglDQeHlZ83B6x9sNE/edit?tab=t.0"}, 
        {"icon": "▶️", "label": "Sách nói Di sản văn hóa dân tộc Tày Dao năm 2025", "url": "https://remarkable-centaur-ea5b4b.netlify.app/"}, 
        {"icon": "▶️", "label": "Chatbot ôn tập tiếng anh 6: unit 1-3", "url": "https://gemini.google.com/share/ac9f88d30fef"}, 
        {"icon": "▶️", "label": "Công cụ vẽ đồ thị tương tác", "url": "https://gemini.google.com/share/2ff07d820508"},
    ]

    NUM_COLUMNS = 3

    for i in range(0, len(thcs_links), NUM_COLUMNS):
        cols = st.columns(NUM_COLUMNS)
        for j, link_item in enumerate(thcs_links[i:i + NUM_COLUMNS]):
            with cols[j]:
                st.markdown(f"* {link_item['icon']} [{link_item['label']}]({link_item['url']})")

elif selected == "thpt":
    st.header("📕 Dạy học cấp THPT")
    
    thpt_links = [
        {"icon": "▶️", "label": "iTeX: Phần mềm tự động tạo câu hỏi Toán", "url": "https://www.youtube.com/@iTeX-Teams"}, 
        {"icon": "▶️", "label": "Chatbot: Học sinh giỏi môn Tin học", "url": "https://chatgpt.com/g/g-688b68637db88191a7537adc8b4fe755-tro-ly-tin-hoc-hsg"}, 
        {"icon": "▶️", "label": "Chatbot: Học sinh giỏi môn Hóa học", "url": "https://chatgpt.com/g/g-688c16e1f338819198735dbadab0bb0b-tro-ly-hoa-hoc-chuyen-sau"}, 
        {"icon": "▶️", "label": "Chatbot: Học sinh giỏi môn Toán", "url": "https://chatgpt.com/g/g-688c7ff0165081919d6ebf35f7c7540b-on-luyen-hoc-sinh-gioi-quoc-gia-toan"}, 
        {"icon": "▶️", "label": "Chatbot: Học sinh giỏi môn Vật lí", "url": "https://chatgpt.com/g/g-688c88527ff081918a9a747c0597212f-tro-ly-vat-ly-chuyen-sau-bdhsgqg"}, 
        {"icon": "▶️", "label": "Chatbot: Học sinh giỏi môn Sinh học", "url": "https://chatgpt.com/g/g-688c894c97b48191bca4aaf2aef38510-sinh-hoc-hsg-quoc-gia-ai-tutor"}, 
        {"icon": "📁", "label": "Hướng dẫn sử dụng Google AI Studio", "url": "https://drive.google.com/file/d/1EiJX-Gt1o0fTY4UHgBEx63h8fHgtjyWp/view"}, 
        {"icon": "📁", "label": "Tài liệu hướng dẫn khai thác NotebookLM", "url": "https://docs.google.com/document/d/1LQdDnU_jhZ2SPy-NitOlYEugZSJzytFs/edit"}, 
        {"icon": "▶️", "label": "Tạo trờ chơi tương tác với Canva AI", "url": "https://www.youtube.com/watch?v=gosdE5sHfw8"}, 
        {"icon": "▶️", "label": "Hướng dẫn sử dụng NotebookLM", "url": "https://www.youtube.com/watch?v=eWSRK7Ug01s"}, 
    ]

    NUM_COLUMNS = 3

    for i in range(0, len(thpt_links), NUM_COLUMNS):
        cols = st.columns(NUM_COLUMNS)
        for j, link_item in enumerate(thpt_links[i:i + NUM_COLUMNS]):
            with cols[j]:
                st.markdown(f"* {link_item['icon']} [{link_item['label']}]({link_item['url']})")

elif selected is None:
    st.info("🎈 Hãy chọn một mục ở trên để xem nội dung chi tiết.")
