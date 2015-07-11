__version__ = "1.0"

from kivy.app import App
from kivy.lang import Builder
from kivy.garden.scrolllabel import ScrollLabel

LOREM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur nec arcu accumsan, lacinia libero sed, cursus nisi. Curabitur volutpat mauris id ornare finibus. Cras dignissim arcu viverra, bibendum est congue, tempor elit. Vivamus luctus sapien sapien, id tincidunt eros molestie vitae. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut commodo eget purus vel efficitur. Duis facilisis ex dolor, vel convallis odio pharetra quis. Vivamus eu suscipit tortor. Proin a tellus a nisl iaculis aliquam. Nam tristique ipsum dui, ut faucibus libero lacinia id. Pellentesque eget rhoncus justo, quis interdum eros. Suspendisse felis lorem, gravida in orci ac, auctor malesuada turpis. Fusce dapibus urna dolor, id viverra enim semper a. Proin dignissim neque quis ante commodo feugiat.
Duis dictum sagittis urna nec dapibus. Vestibulum ac elit vel nunc euismod lobortis. Vivamus sit amet tortor in diam consectetur ultrices vitae vulputate leo. Aenean vehicula orci leo, eget fringilla enim condimentum eget. Sed sapien lacus, vulputate nec ligula eget, luctus feugiat risus. Nullam ultricies quam ac metus imperdiet, eget scelerisque dolor commodo. Ut nec elementum orci. Cras massa lacus, consectetur varius est a, congue pulvinar magna. Proin nec sapien facilisis, tristique turpis vel, malesuada leo. Phasellus faucibus justo vel risus tristique, in laoreet ligula vestibulum. Vestibulum varius eget nibh nec convallis. Morbi eu diam at turpis mollis hendrerit. Aenean sed turpis lectus.
Suspendisse pharetra ligula nec faucibus mattis. Aliquam et felis eget augue efficitur aliquam viverra ut tellus. Aliquam sagittis ut sapien venenatis condimentum. Quisque in turpis ac nisi vehicula commodo vel porttitor erat. Maecenas lobortis, sapien dictum congue gravida, nulla urna ultricies lorem, at tincidunt ex arcu nec eros. Maecenas egestas a augue sit amet euismod. Praesent ut sapien metus. Curabitur lorem erat, consectetur quis rhoncus quis, tristique ac ligula. Suspendisse justo magna, cursus id mauris et, lacinia egestas neque.
Suspendisse bibendum sit amet est eget ullamcorper. Duis pellentesque tristique nisi. Donec id dolor eget arcu lobortis sollicitudin vel et justo. Vivamus vel risus eget felis condimentum tempus ac sed dui. Donec placerat risus quis metus auctor sagittis. Pellentesque vel sem dolor. Praesent erat eros, facilisis placerat ultrices et, interdum quis risus. Donec eleifend risus dapibus, laoreet felis ut, fermentum neque. Aenean purus elit, congue non tempus quis, dictum quis metus. Maecenas finibus rutrum bibendum. Ut vestibulum dapibus felis vel luctus. Aliquam vitae consequat eros, quis ultricies tortor. Quisque eu accumsan erat, id commodo nisi.
Etiam nec risus porttitor, placerat est et, facilisis diam. Etiam vel feugiat ligula. Aliquam at quam congue, lacinia velit nec, congue nibh. In varius quis elit vel sollicitudin. Vivamus molestie elementum ipsum et vehicula. Etiam non augue quis tortor ultrices maximus. Etiam vel blandit nibh. Nullam facilisis posuere erat vel mattis. Vestibulum mattis condimentum purus efficitur vehicula. Aliquam consequat interdum eros eu semper. Etiam feugiat, erat at tempor tincidunt, odio eros maximus sapien, sit amet lacinia nibh tortor quis dui. In hac habitasse platea dictumst.
"""

KV_EXAMPLE = """
#: import LOREM __main__.LOREM
BoxLayout:
    orientation: "vertical"
    Label:
        text: "ScrollLabel Demo"
        size_hint_y: None
        height: "48sp"

    ScrollLabel:
        id: sl
        text: LOREM * int(sl_count.value)
        font_size: sl_fontsize.value

    BoxLayout:
        size_hint_y: None
        height: "48sp"
        Label:
            text: "Text count"
            size_hint_x: None
            width: self.texture_size[0] + dp(48)
        Slider:
            id: sl_count
            min: 1
            max: 20
            value: 1
            step: 1

    BoxLayout:
        size_hint_y: None
        height: "48sp"
        Label:
            text: "Font size"
            size_hint_x: None
            width: self.texture_size[0] + dp(48)
        Slider:
            id: sl_fontsize
            min: sp(8)
            max: sp(100)
            value: sp(14)

    BoxLayout:
        size_hint_y: None
        height: "48sp"
        Label:
            text: "Alignment"
            size_hint_x: None
            width: self.texture_size[0] + dp(48)
        Button:
            text: "Left"
            on_press: sl.halign = "left"
        Button:
            text: "Center"
            on_press: sl.halign = "center"
        Button:
            text: "Right"
            on_press: sl.halign = "right"

    BoxLayout:
        size_hint_y: None
        height: "32sp"

        Label:
            text: "Len: {} - Size: {}".format(len(sl.text), sl.content_size)

"""


class TestScrollLabel(App):
    def build(self):
        return Builder.load_string(KV_EXAMPLE)

if __name__ == "__main__":
    TestScrollLabel().run()
