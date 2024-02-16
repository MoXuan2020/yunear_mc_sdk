import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod
from yunear_mc_sdk.event.client_event import ClientEvent
from yunear_mc_sdk.event.server_event import ServerEvent


@Mod.Binding("YunearMcSdk", "0.0.1")
class YunearMcSdk(object):

    def __init__(self, mod_cls=None):
        self.mod_cls = mod_cls
        self.mod = None
        self.server = None
        self.client = None

    def __call__(self):
        if self.mod is None:
            self.mod = self.mod_cls()
            self.server = serverApi.GetSystem("YunearMcSdk", "YunearMcSdkServer")
            if self.server is None:
                self.server = serverApi.RegisterSystem(
                    "YunearMcSdk",
                    "%sServer" % self.mod.__class__.__name__,
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
            self.client = clientApi.RegisterSystem(
                "YunearMcSdk",
                "%sClient" % self.mod.__class__.__name__,
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
