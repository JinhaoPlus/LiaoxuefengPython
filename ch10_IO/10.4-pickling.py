import pickle, json

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

# with open('/Users/jinhaoplus/Desktop/pickling.txt', 'wb') as f:
#     pickle.dump(d, f)

with open('/Users/jinhaoplus/Desktop/pickling.txt', 'rb') as f:
    dump = pickle.load(f)

print(dump)

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student Name=%s Age=%d Score=%s' % (self.name, self.age, self.score)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
