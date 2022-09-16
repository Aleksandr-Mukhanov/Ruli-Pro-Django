from app.mixins.db_classes import NameMixin, CreatedUpdatedMixin, SortMixin, IsActiveMixin


class Category(NameMixin, CreatedUpdatedMixin, SortMixin, IsActiveMixin):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class CarModels(NameMixin):

    class Meta:
        verbose_name = 'Модели авто'
        verbose_name_plural = 'Модель авто'

    def __str__(self):
        return self.name


class CarColors(NameMixin):

    class Meta:
        verbose_name = 'Цвета авто'
        verbose_name_plural = 'Цвет авто'

    def __str__(self):
        return self.name
