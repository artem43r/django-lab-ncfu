class MyMixin:
    mixin_prop = ''
    
    def get_prop(self):
        return self.mixin_prop.upper()
    
    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()
class MetaTagsMixin:
    meta_description = ''
    meta_keywords = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['meta_description'] = self.meta_description
        context['meta_keywords'] = self.meta_keywords

        return context
    
