from datetime import datetime, timedelta


class Time:
    dc = {
        "1": [],
        "2": [],
        "3": []
    }

    def __init__(self, time_now, name_block, time_training):
        self.time_now = self.name_block = self.time_training = None

        if self.check_str(name_block) and self.check_num(time_training):
            self.time_now = time_now
            self.name_block = name_block
            self.time_training = time_training
            self.res = ''

    @classmethod
    def check_str(cls, name):
        return isinstance(name, str)

    @classmethod
    def check_num(cls, num):
        return isinstance(num, int)

    def form_data_time(self, obj):
        return obj.strftime("%d-%m-%Y %H:%M")

    def base_dc(self, block):
        self.dc.update(block)

    def result(self):
        self.time_training = self.time_now + timedelta(hours=self.time_training)
        self.time_now = self.form_data_time(self.time_now)
        self.res = f'<<<{self.name_block.upper()}<<< поступило на тренировку <<<{self.time_now}<<<\n' \
                   f'>>>{self.name_block.upper()}>>> выйдет     с тренировки >>>{self.form_data_time(self.time_training)}>>>'
        return self.res


time_data = datetime.now()
a = Time(time_data, ' ', 95)
print(a.result())
