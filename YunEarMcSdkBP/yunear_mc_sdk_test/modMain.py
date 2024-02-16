# pylint: disable = invalid-name
from yunear_mc_sdk import YunearMcSdk
from yunear_mc_sdk.event.control.client_jump_button_press_down_event import (
    ClientJumpButtonPressDownEvent,
)


@YunearMcSdk
class YunearMcSdkTest(object):

    @ClientJumpButtonPressDownEvent
    def client_jump_button_press_down_event(self, event):
        # type: (ClientJumpButtonPressDownEvent) -> None
        event.args["continueJump"] = False
