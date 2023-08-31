import trig_calculator

class TestTrig:
    
    
    @staticmethod
    def test_calculate_sin():
        assert trig_calculator.calculate_sin(90) == 1
    
    @staticmethod
    def test_calculate_cos():
        assert trig_calculator.calculate_cos(90) == 0
    
    @staticmethod
    def test_calculate_tan():
        assert trig_calculator.calculate_tan(45) == 1
    