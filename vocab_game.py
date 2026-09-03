import time
import steamlit as st

st.title("เกมเติมศักพ์จับเวลา")
if "ans1_va1" not in st.session_state:
    st.session_state.ans1_va1 = ""
if "ans2_va1" not in st.session_state:
    st.session_state.ans2_va1 = ""




# ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
  st.session_state.ans1_va1 = "" # เคลียร์ค่าช่องข้อ1
  st.session_state.ans2_va1 = "" # เคลียร์ค่าช่องข้อ2
  st.session_state.staet = time.time() # เริ่มเวลาใหม่
  st.session_state.is_ended = False # ปิด Dialog


# -----------------------------------------------
# ฟังก์ชัน MessageBox (Dialog)
# -----------------------------------------------
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1,ans2):
  st.balloons()
  score = 0

u_ans1 = ans1.strip().lower()
u_ans2 = ans2.strip().lower()

# ตรวจข้อ1
if u_ans1 == "apple":
   st.success(" ข้อ1 : ถูกต้อง")
   score +- 1
else:
   st.error(f" ข้อ1: ยังไม่ถูกต้อง(คุณตอบ '{u_ans1} ')")
