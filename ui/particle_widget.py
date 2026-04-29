import random
import math
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QTimer, Qt, QPointF

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.radius = random.uniform(1, 3)
        self.base_radius = self.radius

    def update(self, volume=0):
        self.x += self.vx
        self.y += self.vy
        
        # Sınır kontrolü
        if self.x < 0 or self.x > 400: self.vx *= -1
        if self.y < 0 or self.y > 400: self.vy *= -1
        
        # Ses şiddetine göre titreşim
        self.radius = self.base_radius + (volume * 10)

class ParticleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 400)
        self.particles = [Particle(random.uniform(0, 400), random.uniform(0, 400)) for _ in range(100)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(30)
        self.volume = 0 # 0 ile 1 arası ses şiddeti

    def set_volume(self, volume):
        self.volume = volume

    def update_particles(self):
        for p in self.particles:
            # Merkeze çekim kuvveti (dairesel küme için)
            dx = 200 - p.x
            dy = 200 - p.y
            dist = math.sqrt(dx**2 + dy**2)
            if dist > 150:
                p.vx += dx * 0.001
                p.vy += dy * 0.001
            
            p.update(self.volume)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(30, 30, 30)) # Uzay Siyahı

        for p in self.particles:
            painter.setBrush(QColor(0, 150, 255, 150))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(QPointF(p.x, p.y), p.radius, p.radius)
            
            # Yakın parçacıklar arası çizgi
            for p2 in self.particles:
                d = math.sqrt((p.x-p2.x)**2 + (p.y-p2.y)**2)
                if d < 30:
                    painter.setPen(QPen(QColor(0, 150, 255, int(255 * (1 - d/30))), 1))
                    painter.drawLine(QPointF(p.x, p.y), QPointF(p2.x, p2.y))