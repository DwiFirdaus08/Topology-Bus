import random
import time

class BusTopology:
    def __init__(self):
        self.devices = ["Penerima 1", "Penerima 2", "Penerima 3"]

    def is_ready(self):
        """Menghasilkan True atau False secara acak untuk mensimulasikan apakah perangkat siap menerima data."""
        return random.choice([True, False])

    def send_data(self, sender, data):
        print(f"\n{sender} mengirim data: '{data}' ke bus...")
        time.sleep(1)  # Simulasi jeda waktu pengiriman

        data_delivered = False

        # Cek setiap penerima apakah siap
        for device in self.devices:
            ready_status = self.is_ready()
            if ready_status:
                print(f"{device} siap menerima data.")
            else:
                print(f"{device} tidak siap. Mencoba perangkat berikutnya...")

            if ready_status:
                print(f"Data '{data}' berhasil diterima oleh {device}!")
                data_delivered = True
                self.log_status(data, device)
                break
            time.sleep(1)  # Simulasi waktu pengecekan

        if not data_delivered:
            print(f"Tidak ada penerima yang siap. Pengiriman data '{data}' gagal.")
            self.log_status(data, "Gagal - Tidak ada penerima siap")

    def log_status(self, data, status):
        """Menyimpan log aktivitas pengiriman data ke dalam file."""
        with open("log.txt", "a") as log_file:
            log_file.write(f"Data: '{data}' - Status: {status}\n")


# Contoh Penggunaan:
bus = BusTopology()

print("=== SIMULASI TOPOLOGI BUS ===")
data_to_send = input("Masukkan data yang ingin dikirim: ").strip()

if data_to_send:
    bus.send_data("Pengirim", data_to_send)
else:
    print("Data tidak boleh kosong. Silakan masukkan data yang ingin dikirim.")
