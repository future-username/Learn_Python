import matplotlib.pyplot as plt

# class Plot:
#     def __init__(self):
#         raise NotImplementedError()
#
#     @property
#     def diagram(self):
#         """
#         any diagrams for example: diagram.hist() or diagram.bar() ...
#         """
#         raise NotImplementedError()
#
#     @property
#     def settings_axis(self):
#         """
#         methods and settings axis
#         """
#         raise NotImplementedError()
#
#     @property
#     def (self):

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Plot(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def diagram(self):
        """
        any diagrams for example: diagram.hist() or diagram.bar() ...
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def settings_axis(self):
        """
        methods and settings axis
        """
        raise NotImplementedError()


class Diagram:
    def __init__(self, ax):
        self.ax = ax

    def line(self, x, y, **kwargs):
        """Plot line chart"""
        return self.ax.plot(x, y, **kwargs)

    def scatter(self, x, y, **kwargs):
        """Plot scatter chart"""
        return self.ax.scatter(x, y, **kwargs)

    def bar(self, x, height, **kwargs):
        """Plot bar chart"""
        return self.ax.bar(x, height, **kwargs)

    def hist(self, x, **kwargs):
        """Plot histogram"""
        return self.ax.hist(x, **kwargs)

    def pie(self, x, **kwargs):
        """Plot pie chart"""
        return self.ax.pie(x, **kwargs)


class AxisSettings:
    def __init__(self, ax):
        self.ax = ax

    def set_labels(self, xlabel=None, ylabel=None, title=None):
        """Set labels for axes and title"""
        if xlabel:
            self.ax.set_xlabel(xlabel)
        if ylabel:
            self.ax.set_ylabel(ylabel)
        if title:
            self.ax.set_title(title)
        return self

    def set_limits(self, xlim=None, ylim=None):
        """Set axis limits"""
        if xlim:
            self.ax.set_xlim(xlim)
        if ylim:
            self.ax.set_ylim(ylim)
        return self

    def set_grid(self, visible=True, **kwargs):
        """Set grid properties"""
        self.ax.grid(visible=visible, **kwargs)
        return self

    def set_ticks(self, xticks=None, yticks=None):
        """Set ticks for axes"""
        if xticks is not None:
            self.ax.set_xticks(xticks)
        if yticks is not None:
            self.ax.set_yticks(yticks)
        return self

    def set_scale(self, xscale=None, yscale=None):
        """Set scale for axes"""
        if xscale:
            self.ax.set_xscale(xscale)
        if yscale:
            self.ax.set_yscale(yscale)
        return self


class MatplotlibPlot(Plot):
    def __init__(self, figsize=(10, 6)):
        self.fig = plt.figure(figsize=figsize)
        self.ax = self.fig.add_subplot(111)
        self._diagram = Diagram(self.ax)
        self._settings_axis = AxisSettings(self.ax)

    @property
    def diagram(self):
        return self._diagram

    @property
    def settings_axis(self):
        return self._settings_axis

    def show(self):
        """Display the plot"""
        plt.show()

    def save(self, filename, **kwargs):
        """Save the plot to file"""
        self.fig.savefig(filename, **kwargs)

    def close(self):
        """Close the plot"""
        plt.close(self.fig)



if __name__ == "__main__":
    import numpy as np

    # Создаем данные
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Создаем график
    plot = MatplotlibPlot(figsize=(12, 8)).diagram

    # Строим линейный график
    plot.diagram.line(x, y, label='sin(x)', color='blue')

    # Настраиваем оси
    plot.settings_axis.set_labels(
        xlabel='X axis',
        ylabel='Y axis',
        title='Sin function'
    ).set_grid(True).set_limits(xlim=(0, 10), ylim=(-1.5, 1.5))

    # Показываем график
    plot.show()