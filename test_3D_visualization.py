# show the .obj file
import open3d as o3d
import numpy as np

# obj_tex_path = 'output_data/01802/01802_obj.obj'
# Read the OBJ file
# mesh = o3d.io.read_triangle_mesh(obj_tex_path)


def capture_default_view(mesh_path, output_image_path, width=512, height=512):
    # Read the mesh
    mesh = o3d.io.read_triangle_mesh(mesh_path)

    # Ensure the mesh has normals
    # if not mesh.has_vertex_normals():
    #     mesh.compute_vertex_normals()

    # Create visualizer object
    vis = o3d.visualization.Visualizer()
    vis.create_window(width=width, height=height, visible=False)
    vis.add_geometry(mesh)

    # This will set up the default camera view
    vis.reset_view_point(True)

    # Update rendering
    vis.poll_events()
    vis.update_renderer()

    # Capture image
    image = vis.capture_screen_float_buffer(do_render=True)

    # Convert to numpy array
    plt_img = np.asarray(image)

    # Convert to uint8
    plt_img = (plt_img * 255).astype(np.uint8)

    # Create Open3D Image
    o3d_image = o3d.geometry.Image(plt_img)

    # Save image
    o3d.io.write_image(output_image_path, o3d_image)

    # Clean up
    vis.destroy_window()

mesh_path = "output_data/01802/01802_obj.obj"
output_path = "output_data/01802/01802_screenshot.png"
capture_default_view(mesh_path, output_path)


# # Remove texture by setting vertex colors to None
# mesh.textures = []
# mesh.vertex_colors = o3d.utility.Vector3dVector([])
#
# # Optional: You can set a single color for the entire mesh
# mesh.paint_uniform_color([0.7, 0.7, 0.7])  # Gray color - RGB values between 0 and 1
#
# # Optional: Compute vertex normals for better visualization
# mesh.compute_vertex_normals()

# # Visualize the mesh
# o3d.visualization.draw_geometries([mesh])