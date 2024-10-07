from parameters import WaterLPParameter

from utilities.converter import convert

class MID_Main_Observed_Delivery(WaterLPParameter):
    """"""

    def _value(self, timestep, scenario_index):

        return self.read_csv("Management/BAU/Demand/MID_Main_Diversion_cfs.csv", index_col=0, header=0, squeeze=True)[timestep.datetime] / 35.31

    def value(self, timestep, scenario_index):
        return convert(self._value(timestep, scenario_index), "m^3 s^-1", "m^3 day^-1", scale_in=1, scale_out=1000000.0)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)
        
MID_Main_Observed_Delivery.register()
print(" [*] MID_Main_Observed_Delivery successfully registered")
