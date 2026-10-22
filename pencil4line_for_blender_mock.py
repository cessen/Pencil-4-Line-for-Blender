# Mocking out the cpp module, so we can load the addon for the node
# trees and whatnot without actually needing Pencil+ itself.

line_render_element = None
vector_output = None

class draw_ret:
    success: None = None
    success_without_license: None = None
    timeout: None = None
    error_unknown: None = None

def interm_context():
    return None

def simulate_esc_key_press():
    pass

def interm_camera(
    clip_start: float,
    clip_end: float,
    line_size: float,
    camera_matrix,
    window_matrix
):
    return None

def interm_curve_data(
    materials,
    material_indices: list[int],
):
    return None

def interm_render_Instance(
    src_object,
    instance_matrix_world,
    mesh,
    holdout,
    object_materials
):
    return None

def set_blender_version(major, minor, patch):
    pass

def set_render_app_path(path):
    pass

def draw_options():
    return None

def brush_detail_node():
    return None

def texture_map_node():
    return None

def create_previews(
    preview_size,
    stroke_preview_width,
    brush_detail_node,
    stroke_preview_brush_size,
    stroke_preview_scale,
    color,
    bg_color,
    hash_prev
):
    return None
