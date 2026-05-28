def check_rules(self, pos, player_name, log):
        # ركل الخصم
        if self.p1_pos == self.p2_pos and pos != 0:
            if player_name == "اللاعب 1":
                self.p2_pos = max(0, self.p2_pos - 5)
                log += "🤺 كفو! اللاعب 1 ركل اللاعب 2 وأرجعه 5 خطوات!\n"
            else:
                self.p1_pos = max(0, self.p1_pos - 5)
                log += "🤺 كفو! اللاعب 2 ركل اللاعب 1 وأرجعه 5 خطوات!\n"
                
        # المربعات السحرية والفخاخ والفلوس
        if pos in self.bonus_tiles:
            log += "✨ مربع سحري! تقدم 3 خطوات مجاناً!\n"
            if player_name == "اللاعب 1": self.p1_pos = min(50, self.p1_pos + 3)
            else: self.p2_pos = min(50, self.p2_pos + 3)
        elif pos in self.trap_tiles:
            log += "💥 فخ! تراجع 4 خطوات للخلف!\n"
            if player_name == "اللاعب 1": self.p1_pos = max(0, self.p1_pos - 4)
            else: self.p2_pos = max(0, self.p2_pos - 4)
        elif pos in self.coin_tiles:
            log += "💰 صندوق ذهب! حصلت على +10 عملات!\n"
            if player_name == "اللاعب 1": self.p1_coins += 10
            else: self.p2_coins += 10
            
        return log

    def buy_bomb(self, instance):
        if self.turn == 1 and self.p1_coins >= 25:
            self.p1_coins -= 25
            self.p2_pos = max(0, self.p2_pos - 5)
            self.update_ui("💣 اللاعب 1 اشترى قنبلة وفجّر اللاعب 2 (-5 خطوات)!")
        elif self.turn == 2 and self.p2_coins >= 25:
            self.p2_coins -= 25
            self.p1_pos = max(0, self.p1_pos - 5)
            self.update_ui("💣 اللاعب 2 اشترى قنبلة وفجّر اللاعب 1 (-5 خطوات)!")
        else:
            self.log_label.text = "❌ لا تملك عملات كافية (تحتاج 25 عملة)!"

    def update_ui(self, log_text):
        self.p1_label.text = f"👤 اللاعب 1 (❌)\nالموقع: {self.p1_pos} | 💰: {self.p1_coins}"
        self.p2_label.text = f"👤 اللاعب 2 (⭕)\nالموقع: {self.p2_pos} | 💰: {self.p2_coins}"
        self.log_label.text = log_text

    def end_game(self, winner):
        self.log_label.text = f"👑 مبرووووك! {winner} هو الفائز ببطولة RORO! 👑"
        self.roll_btn.disabled = True
        self.bomb_btn.disabled = True

class RoroApp(App):
    def build(self):
        return RoroGame()

if name == 'main':
    RoroApp().run()