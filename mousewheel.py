def _bound_mousewheel(self, eve):
    self.canvas.bind_all("<MouseWheel>", self.__move)


def _unbound_mousewheel(self, eve):
    self.canvas.unbind_all("<MouseWheel>")


def __move(self, event):
    self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")