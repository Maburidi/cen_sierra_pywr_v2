from sierra.base_parameters import MinFlowParameter

from sierra.utilities.converter import convert


class IFR_bl_NF_Stanislaus_Div_Res_Min_Requirement(MinFlowParameter):
    """"""

    initial_value = 16.5 / 35.31

    def _value(self, timestep, scenario_index):
        ifr_val = self.initial_value # cfs to cms (16.5 cfs)
        if self.model.mode == 'scheduling':
            ifr_val = self.get_down_ramp_ifr(timestep, scenario_index, ifr_val, initial_value=ifr_val, rate=0.25)
        if self.model.mode == 'planning':
            ifr_val *= self.days_in_month
        return ifr_val

    def value(self, timestep, scenario_index):
        val = self.requirement(timestep, scenario_index, default=self._value)
        return convert(val, "m^3 s^-1", "m^3 day^-1", scale_in=1, scale_out=1000000.0)

    @classmethod
    def load(cls, model, data):
        return cls(model, **data)


IFR_bl_NF_Stanislaus_Div_Res_Min_Requirement.register()
