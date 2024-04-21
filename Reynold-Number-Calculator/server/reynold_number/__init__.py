from reynold_number.FluidAttributes import FluidAttributes

# Nu kinematic visc
# Mu dynamic visc

air_at_15C = FluidAttributes(p=1.225, nu=0.000014776, mu=0.0000181)
air_at_25C = FluidAttributes(p=1.184, nu=0.00001571, mu=0.0000186)

water_at_10C = FluidAttributes(p=999.7, nu=0.0000013084, mu=0.001308)
water_at_50C = FluidAttributes(p=998, nu=5.537e-7, mu=0.0005471)
water_at_90C = FluidAttributes(p=965.3, nu=3.263e-7, mu=0.000315)