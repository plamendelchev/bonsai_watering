import ujson

class Logger:
    def __init__(self, file='action_logs.txt'):
        self.file = file

    def get_logs(self):
        with open(self.file, 'r') as reader:
            logs = reader.readlines()
        return logs

    def append(self, date, job):
        line = {'date': date, 'job': job}
        json_line = ujson.dumps(line)

        with open(self.file, 'a') as writer:
            writer.write('{line},'.format(line=json_line))
