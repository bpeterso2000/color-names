import binascii
import json
import os


def test_colors():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    color_files = os.listdir(parent_dir)
    assert len(color_files) > 1
    for color_file in color_files:
        if color_file.endswith('.json'):
            with open(os.path.join(parent_dir, color_file)) as file_:
                colors = json.load(file_)
            for color_name, rgb_value in colors.items():
                assert color_name[0].islower()
                for letter in color_name[1:]:
                    assert letter.islower() or letter.isdigit()
                assert rgb_value.startswith('#')
                assert len(rgb_value[1:]) in (3, 6)
                binascii.unhexlify(rgb_value[1:])
