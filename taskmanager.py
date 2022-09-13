import json
import os

importance_weight = 1.0
urgence_weight = 1.0


class Task:

    def __init__(self, tid, name, importance, urgence):
        self.tid = tid
        self.name = name
        self.importance = importance
        self.urgence = urgence

    def to_json(self):
        return {"id": self.tid, "name": self.name, "importance": self.importance, "urgence": self.urgence}

    def __lt__(self, other):
        self_value = ((importance_weight * self.importance) + (urgence_weight * self.urgence))
        other_value = ((importance_weight * other.importance) + (urgence_weight * other.urgence))
        return self_value < other_value

    def __gt__(self, other):
        self_value = ((importance_weight * self.importance) + (urgence_weight * self.urgence))
        other_value = ((importance_weight * other.importance) + (urgence_weight * other.urgence))
        return self_value > other_value

    def __le__(self, other):
        self_value = ((importance_weight * self.importance) + (urgence_weight * self.urgence))
        other_value = ((importance_weight * other.importance) + (urgence_weight * other.urgence))
        return self_value <= other_value

    def __ge__(self, other):
        self_value = ((importance_weight * self.importance) + (urgence_weight * self.urgence))
        other_value = ((importance_weight * other.importance) + (urgence_weight * other.urgence))
        return self_value >= other_value

    def __eq__(self, other):
        self_value = ((importance_weight * self.importance) + (urgence_weight * self.urgence))
        other_value = ((importance_weight * other.importance) + (urgence_weight * other.urgence))
        return self_value == other_value

    def __ne__(self, other):
        self_value = ((importance_weight * self.importance) + (urgence_weight * self.urgence))
        other_value = ((importance_weight * other.importance) + (urgence_weight * other.urgence))
        return self_value != other_value


class TaskList:

    def __init__(self):
        self.__task_id = 1
        self.__cache_dir = ".cache/cache.json"

        self.task_list = list()
        self.__init_from_cache()

    @staticmethod
    def __in_cache(data, task):
        for t1 in data["tasks"]:
            if t1["id"] == task.tid:
                return True
        return False

    def __index_of_task_list(self, tid):
        for i in range(len(self.task_list)):
            if tid == self.task_list[i].tid:
                return i
        return -1

    @staticmethod
    def __index_of_task_cache(data, tid):
        tasks = data["tasks"]
        for i in range(len(tasks)):
            if tasks[i]["id"] == tid:
                return i
        return -1

    def __init_from_cache(self):
        if not os.path.exists(".cache/"):
            os.makedirs(".cache/")
        try:
            cache_file = open(self.__cache_dir, "r")
        except FileNotFoundError:
            with open(self.__cache_dir, "x") as f:
                f.write('{"tasks":[],"task_id":1}')
            return
        data = json.loads(cache_file.read())

        self.__task_id = data["task_id"]

        for task in data["tasks"]:
            self.__add_task_wid(task["id"], task["name"], task["importance"], task["urgence"])

    def __add_to_cache(self, task):
        cache_file = open(self.__cache_dir, 'r')
        data = json.load(cache_file)
        cache_file.close()

        if self.__in_cache(data, task):
            return

        data["tasks"].append(task.to_json())
        data["task_id"] = self.__task_id
        cache_file = open(self.__cache_dir, 'w')
        json.dump(data, cache_file)
        cache_file.close()

    def add_task(self, name, importance, urgence):
        task = Task(self.__task_id, name, importance, urgence)
        self.task_list.append(task)
        self.task_list.sort(reverse=True)
        self.__task_id += 1
        self.__add_to_cache(task)

    def __add_task_wid(self, tid, name, importance, urgence):
        task = Task(tid, name, importance, urgence)
        self.task_list.append(task)
        self.task_list.sort(reverse=True)

    def __remove_from_cache(self, tid):
        cache_file = open(self.__cache_dir, "r+")
        data = json.load(cache_file)
        cache_file.close()

        idx = TaskList.__index_of_task_cache(data, tid)
        if idx == -1:
            return

        data["tasks"].pop(idx)
        cache_file = open(self.__cache_dir, 'w')
        json.dump(data, cache_file)
        cache_file.close()

    def remove_task(self, tid):
        idx = self.__index_of_task_list(tid)
        if idx == -1:
            return
        self.task_list.pop(idx)
        self.__remove_from_cache(tid)

    def __clear_cache(self):
        cache_file = open(self.__cache_dir, "r+")
        data = json.load(cache_file)
        cache_file.close()

        data["tasks"].clear()

        cache_file = open(self.__cache_dir, 'w')
        json.dump(data, cache_file)
        cache_file.close()

    def clear_tasks(self):
        self.task_list.clear()
        self.__clear_cache()
