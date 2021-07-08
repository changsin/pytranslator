import pptx.shapes.graphfrm
from pptx import Presentation
from pptx.shapes.graphfrm import GraphicFrame, Table
from pptx.shapes.autoshape import Shape
from pptx.enum.shapes import MSO_SHAPE_TYPE

class PptHandler:
    def __init__(self, translator):
        self.translator = translator

    def set_font(self, shape, font_name):
        for paragraph in shape.text_frame.paragraphs:
            paragraph.font.name = font_name

    def translate_payload(self, slide):
        def _translate_text(obj):
            if obj.text and str(obj.text).strip():
                translated_text = self.translator.translate(obj.text)
                print("\t: {}->{}".format(obj.text, translated_text))
                if translated_text:
                    obj.text = translated_text

        print(len(slide.shapes))
        for shape in slide.shapes:
            if isinstance(shape, Shape):
                _translate_text(shape)
                # self.set_font(shape, 'Gulim')
                # pass
            elif isinstance(shape, GraphicFrame):
                if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
                    for row in shape.table.rows:
                        for cell in row.cells:
                            _translate_text(cell)
                else:
                    if shape.shape_type == MSO_SHAPE_TYPE.EMBEDDED_OLE_OBJECT:
                        pass
                    else:
                        print("### Unknown GraphicFrame type", type(shape), shape)
            else:
                if isinstance(shape, pptx.shapes.connector.Connector):
                    pass
                else:
                    print("### Unknown GraphicFrame type", type(shape), shape)

    def translate(self, path):
        presentation = Presentation(path)
        print(len(presentation.slides))
        for slide, id in zip(presentation.slides, range(5)):
            print(id)
            self.translate_payload(slide)
            id += 1

        presentation.save(path[:-5] + "-tr" + path[-5:])
