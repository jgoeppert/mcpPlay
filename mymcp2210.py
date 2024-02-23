from mcp2210 import Mcp2210, Mcp2210GpioDesignation, Mcp2210GpioDirection
class myMcp2210(Mcp2210):

    def configure_spi_timing(self
        , chip_select_to_data_delay: int = None
        , last_data_byte_to_cs: int = None
        , delay_between_bytes: int = None
        , bit_rate: int = None
    ):
    
        if chip_select_to_data_delay is not None:
            self._spi_settings.chip_select_to_data_delay = chip_select_to_data_delay
        if last_data_byte_to_cs is not None:
            self._spi_settings.last_data_byte_to_cs_delay = last_data_byte_to_cs
        if delay_between_bytes is not None:
            self._spi_settings.delay_between_bytes = delay_between_bytes
        if bit_rate is not None:
            self._spi_settings.bit_rate = bit_rate
        self._set_spi_configuration()

    def get_config_spi_timing(self):
        return [
            self._spi_settings.chip_select_to_data_delay
          , self._spi_settings.last_data_byte_to_cs_delay
          , self._spi_settings.delay_between_bytes
          , self._spi_settings.bit_rate
        ]



# self._spi_settings.chip_select_to_data_delay
# self._spi_settings.last_data_byte_to_cs_delay
# self._spi_settings.delay_between_bytes
# self._spi_settings.bit_rate
