# Source - https://stackoverflow.com/a/68615531
# Posted by The King Killer, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-24, License - CC BY-SA 4.0

import sys
from time import sleep
import Xlib.display

sleep(5)
def window_is_fullscreen(display=Xlib.display.Display()):
    """Check if window is fullscreen or not."""
    focused_window = display.get_input_focus().focus
    screen = display.screen()
    wm_info = win_width = get_focused_window_info(focused_window)
    win_width = get_focused_window_info(focused_window)['width']
    win_height = get_focused_window_info(focused_window)['height']
    reso = get_desktop_resolution(screen)
    # Desktop environments in general should appear in fullscreen,
    # generating false positives, a way to ignore them is necessary.
    if wm_info['class'] != 'xfdesktop':
        print(win_width, win_height)
        if win_width == reso['width'] and win_height == reso['height']:
            return True
        else:
            return False

def get_desktop_resolution(screen):
    """Get desktop resolution."""
    return {
        'width': screen.width_in_pixels, 
        'height': screen.height_in_pixels
    }

def get_focused_window_info(window):
    """Get info from focused window'"""
    wmname = window.get_wm_name()
    try:
        wmclass = window.get_wm_class()[0]
    except TypeError:
        wmclass = window.get_wm_class()
        pass
    wm_data = window.get_geometry()._data
    width = wm_data['width']
    height = wm_data['height']
    # workaround for Java app
    # https://github.com/JetBrains/jdk8u_jdk/blob/master/src/solaris/classes/sun/awt/X11/XFocusProxyWindow.java#L35
    if not wmclass and not wmname or "FocusProxy" in wmclass:
        parent_window = window.query_tree().parent
        if parent_window:
            return get_focused_window_info(parent_window)
    elif wmclass and wmname:
        return {'class': wmclass, 'name': wmname, 'width': width, 'height': height}
    elif wmclass and not wmname:
        return {'class': wmclass, 'width': width, 'height': height}
    elif not wmclass and wmname:
        return {'name': wmname, 'width': width, 'height': height}
    return None