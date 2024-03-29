# Detector-of-intrusion-which-sends-email-as-an-alert
```
git clone https://github.com/Hasul79/Detector-of-intrusion-which-sends-email-as-an-alert.git
cd Detector-of-intrusion-which-sends-email-as-an-alert
sudo python Email.py

```
<br>

<h1>Этот код написан на Python с использованием библиотеки  Scapy для анализа сетевого трафика и <u>termcolor</u> для цветного вывода в консоли.</h1>

<ol>
  <li>Импорт библиотек:</li>
   
  <ul>
    <li>from scapy.all import sniff, IP, TCP: Импорт функции sniff и классов IP и TCP из библиотеки Scapy для анализа сетевых пакетов.</li>
    <li>import smtplib: Импорт модуля для отправки электронной почты.</li>
    <li>from termcolor import cprint: Импорт функции cprint для цветного вывода в консоли.</li>
    <li>import sys: Импорт модуля sys для использования функции sys.exit().</li>
  </ul>
  <li>Инициализация переменных:</li>
  <ul>
   <li>cprint('Sniffing...', 'yellow'): Вывод в консоль сообщения "Sniffing..." желтым цветом.</li>
   <li>syn_count, failed_attempts = 0, {}: Инициализация переменных syn_count и failed_attempts для отслеживания количества синхронных (SYN) пакетов и неудачных попыток соединения. </li>
   </ul>
  <li>Функция send_email(subject, body):</li>
  <ul>
    <li>Отправляет электронное письмо с указанным заголовком (subject) и телом (body) через SMTP-сервер Gmail.</li>
  </ul>
  <li>Функция detect_scan(pkt):</li>
  <ul>
    <li>Анализирует каждый захваченный сетевой пакет.</li>
    <li>Если пакет содержит TCP-слои и установлен флаг SYN (пакет начала соединения), увеличивается счетчик syn_count. Если счетчик превышает 10, программа считает это сканированием и отправляет уведомление по электронной почте.</li>
    <li>Если пакет содержит TCP-слои с портом 22 (SSH), программа отслеживает неудачные попытки аутентификации. Если количество неудачных попыток от одного источника превышает 3, программа считает это попыткой подбора пароля и отправляет уведомление по электронной почте.</li>
  </ul>
  <li>Основной блок кода if __name__ == '__main__':</li>
  <ul>
    <li>sniff(prn=detect_scan, filter='tcp', store=0): Запускает захват сетевого трафика с использованием функции detect_scan в качестве обработчика. Захватываются только TCP-пакеты, и результаты не сохраняются (store=0).</li>
  </ul>
</ol>
<br>
<h3>Программа создана для мониторинга сетевого трафика и обнаружения потенциальных атак, таких как сканирование портов и попытки подбора пароля по SSH. В случае обнаружения таких событий программа отправляет уведомления на заданный адрес электронной почты.
</h3>
<br>

![Screenshot 2024-03-05 180829](https://github.com/Hasul79/Detector-of-intrusion-which-sends-email-as-an-alert/assets/95657084/8cf56c97-14f4-40a7-977b-3c7d5267b3e2)

<br>

![Screenshot 2024-03-04 180305](https://github.com/Hasul79/Detector-of-intrusion-which-sends-email-as-an-alert/assets/95657084/7dc5f06f-e435-4d27-99ae-92bd0452e5a9)

<br>

# Author: Hasmik Minasyan
