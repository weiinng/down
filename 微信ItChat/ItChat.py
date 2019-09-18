import itchat , time

class Itchat():

    def get_user(self):  #获取好友列表
        friends = itchat.get_friends(update=True)
        return friends

    def get_user_name(self):   #获取到所有好友的名称！
        user_name_list = []
        data = self.get_user()
        for a in data[0:]:
            user_name_list.append(a)
        print(user_name_list)
        return user_name_list


    def send_user(self):    #向好友群发消息
        for user in self.get_user_name():
            itchat.send_msg('测试数据！',toUserName=user['UserName'])
            print(user['NickName']+'发送成功！')



    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        print(msg)
        return msg.text


if __name__ == '__main__':
    itchat.auto_login()

    chat = Itchat()
    # chat.send_()
    # chat.get_user_name()
    itchat.run(debug=True)