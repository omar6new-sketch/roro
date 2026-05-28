lbl_story.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll.add_widget(lbl_story)
        
        btn_next = Button(text="التالي", size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.4, 1))
        btn_next.bind(on_press=self.go_to_question)
        
        layout.add_widget(scroll)
        layout.add_widget(btn_next)
        self.add_widget(layout)
        
    def go_to_question(self, instance):
        self.manager.current = 'question'

# 3. شاشة السؤال والإرسال
class QuestionScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(text="سؤال خاص لكِ ❤️", font_size='22sp', bold=True))
        layout.add_widget(Label(text="عرفنا بعض ازاي؟ احكيلي بالتفصيل..", font_size='18sp'))
        
        self.txt_answer = TextInput(hint_text="اكتبي إجابتكِ هنا...", multiline=True, size_hint_y=None, height=150)
        
        self.btn_send = Button(text="إرسال الإجابة لكبسة قلبي", size_hint_y=None, height=50, background_color=(0.8, 0.2, 0.4, 1))
        self.btn_send.bind(on_press=self.send_answer)
        
        self.lbl_status = Label(text="", font_size='16sp')
        
        layout.add_widget(self.txt_answer)
        layout.add_widget(self.btn_send)
        layout.add_widget(self.lbl_status)
        self.add_widget(layout)
        
    def send_answer(self, instance):
        answer = self.txt_answer.text.strip()
        if answer:
            full_message = f"💌 إجابة من روان روح قلبك:\n\n{answer}"
            send_to_telegram(full_message)
            self.lbl_status.text = "تم الإرسال بنجاح يا روحي! وصلته خلاص 🥰"
            self.btn_send.disabled = True
        else:
            self.lbl_status.text = "اكتبي حاجة الأول عشان تبعتيها!"

class RoroApp(App):
    def build(self):
        self.title = "RORO"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(StoryScreen(name='story'))
        sm.add_widget(QuestionScreen(name='question'))
        return sm

if name == 'main':
    RoroApp().run()
