import rospy
from std_srvs.srv import Empty

rospy.init_node('navigation_client')
rospy.wait_for_service('/go_to_kitchen')
rospy.wait_for_service('/stop')
rospy.wait_for_service('/go_home')

go_to_kitchen = rospy.ServiceProxy('/go_to_kitchen', Empty)
stop = rospy.ServiceProxy('/stop', Empty)
go_home = rospy.ServiceProxy('/go_home', Empty)

# ทำการเดินทางไปยังห้องครัว
go_to_kitchen()

# หยุด
stop()

# กลับมาที่จุดเริ่มต้น
go_home()

# หยุดอีกครั้ง
stop()
