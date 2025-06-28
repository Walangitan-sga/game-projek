import pygame
import time
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
lebar_layar = 600
tinggi_layar = 400

# Warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
merah = (255, 0, 0)
hijau = (0, 255, 0)
biru = (0, 0, 255)

# Ukuran blok ular
ukuran_blok = 20
kecepatan = 15

# Font
font = pygame.font.SysFont(None, 35)

# Layar
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption('Game Ular Python')

# Fungsi untuk menampilkan skor
def tampilkan_skor(skor):
    teks = font.render(f"Skor: {skor}", True, putih)
    layar.blit(teks, [0, 0])

# Fungsi utama game
def game_ular():
    game_over = False
    game_keluar = False

    x = lebar_layar / 2
    y = tinggi_layar / 2

    x_perubahan = 0
    y_perubahan = 0

    ular = []
    panjang_ular = 1

    makanan_x = round(random.randrange(0, lebar_layar - ukuran_blok) / 20.0) * 20.0
    makanan_y = round(random.randrange(0, tinggi_layar - ukuran_blok) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_keluar:

        while game_over:
            layar.fill(hitam)
            pesan = font.render("Game Over! Tekan Q untuk keluar, C untuk main lagi", True, merah)
            layar.blit(pesan, [lebar_layar / 6, tinggi_layar / 3])
            tampilkan_skor(panjang_ular - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_keluar = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_keluar = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_ular()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_keluar = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_perubahan = -ukuran_blok
                    y_perubahan = 0
                elif event.key == pygame.K_RIGHT:
                    x_perubahan = ukuran_blok
                    y_perubahan = 0
                elif event.key == pygame.K_UP:
                    y_perubahan = -ukuran_blok
                    x_perubahan = 0
                elif event.key == pygame.K_DOWN:
                    y_perubahan = ukuran_blok
                    x_perubahan = 0

        if x >= lebar_layar or x < 0 or y >= tinggi_layar or y < 0:
            game_over = True

        x += x_perubahan
        y += y_perubahan

        layar.fill(hitam)
        pygame.draw.rect(layar, hijau, [makanan_x, makanan_y, ukuran_blok, ukuran_blok])

        kepala_ular = []
        kepala_ular.append(x)
        kepala_ular.append(y)
        ular.append(kepala_ular)

        if len(ular) > panjang_ular:
            del ular[0]

        for segmen in ular[:-1]:
            if segmen == kepala_ular:
                game_over = True

        for segmen in ular:
            pygame.draw.rect(layar, biru, [segmen[0], segmen[1], ukuran_blok, ukuran_blok])

        tampilkan_skor(panjang_ular - 1)
        pygame.display.update()

        if x == makanan_x and y == makanan_y:
            makanan_x = round(random.randrange(0, lebar_layar - ukuran_blok) / 20.0) * 20.0
            makanan_y = round(random.randrange(0, tinggi_layar - ukuran_blok) / 20.0) * 20.0
            panjang_ular += 1

        clock.tick(kecepatan)

    pygame.quit()
    quit()

# Jalankan game
game_ular()

