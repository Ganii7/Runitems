import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from file_updater import main as file_updater


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        # Create a Builder
        builder = Gtk.Builder()
        builder.add_from_file("linux.ui")

        # Obtain and show the main window
        self.win = builder.get_object("main_window")
        # Application will close once it no longer has active windows attached to it
        self.win.set_application(self)
        # Connect buttons to functions
        import_main_lane = builder.get_object("import_main_lane")
        import_main_lane.connect("clicked", self.button_clicked, False)
        import_all_lane = builder.get_object("import_all_lane")
        import_all_lane.connect("clicked", self.button_clicked, True)

        # Set dark mode
        Adw.StyleManager.get_default().set_color_scheme(Adw.ColorScheme.FORCE_DARK)

        self.win.present()

    def button_clicked(self, button, var):
        file_updater(var)


app = MyApp(application_id="com.runitems.Runitems")
app.run(sys.argv)
