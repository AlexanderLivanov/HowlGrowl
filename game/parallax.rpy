init python:
    build.classify("**01_parallax_viewport.rpy", None)
    build.classify("**01_parallax_viewport.rpyc", "archive")

################################################################################

python early:

    class ParallaxVP(Viewport):
        """
        Специальный видоискатель с параллаксом. Наследуется от Viewport.
        Автоматически прокручивает детей на основе их размеров.
        """
        def render(self, width, height, st, at):
            self.width = width
            self.height = height

            child_width = self.child_width or width
            child_height = self.child_height or height

            surf = renpy.render(self.child, child_width, child_height, st, at)
            cw, ch = surf.get_size()
            cxo, cyo, width, height = self.update_offsets(cw, ch, st)

            self.offsets = [(cxo, cyo)]

            rv = renpy.Render(width, height)

            for child in self.child.children:
                child_render = child.render(width, height, st, at)
                pct_xscrolled = self.xadjustment.value / max(self.xadjustment.range, 1.0)
                pct_yscrolled = self.yadjustment.value / max(self.yadjustment.range, 1.0)
                child_w, child_h = child_render.get_size()

                new_xo = (width - child_w) * pct_xscrolled
                new_yo = (height - child_h) * pct_yscrolled

                child_render.xclipping = False
                child_render.yclipping = False
                rv.blit(child_render, (new_xo, new_yo))

            rv = rv.subsurface((0, 0, width, height), focus=True)

            if self.draggable or self.arrowkeys:
                rv.add_focus(self, None, 0, 0, width, height)

            return rv

    renpy.register_sl_displayable(
        "parallax_viewport", ParallaxVP, 'viewport', 1,
        replaces=True, pass_context=True
    ).add_property("child_size"
    ).add_property("mousewheel"
    ).add_property("arrowkeys"
    ).add_property("pagekeys"
    ).add_property("draggable"
    ).add_property("edgescroll"
    ).add_property("xadjustment"
    ).add_property("yadjustment"
    ).add_property("xinitial"
    ).add_property("yinitial"
    ).add_property("scrollbars"
    ).add_property("spacing"
    ).add_property("transpose"
    ).add_property("xminimum"
    ).add_property("yminimum"
    ).add_property_group("position"
    ).add_property_group("ui")

init python:

    class AnimateScroll(Scroll):
        """
        Плавная анимация прокрутки с варперами.
        """
        def __init__(self, id, direction, amount="step", delay=0.5, warper="ease-in-out"):
            super().__init__(id, direction, amount)
            self.delay = delay
            self.warper = warper

        def get_adjustment_and_delta(self):
            d = renpy.get_widget(None, self.id)
            if d is None:
                return None, +1

            if "horizontal" in self.direction:
                adjustment = d.xadjustment
            elif "vertical" in self.direction:
                adjustment = d.yadjustment
            else:
                adjustment = d.adjustment

            delta = 1 if "increase" in self.direction else -1
            return adjustment, delta

        def __call__(self):
            adjustment, delta = self.get_adjustment_and_delta()

            if adjustment is None:
                raise Exception(f"No displayable with the id {self.id}.")

            if self.amount == "step":
                amount = delta * adjustment.step
            elif self.amount == "page":
                amount = delta * adjustment.page
            elif self.amount == "max":
                amount = adjustment.range
            elif self.amount == "min":
                amount = -adjustment.range
            elif self.amount == "toggle":
                amount = -adjustment.range if adjustment.value == adjustment.range else adjustment.range
            else:
                amount = delta * self.amount

            adjustment.animate(amount, self.delay, renpy.atl.warpers[self.warper])

style vparallax_fixed:
    xfit True
    yfit True

################################################################################

#screen parallax_view():
#    tag menu
#
#    # Параллакс-видоискатель с изображением
#    parallax_viewport id "parallax":
#        child "images/large_image.png"
#        draggable True
#        xadjustment Adjustment(range=2000, value=0)
#        yadjustment Adjustment(range=1000, value=0)
#
#    # Кнопки управления прокруткой
#    hbox:
#        spacing 20
#        textbutton "Влево" action AnimateScroll("parallax", "horizontal decrease")
#        textbutton "Вправо" action AnimateScroll("parallax", "horizontal increase")
#        textbutton "Вверх" action AnimateScroll("parallax", "vertical decrease")
#        textbutton "Вниз" action AnimateScroll("parallax", "vertical increase")
