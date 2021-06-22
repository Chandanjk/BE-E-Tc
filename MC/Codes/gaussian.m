%GMSK
clear all;
close all;
clc;
nrz_data=[0 1 0.5 1 0 0.5 0.5]; %sample code
pi=3.14;
Tb=1; %bit duration
BT=0.3; %BT product of filter
sps=32;
Ts=Tb/sps; %sample period
t=0.5;
Tb=(-2*Tb:Ts:2*Tb);
alpha=2*pi*BT/(sqrt(log(2)));
gauss=(alpha*(2*t-0.5))-(alpha*(2*t+0.5));
K=pi/2;
gauss=K*gauss;
nrz=upsample(nrz_data,sps);
nrz_gauss=conv(gauss,nrz);
subplot(2,1,1);
stem(nrz_data);
title('sample input data');
xlabel('time');
ylabel('amp');
subplot(2,1,2);
plot(nrz_gauss);
title('gmsk output');
xlabel('time');
ylabel('amp');