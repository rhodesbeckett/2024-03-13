from controller.Cutting import Cutting
from controller.Merging import Merging
from controller.Rendering import Rendering
from controller.Testing import Testing
from controller.TestingPicture import TestingPicture


class Controller():
    def __init__(self, collection):
        self.collection = collection

    def test(self, ID):
        testing = Testing(self.collection, ID)
        testing.test_all()
        return testing.test_response

    def cut(self, ID):
        cutting = Cutting(self.collection, ID)
        cutting.cut_all()

    def render(self, ID):
        rendering = Rendering(self.collection, ID)
        rendering.render()

    def merge_videos(self, ID):
        merging = Merging(ID)
        merging.merge_videos()

    def get_photo(self, ID, minute, second):
        return TestingPicture(ID).test_photo(minute, second)
