from ..models import TopicModel


class SearchTopicsController:
    model = TopicModel

    def get_by_name(self, name):
        topic = self.model.get(name=name)
        return topic

    def filter_by_name(self, name):
        topics = self.model.filter_by_name(name)
        return topics

    def get_all(self):
        topics = self.model.get_all()
        return topics
