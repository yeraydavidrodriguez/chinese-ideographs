import pyvips
import os


def modify_icc_profile(source_image_path, destination_image_path, profile):
    image = pyvips.Image.new_from_file(source_image_path, access='sequential')
    result = image.icc_transform(profile)
    result.write_to_file(destination_image_path)