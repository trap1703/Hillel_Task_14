# Hillel_Task_14
 Домашнее задание 14
Добавлено: 19.02.2020 12:33
process your infrastructure parameters

напишите boto3 скрипт, который будет менять параметры asg: min/max/desired capacity.
на вход скрипт должен получать имя ASG, и параметр который ему нужно изменить.
используйте библиотеку argparse для передачи параметров при вызове скрипта, типа

$ my_script.py --name "asg_name" [--min 2] [--max 5] [--descap 3]

скобками обозначены необязательные параметры. при вводе только имени АСГ, 
скрипт должен выводить текущие состояния параметров, которые вы можете изменить этим скриптом.

В случае отсутствия параметров [--min 2] [--max 5] [--descap 3] присваивается значение по умолчанию = 10
Параметр --name обязателен.
Вывод работы программы:
trap@trap-VirtualBox:~/PycharmProjects/boto$ python3 task14.py --name asg44 --min 3 --max 6 --descap 4
run programm
Apply new parametrs min,max and descap parametrs
New parametrs for ASG :  asg44
Max size group  :  6
Min size group  :  3
descap size group  :  4
trap@trap-VirtualBox:~/PycharmProjects/boto$ python3 task14.py --name asg44
Not input min and max parametrs
Curent parametrs for ASG :  asg44
Max size group  :  6
Min size group  :  3
descap size group  :  4
trap@trap-VirtualBox:~/PycharmProjects/boto$ python3 task14.py --name asg44 --min 2 --max 4 --descap 3
run programm
Apply new parametrs min,max and descap parametrs
New parametrs for ASG :  asg44
Max size group  :  4
Min size group  :  2
descap size group  :  3
trap@trap-VirtualBox:~/PycharmProjects/boto$ 
