# import matplotlib.pyplot as plt

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

# from abc import ABC, abstractmethod
# import matplotlib.pyplot as plt
#
#
# class Plot(ABC):
#     @abstractmethod
#     def __init__(self):
#         raise NotImplementedError()
#
#     @property
#     @abstractmethod
#     def diagram(self):
#         """
#         any diagrams for example: diagram.hist() or diagram.bar() ...
#         """
#         raise NotImplementedError()
#
#     @property
#     @abstractmethod
#     def settings_axis(self):
#         """
#         methods and settings axis
#         """
#         raise NotImplementedError()
#
#
# class Diagram:
#     def __init__(self, ax):
#         self.ax = ax
#
#     def line(self, x, y, **kwargs):
#         """Plot line chart"""
#         return self.ax.plot(x, y, **kwargs)
#
#     def scatter(self, x, y, **kwargs):
#         """Plot scatter chart"""
#         return self.ax.scatter(x, y, **kwargs)
#
#     def bar(self, x, height, **kwargs):
#         """Plot bar chart"""
#         return self.ax.bar(x, height, **kwargs)
#
#     def hist(self, x, **kwargs):
#         """Plot histogram"""
#         return self.ax.hist(x, **kwargs)
#
#     def pie(self, x, **kwargs):
#         """Plot pie chart"""
#         return self.ax.pie(x, **kwargs)
#
#
# class AxisSettings:
#     def __init__(self, ax):
#         self.ax = ax
#
#     def set_labels(self, xlabel=None, ylabel=None, title=None):
#         """Set labels for axes and title"""
#         if xlabel:
#             self.ax.set_xlabel(xlabel)
#         if ylabel:
#             self.ax.set_ylabel(ylabel)
#         if title:
#             self.ax.set_title(title)
#         return self
#
#     def set_limits(self, xlim=None, ylim=None):
#         """Set axis limits"""
#         if xlim:
#             self.ax.set_xlim(xlim)
#         if ylim:
#             self.ax.set_ylim(ylim)
#         return self
#
#     def set_grid(self, visible=True, **kwargs):
#         """Set grid properties"""
#         self.ax.grid(visible=visible, **kwargs)
#         return self
#
#     def set_ticks(self, xticks=None, yticks=None):
#         """Set ticks for axes"""
#         if xticks is not None:
#             self.ax.set_xticks(xticks)
#         if yticks is not None:
#             self.ax.set_yticks(yticks)
#         return self
#
#     def set_scale(self, xscale=None, yscale=None):
#         """Set scale for axes"""
#         if xscale:
#             self.ax.set_xscale(xscale)
#         if yscale:
#             self.ax.set_yscale(yscale)
#         return self
#
#
# class MatplotlibPlot(Plot):
#     def __init__(self, figsize=(10, 6)):
#         self.fig = plt.figure(figsize=figsize)
#         self.ax = self.fig.add_subplot(111)
#         self._diagram = Diagram(self.ax)
#         self._settings_axis = AxisSettings(self.ax)
#
#     @property
#     def diagram(self):
#         return self._diagram
#
#     @property
#     def settings_axis(self):
#         return self._settings_axis
#
#     def show(self):
#         """Display the plot"""
#         plt.show()
#
#     def save(self, filename, **kwargs):
#         """Save the plot to file"""
#         self.fig.savefig(filename, **kwargs)
#
#     def close(self):
#         """Close the plot"""
#         plt.close(self.fig)
#
#
#
# if __name__ == "__main__":
#     import numpy as np
#
#     # Создаем данные
#     x = np.linspace(0, 10, 100)
#     y = np.sin(x)
#
#     # Создаем график
#     plot = MatplotlibPlot(figsize=(12, 8)).diagram
#
#     # Строим линейный график
#     plot.diagram.line(x, y, label='sin(x)', color='blue')
#
#     # Настраиваем оси
#     plot.settings_axis.set_labels(
#         xlabel='X axis',
#         ylabel='Y axis',
#         title='Sin function'
#     ).set_grid(True).set_limits(xlim=(0, 10), ylim=(-1.5, 1.5))
#
#     # Показываем график
#     plot.show()


# import matplotlib.pyplot as plt
#
#
# class Plot:
#     def __init__(self):
#         raise NotImplementedError("This class is a wrapper and cannot be instantiated directly.")
#
#     # @property
#     class diagrams:
#         """
#         Methods for creating various diagrams and plots.
#         """
#
#         @staticmethod
#         def plot(*args, **kwargs):
#             return plt.plot(*args, **kwargs)
#
#         @staticmethod
#         def scatter(*args, **kwargs):
#             return plt.scatter(*args, **kwargs)
#
#         @staticmethod
#         def bar(*args, **kwargs):
#             return plt.bar(*args, **kwargs)
#
#         @staticmethod
#         def barh(*args, **kwargs):
#             return plt.barh(*args, **kwargs)
#
#         @staticmethod
#         def hist(*args, **kwargs):
#             return plt.hist(*args, **kwargs)
#
#         @staticmethod
#         def boxplot(*args, **kwargs):
#             return plt.boxplot(*args, **kwargs)
#
#         @staticmethod
#         def violinplot(*args, **kwargs):
#             return plt.violinplot(*args, **kwargs)
#
#         @staticmethod
#         def stem(*args, **kwargs):
#             return plt.stem(*args, **kwargs)
#
#         @staticmethod
#         def step(*args, **kwargs):
#             return plt.step(*args, **kwargs)
#
#         @staticmethod
#         def fill(*args, **kwargs):
#             return plt.fill(*args, **kwargs)
#
#         @staticmethod
#         def fill_between(*args, **kwargs):
#             return plt.fill_between(*args, **kwargs)
#
#         @staticmethod
#         def stackplot(*args, **kwargs):
#             return plt.stackplot(*args, **kwargs)
#
#         @staticmethod
#         def pie(*args, **kwargs):
#             return plt.pie(*args, **kwargs)
#
#         @staticmethod
#         def quiver(*args, **kwargs):
#             return plt.quiver(*args, **kwargs)
#
#         @staticmethod
#         def contour(*args, **kwargs):
#             return plt.contour(*args, **kwargs)
#
#         @staticmethod
#         def contourf(*args, **kwargs):
#             return plt.contourf(*args, **kwargs)
#
#         @staticmethod
#         def imshow(*args, **kwargs):
#             return plt.imshow(*args, **kwargs)
#
#         @staticmethod
#         def matshow(*args, **kwargs):
#             return plt.matshow(*args, **kwargs)
#
#         @staticmethod
#         def pcolor(*args, **kwargs):
#             return plt.pcolor(*args, **kwargs)
#
#         @staticmethod
#         def pcolormesh(*args, **kwargs):
#             return plt.pcolormesh(*args, **kwargs)
#
#         @staticmethod
#         def hexbin(*args, **kwargs):
#             return plt.hexbin(*args, **kwargs)
#
#     # @property
#     class settings_axis:
#         """
#         Methods for configuring and managing axis properties.
#         """
#
#         @staticmethod
#         def xlim(*args, **kwargs):
#             return plt.xlim(*args, **kwargs)
#
#         @staticmethod
#         def ylim(*args, **kwargs):
#             return plt.ylim(*args, **kwargs)
#
#         @staticmethod
#         def xticks(*args, **kwargs):
#             return plt.xticks(*args, **kwargs)
#
#         @staticmethod
#         def yticks(*args, **kwargs):
#             return plt.yticks(*args, **kwargs)
#
#         @staticmethod
#         def xlabel(*args, **kwargs):
#             return plt.xlabel(*args, **kwargs)
#
#         @staticmethod
#         def ylabel(*args, **kwargs):
#             return plt.ylabel(*args, **kwargs)
#
#         @staticmethod
#         def tick_params(*args, **kwargs):
#             return plt.tick_params(*args, **kwargs)
#
#         @staticmethod
#         def axis(*args, **kwargs):
#             return plt.axis(*args, **kwargs)
#
#         @staticmethod
#         def gca(*args, **kwargs):
#             return plt.gca(*args, **kwargs)
#
#         @staticmethod
#         def twinx(*args, **kwargs):
#             return plt.twinx(*args, **kwargs)
#
#         @staticmethod
#         def twiny(*args, **kwargs):
#             return plt.twiny(*args, **kwargs)
#
#         @staticmethod
#         def minorticks_on():
#             return plt.minorticks_on()
#
#         @staticmethod
#         def minorticks_off():
#             return plt.minorticks_off()
#
#     # @property
#     class text_and_annotations:
#         """
#         Methods for adding text and annotations to the plot.
#         """
#
#         @staticmethod
#         def title(*args, **kwargs):
#             return plt.title(*args, **kwargs)
#
#         @staticmethod
#         def suptitle(*args, **kwargs):
#             return plt.suptitle(*args, **kwargs)
#
#         @staticmethod
#         def text(*args, **kwargs):
#             return plt.text(*args, **kwargs)
#
#         @staticmethod
#         def annotate(*args, **kwargs):
#             return plt.annotate(*args, **kwargs)
#
#         @staticmethod
#         def legend(*args, **kwargs):
#             return plt.legend(*args, **kwargs)
#
#         @staticmethod
#         def colorbar(*args, **kwargs):
#             return plt.colorbar(*args, **kwargs)
#
#     # @property
#     class figure_management:
#         """
#         Methods for figure-level operations and configurations.
#         """
#
#         @staticmethod
#         def figure(*args, **kwargs):
#             return plt.figure(*args, **kwargs)
#
#         @staticmethod
#         def gcf():
#             return plt.gcf()
#
#         @staticmethod
#         def clf():
#             return plt.clf()
#
#         @staticmethod
#         def savefig(*args, **kwargs):
#             return plt.savefig(*args, **kwargs)
#
#         @staticmethod
#         def close(*args, **kwargs):
#             return plt.close(*args, **kwargs)
#
#     # @property
#     class grid_settings:
#         """
#         Methods to manage the grid on the plot.
#         """
#
#         @staticmethod
#         def grid(*args, **kwargs):
#             return plt.grid(*args, **kwargs)
#
#     # @property
#     class display:
#         """
#         Methods for displaying the plot.
#         """
#
#         @staticmethod
#         def show(*args, **kwargs):
#             return plt.show(*args, **kwargs)
#
#         @staticmethod
#         def draw():
#             return plt.draw()
#
#     # @property
#     class styles:
#         """
#         Methods for configuring plot styles and color maps.
#         """
#
#         @staticmethod
#         def use(*args, **kwargs):
#             return plt.style.use(*args, **kwargs)
#
#         @staticmethod
#         def colormaps():
#             return plt.colormaps()
#
#         @staticmethod
#         def set_cmap(*args, **kwargs):
#             return plt.set_cmap(*args, **kwargs)
#
#     # @property
#     class subplots:
#         """
#         Methods for working with subplots.
#         """
#
#         @staticmethod
#         def subplot(*args, **kwargs):
#             return plt.subplot(*args, **kwargs)
#
#         @staticmethod
#         def subplots(*args, **kwargs):
#             return plt.subplots(*args, **kwargs)
#
#         @staticmethod
#         def subplot2grid(*args, **kwargs):
#             return plt.subplot2grid(*args, **kwargs)
#
#         @staticmethod
#         def add_subplot(*args, **kwargs):
#             return plt.add_subplot(*args, **kwargs)
#
#         @staticmethod
#         def tight_layout(*args, **kwargs):
#             return plt.tight_layout(*args, **kwargs)
#
#     # @property
#     class supplementary:
#         """
#         Miscellaneous methods for additional functionality.
#         """
#
#         @staticmethod
#         def clim(*args, **kwargs):
#             return plt.clim(*args, **kwargs)
#
#         @staticmethod
#         def errorbar(*args, **kwargs):
#             return plt.errorbar(*args, **kwargs)
#
#         @staticmethod
#         def hlines(*args, **kwargs):
#             return plt.hlines(*args, **kwargs)
#
#         @staticmethod
#         def vlines(*args, **kwargs):
#             return plt.vlines(*args, **kwargs)
#
#         @staticmethod
#         def axhline(*args, **kwargs):
#             return plt.axhline(*args, **kwargs)
#
#         @staticmethod
#         def axvline(*args, **kwargs):
#             return plt.axvline(*args, **kwargs)
#
#         @staticmethod
#         def axhspan(*args, **kwargs):
#             return plt.axhspan(*args, **kwargs)
#
#         @staticmethod
#         def axvspan(*args, **kwargs):
#             return plt.axvspan(*args, **kwargs)
#
# # Диаграммы
# # Диаграммы
# x, y = 1, 2
# Plot.diagrams.plot(x, y)
# Plot.diagrams.scatter(x, y)
#
# # Настройка осей
# Plot.settings_axis.xlabel("X-axis")
# Plot.settings_axis.ylim(0, 10)
#
# # Текст и аннотации
# Plot.text_and_annotations.title("My Plot")
# Plot.text_and_annotations.legend()
#
# # Стиль
# Plot.styles.use("seaborn")
#
# # Отображение
# Plot.display.show()

# import matplotlib.pyplot as plt
#
#
# class Plot:
#     def __init__(self):
#         raise NotImplementedError()
#
#     @property
#     def diagram(self):
#         """
#         Графики и диаграммы: диаграммы, графики и др.
#         """
#         raise NotImplementedError()
#
#     def plot(self, *args, **kwargs):
#         """
#         Основной метод для построения графиков.
#         """
#         return plt.plot(*args, **kwargs)
#
#     def scatter(self, *args, **kwargs):
#         """
#         Точечный график.
#         """
#         return plt.scatter(*args, **kwargs)
#
#     def bar(self, *args, **kwargs):
#         """
#         Столбчатая диаграмма.
#         """
#         return plt.bar(*args, **kwargs)
#
#     def barh(self, *args, **kwargs):
#         """
#         Горизонтальная столбчатая диаграмма.
#         """
#         return plt.barh(*args, **kwargs)
#
#     def hist(self, *args, **kwargs):
#         """
#         Гистограмма.
#         """
#         return plt.hist(*args, **kwargs)
#
#     def boxplot(self, *args, **kwargs):
#         """
#         Диаграмма размаха (boxplot).
#         """
#         return plt.boxplot(*args, **kwargs)
#
#     def pie(self, *args, **kwargs):
#         """
#         Круговая диаграмма.
#         """
#         return plt.pie(*args, **kwargs)
#
#
# class Axis:
#     def __init__(self):
#         raise NotImplementedError()
#
#     def xlabel(self, *args, **kwargs):
#         """
#         Устанавливает метку по оси X.
#         """
#         return plt.xlabel(*args, **kwargs)
#
#     def ylabel(self, *args, **kwargs):
#         """
#         Устанавливает метку по оси Y.
#         """
#         return plt.ylabel(*args, **kwargs)
#
#     def xlim(self, *args, **kwargs):
#         """
#         Устанавливает границы оси X.
#         """
#         return plt.xlim(*args, **kwargs)
#
#     def ylim(self, *args, **kwargs):
#         """
#         Устанавливает границы оси Y.
#         """
#         return plt.ylim(*args, **kwargs)
#
#     def xticks(self, *args, **kwargs):
#         """
#         Устанавливает значения на оси X.
#         """
#         return plt.xticks(*args, **kwargs)
#
#     def yticks(self, *args, **kwargs):
#         """
#         Устанавливает значения на оси Y.
#         """
#         return plt.yticks(*args, **kwargs)
#
#     def grid(self, *args, **kwargs):
#         """
#         Включает или отключает сетку на графике.
#         """
#         return plt.grid(*args, **kwargs)
#
#
# class Labels:
#     def __init__(self):
#         raise NotImplementedError()
#
#     def title(self, *args, **kwargs):
#         """
#         Устанавливает заголовок графика.
#         """
#         return plt.title(*args, **kwargs)
#
#     def suptitle(self, *args, **kwargs):
#         """
#         Устанавливает общий заголовок для всех графиков на фигуре.
#         """
#         return plt.suptitle(*args, **kwargs)
#
#     def legend(self, *args, **kwargs):
#         """
#         Добавляет легенду на график.
#         """
#         return plt.legend(*args, **kwargs)
#
#     def annotate(self, *args, **kwargs):
#         """
#         Добавляет аннотацию на график.
#         """
#         return plt.annotate(*args, **kwargs)
#
#
# class Styles:
#     def __init__(self):
#         raise NotImplementedError()
#
#     def style(self, *args, **kwargs):
#         """
#         Устанавливает стиль графика.
#         """
#         return plt.style.use(*args, **kwargs)
#
#     def colormap(self, *args, **kwargs):
#         """
#         Устанавливает цветовую карту.
#         """
#         return plt.set_cmap(*args, **kwargs)
#
#
# class Layout:
#     def __init__(self):
#         raise NotImplementedError()
#
#     def figure(self, *args, **kwargs):
#         """
#         Создает новую фигуру.
#         """
#         return plt.figure(*args, **kwargs)
#
#     def subplot(self, *args, **kwargs):
#         """
#         Добавляет подграфик (subplot) на фигуру.
#         """
#         return plt.subplot(*args, **kwargs)
#
#     def subplots(self, *args, **kwargs):
#         """
#         Создает несколько подграфиков на фигуре.
#         """
#         return plt.subplots(*args, **kwargs)
#
#     def tight_layout(self, *args, **kwargs):
#         """
#         Автоматическая компоновка графиков на фигуре.
#         """
#         return plt.tight_layout(*args, **kwargs)
#
#     def show(self, *args, **kwargs):
#         """
#         Показывает все графики.
#         """
#         return plt.show(*args, **kwargs)
#
#
# # Пример использования
# plot = Plot()
# axis = Axis()
# labels = Labels()
# styles = Styles()
# layout = Layout()
#
# plot.plot([0, 1, 2], [2, 3, 5])
# axis.xlabel("Ось X")
# axis.ylabel("Ось Y")
# labels.title("Пример графика")
# layout.show()


import matplotlib.pyplot as plt

class FigureManager:
    """
    Управляет созданием и настройкой фигур и осей.
    """
    def figure(self):
        """Создает новую фигуру."""
        return plt.figure()

    def subplots(self):
        """Создает фигуру и набор осей."""
        return plt.subplots()

    def add_subplot(self):
        """Добавляет оси на текущую фигуру."""
        return plt.subplot()

    def gca(self):
        """Возвращает текущие оси."""
        return plt.gca()

    def gcf(self):
        """Возвращает текущую фигуру."""
        return plt.gcf()

    def clf(self):
        """Очищает текущую фигуру."""
        plt.clf()

    def close(self):
        """Закрывает фигуру."""
        plt.close()

# class PlotDrawer:
#     """
#     Предоставляет методы для построения различных типов графиков.
#     """
#     def plot(self, *args, **kwargs):
#         """Строит график линий."""
#         return plt.plot(*args, **kwargs)
#
#     def scatter(self):
#         """Строит точечный график."""
#         return plt.scatter()
#
#     def bar(self):
#         """Строит столбчатую диаграмму."""
#         return plt.bar()
#
#     def hist(self):
#         """Строит гистограмму."""
#         return plt.hist()
#
#     def imshow(self):
#         """Отображает изображение."""
#         return plt.imshow()
#
#     def pie(self):
#         """Строит круговую диаграмму."""
#         return plt.pie()
#
#     def errorbar(self):
#         """Строит график с полосами ошибок."""
#         return plt.errorbar()
#
#     def fill_between(self):
#         """Заполняет область между двумя линиями."""
#         return plt.fill_between()
#
# class AppearanceManager:
#     """
#     Управляет внешним видом графиков (заголовки, метки, легенда и т.д.).
#     """
#     def title(self):
#         """Устанавливает заголовок графика."""
#         plt.title()
#
#     def xlabel(self, *args, **kwargs):
#         """Устанавливает метку оси X."""
#         plt.xlabel(*args, **kwargs)
#         print(plt.xlabel.__doc__)
#
#     def ylabel(self):
#         """Устанавливает метку оси Y."""
#         plt.ylabel()
#
#     def legend(self):
#         """Отображает легенду."""
#         plt.legend()
#
#     def xlim(self):
#         """Устанавливает пределы оси X."""
#         plt.xlim()
#
#     def ylim(self):
#         """Устанавливает пределы оси Y."""
#         plt.ylim()
#
#     def grid(self):
#         """Включает/выключает сетку."""
#         plt.grid()
#
#     def xticks(self):
#         """Устанавливает метки оси X."""
#         plt.xticks()
#
#     def yticks(self):
#         """Устанавливает метки оси Y."""
#         plt.yticks()
#
#     def axis(self):
#         """Управляет свойствами осей."""
#         plt.axis()
#
# class TextManager:
#     """
#     Управляет текстом и аннотациями на графиках.
#     """
#     def text(self):
#         """Добавляет текст на график."""
#         plt.text()
#
#     def annotate(self):
#         """Добавляет аннотацию на график."""
#         plt.annotate()
#
#     def arrow(self):
#         """Добавляет стрелку на график."""
#         plt.arrow()
#
# class OutputManager:
#     """
#     Управляет сохранением и отображением графиков.
#     """
#     def show(self):
#         """Отображает график."""
#         plt.show()
#
#     def savefig(self):
#         """Сохраняет график в файл."""
#         plt.savefig()
#
# class StyleManager:
#     """
#     Управляет цветами, стилями и цветовыми картами.
#     """
#     def cm(self):
#         """Возвращает объект для работы с цветовыми картами."""
#         return plt.cm
#
#     def colormaps(self):
#         """Возвращает список доступных цветовых карт."""
#         return plt.colormaps()
#
#     def set_cmap(self):
#         """Устанавливает текущую цветовую карту."""
#         plt.set_cmap()
#
#     def style(self):
#         """Управляет стилями графиков."""
#         return plt.style
#
#     def rc(self):
#         """Управляет параметрами matplotlib."""
#         return plt.rc
#
# class PlotFacade:
#     """
#     Фасад, предоставляющий упрощенный интерфейс для работы с matplotlib.pyplot.
#     """
#     def __init__(self):
#         self._figure_manager = FigureManager()
#         self._plot_drawer = PlotDrawer()
#         self._appearance_manager = AppearanceManager()
#         self._text_manager = TextManager()
#         self._output_manager = OutputManager()
#         self._style_manager = StyleManager()
#
#     @property
#     def figure(self):
#         """Управляет созданием и настройкой фигур и осей."""
#         return self._figure_manager
#
#     @property
#     def plot(self):
#         """Предоставляет методы для построения различных типов графиков."""
#         return self._plot_drawer
#
#     @property
#     def appearance(self):
#         """Управляет внешним видом графиков (заголовки, метки, легенда и т.д.)."""
#         return self._appearance_manager
#
#     @property
#     def text(self):
#         """Управляет текстом и аннотациями на графиках."""
#         return self._text_manager
#
#     @property
#     def output(self):
#         """Управляет сохранением и отображением графиков."""
#         return self._output_manager
#
#     @property
#     def style(self):
#         """Управляет цветами, стилями и цветовыми картами."""
#         return self._style_manager

# Пример использования:
# plot_facade = PlotFacade()

# Теперь при plot_facade. вы увидите только свойства: figure, plot, appearance, text, output, style
# fig, ax = plot_facade.figure.subplots()

# Построение графика
# plot_facade.plot.plot([1, 2, 3], [2, 3, 1])
plot_facade.appearance.xlabel("Ось X")

# Настройка внешнего вида
# plot_facade.appearance.title("Пример графика")
# plot_facade.appearance.xlabel("Ось X")
# plot_facade.appearance.ylabel("Ось Y")

# Отображение графика
plot_facade.output.show()