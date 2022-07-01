from app.mixins.db_classes import NameMixin, CreatedUpdatedMixin, SortMixin, IsActiveMixin


class Category(NameMixin, CreatedUpdatedMixin, SortMixin, IsActiveMixin):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
