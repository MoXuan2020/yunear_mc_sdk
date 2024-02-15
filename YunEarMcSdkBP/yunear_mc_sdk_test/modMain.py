# pylint: disable = invalid-name
from yunear_mc_sdk import YunearMcSdk
from yunear_mc_sdk.event.world.on_script_tick_client import OnScriptTickClient


@YunearMcSdk
class YunearMcSdkTest(object):

    @OnScriptTickClient
    def OnScriptTickClient(self, args):
        print(args)
