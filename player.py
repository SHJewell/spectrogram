import dearpygui.dearpygui as dpg
import dearpygui_extend as dpge

import pydub
import simpleaudio as sa
import time

def fileBrowse():
    pass

    # dpge.add_file_browser(
    #     default_path=r"E:\Music",
    #     collapse_sequences=False
    # )


def exit_gui():

    print("Exiting")
    dpg.stop_dearpygui()
    dpg.destroy_context()


def show_selected_file(sender, files, cancel_pressed):

    if not cancel_pressed:
	    print(files[0])


def guiFrame():
    # a = ""
    a_buff = []
    t0 = time.time()
    # dpg.set_exit_callback(exit_gui)

    dpg.create_context()
    with dpg.window(tag="Primary Window"):
        #dpg.add_button(label="Select File", callback=fileBrowse)

        dpge.add_file_browser(
            width=800,
            height=600,
            default_path="E:\\Music",
            show_as_window=True,
            show_ok_cancel=True,
            allow_multi_selection=False,
            collapse_sequences=False,
            modal_window=True,
            allow_create_new_folder=False,
            #filetype_filter="audio",
            callback=show_selected_file)


        # dpg.add_button(label="Select File")

            # a = dpge.add_file_browser(
            #     default_path=r"E:\Music",
            #     collapse_sequences=False
            # )

            # dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))

        dpg.add_button(label="Exit", callback=exit_gui)

    dpg.create_viewport(title='Custom Title', width=1200, height=800)
    dpg.setup_dearpygui()

    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)

    # pg.start_dearpygui()
    while dpg.is_dearpygui_running():

        # if a != "":
        #     a_buff.append(a)
        #
        # if time.time() - t0 > 1:
        #     print(a_buff)
        #     a_buff = []
        #     t0 = time.time()


        dpg.render_dearpygui_frame()


    dpg.destroy_context()


if __name__ == "__main__":

    guiFrame()