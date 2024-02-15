import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod
from yunear_mc_sdk.event.client_event import ClientEvent
from yunear_mc_sdk.event.server_event import ServerEvent


@Mod.Binding("YunearMcSdk", "0.0.1")
class YunearMcSdk(object):

    def __init__(self, mod_cls=None):
        if mod_cls:
            self.mod = mod_cls()
        self.server = None
        self.client = None

    def __call__(self):
        self.server = serverApi.GetSystem("YunearMcSdk", "YunearMcSdkServer")
        if self.server is None:
            self.server = serverApi.RegisterSystem(
                "YunearMcSdk",
                "YunearMcSdkServer",
                "yunear_mc_sdk.server.yunear_mc_sdk_server.YunearMcSdkServer",
            )
            for attr_name in dir(self.mod):
                event = getattr(self.mod, attr_name)
                if isinstance(event, ServerEvent):
                    event.bind_mod(self.mod)
                    self.server.ListenForEvent(
                        serverApi.GetEngineNamespace(),
                        serverApi.GetEngineSystemName(),
                        event.__class__.__name__,
                        self.mod,
                        event.callback,
                    )
        else:
            self.client = clientApi.RegisterSystem(
                "YunearMcSdk",
                "YunearMcSdkClient",
                "yunear_mc_sdk.client.yunear_mc_sdk_client.YunearMcSdkClient",
            )
            for attr_name in dir(self.mod):
                event = getattr(self.mod, attr_name)
                if isinstance(event, ClientEvent):
                    event.bind_mod(self.mod)
                    self.client.ListenForEvent(
                        clientApi.GetEngineNamespace(),
                        clientApi.GetEngineSystemName(),
                        event.__class__.__name__,
                        self.mod,
                        event.callback,
                    )
