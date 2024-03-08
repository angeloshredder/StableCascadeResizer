# quick node to set resize a picture for Stable Cascade
# by Angelo
class CascadeResize:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 2048}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 2048}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "resize_picture"  # Corrected attribute name
    CATEGORY = "image"

    @staticmethod
    def resize_picture(width, height):
        original_aspect_ratio = height / width
        original_resolution = width * height

        best_resolution_diff = float('inf')
        best_aspect_ratio_diff = float('inf')
        best_W, best_H = 0, 0

        for W in range(64, width + 1, 64):
            for H in range(64, height + 1, 64):
                aspect_ratio = H / W
                aspect_ratio_diff = abs(original_aspect_ratio - aspect_ratio)
                resolution_diff = abs(original_resolution - (W * H))

                if resolution_diff < best_resolution_diff or \
                        (resolution_diff == best_resolution_diff and aspect_ratio_diff < best_aspect_ratio_diff):
                    best_resolution_diff = resolution_diff
                    best_aspect_ratio_diff = aspect_ratio_diff
                    best_W = W
                    best_H = H

        return best_W, best_H


NODE_CLASS_MAPPINGS = {
    "CascadeResize": CascadeResize
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Cascade_Resizer": "Cascade_Resizer"
}
