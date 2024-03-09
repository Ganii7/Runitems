import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

from file_updater import main as file_updater


class StackWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Runitems")

        self.switch = False

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        vbox.set_margin_start(30)
        vbox.set_margin_end(30)
        vbox.set_margin_top(30)
        vbox.set_margin_bottom(30)
        self.set_child(vbox)

        self.add_import_button(vbox)
        self.add_stack_and_switcher(vbox)

    def add_import_button(self, vbox):
        """
        Adds an import button to the specified vbox.

        Parameters:
            self (obj): The object itself.
            vbox (obj): The Gtk.VBox to which the button will be appended.

        Returns:
            None
        """
        button = Gtk.Button(label="Import items")
        button.connect('clicked', self.on_button_clicked)
        vbox.append(button)

    def add_stack_and_switcher(self, vbox):
        """
        Adds a stack and a stack switcher to the given vbox.

        :param vbox: Gtk.Box - the box to which the stack and stack switcher will be added
        :return: None
        """
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        stack.set_size_request(400, -1)  # Adjust width as needed
        vbox.append(stack)

        self.add_stack_pages(stack)

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.append(stack_switcher)

        stack.connect("notify::visible-child", self.on_stack_switched)

    def add_stack_pages(self, stack):
        """
        Add stack pages to the given stack.

        :param stack: The stack to add the pages to.
        """
        self.add_stack_page(stack, "Most popular lane", "check",
                            "<big> This imports the most popular\n item build for the main lane </big>")
        self.add_stack_page(stack, "All lanes", "label",
                            "<big> This imports the most popular\n item build for all lanes </big>")

    def add_stack_page(self, stack, title, name, markup):
        """
        Adds a page to the stack with the specified title, name, and markup.

        Parameters:
            stack (Gtk.Stack): The stack to which the page will be added.
            title (str): The title of the page.
            name (str): The name of the page.
            markup (str): The markup for the label on the page.

        Returns:
            None
        """
        label = Gtk.Label()
        label.set_markup(markup)
        label.set_wrap_mode(Gtk.WrapMode.WORD)
        stack.add_titled(label, name, title)

    def on_button_clicked(self, button):
        file_updater(self.switch)

    def on_stack_switched(self, stack, pspec):
        visible_child_name = stack.get_visible_child_name()
        self.switch = (visible_child_name == "label")


def activate(app):
    win = StackWindow(app)
    win.present()


def startup(app):
    pass


app = Gtk.Application(application_id="your.application.id",
                      flags=Gio.ApplicationFlags.FLAGS_NONE)
app.connect("activate", activate)
app.connect("startup", startup)
app.run()
