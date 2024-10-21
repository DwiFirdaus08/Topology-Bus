import random
import time

class BusTopology:
    def __init__(self):
        self.devices = {
            "Penerima 1": {"status": "ready", "is_broken": False},
            "Penerima 2": {"status": "ready", "is_broken": False},
            "Penerima 3": {"status": "ready", "is_broken": False}
        }

    def randomize_device_failure(self):
        """Mensimulasikan kemungkinan Penerima 1 rusak."""
        self.devices["Penerima 1"]["is_broken"] = random.choice([True, False])

    def is_ready(self, device_name):
        """Menghasilkan True atau False berdasarkan apakah perangkat siap atau rusak."""
        device = self.devices[device_name]
        if device["is_broken"]:
            return False  # Jika rusak, langsung False
        # Simulasi status penerima: "ready" atau "busy"
        device["status"] = random.choice(["ready", "busy"])
        return device["status"] == "ready"

    def send_data(self, sender, data):
        print(f"\n{sender} mengirim data: '{data}' ke bus...")
        time.sleep(1)  # Simulasi jeda waktu pengiriman

        # apakah Penerima 1 rusak atau tidak
        self.randomize_device_failure()

        # Cek status Penerima 1 dulu
        if self.devices["Penerima 1"]["is_broken"]:
            print("Penerima 1 rusak, tidak dapat menerima data.")
            self.log_status(data, "Gagal - Penerima 1 rusak")
            return  # Jika rusak, tidak lanjut ke penerima lain

        for device_name in self.devices:
            if self.is_ready(device_name):
                print(f"{device_name} siap menerima data.")
                print(f"Data '{data}' berhasil diterima oleh {device_name}!")
                self.log_status(data, device_name)
                return  # Data berhasil diterima, berhenti di sini
            else:
                print(f"{device_name} tidak siap, mengalihkan ke penerima berikutnya...")

        # Jika tidak ada penerima yang siap
        print(f"Tidak ada penerima yang siap. Pengiriman data '{data}' gagal.")
        self.log_status(data, "Gagal - Semua penerima sibuk atau tidak siap")

    def log_status(self, data, status):
        """Menyimpan log aktivitas pengiriman data ke dalam file."""
        with open("log.txt", "a") as log_file:
            log_file.write(f"Data: '{data}' - Status: {status}\n")

bus = BusTopology()

print("=== SIMULASI TOPOLOGI BUS ===")
data_to_send = input("Masukkan data yang ingin dikirim: ").strip()

if data_to_send:
    bus.send_data("Pengirim", data_to_send)
else:
    print("Data tidak boleh kosong. Silakan masukkan data yang ingin dikirim.")
