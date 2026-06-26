from audio_sensor import AudioSensor
from noise_analyzer import NoiseAnalyzer
from alert_system import AlertSystem
from analytics import AnalyticsManager

sensor = AudioSensor()
analyzer = NoiseAnalyzer()
alert = AlertSystem()
analytics = AnalyticsManager()

while True:

    noise = sensor.get_noise_level()

    status = analyzer.analyze_noise(noise)

    print("Noise Level:", noise)
    print("Status:", status)

    analytics.save_data(noise, status)

    if analyzer.is_dangerous(noise):
        alert.show_alert()