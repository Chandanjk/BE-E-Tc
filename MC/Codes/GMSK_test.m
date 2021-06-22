%GMSK
clear all;
close all;
clc;
nrz_data=[0 1 0 1 0 1 1 0 0 1]; %sample code
pi=3.14;
Tb=1; %bit duration
BT=0.3; %BT product of filter
sps=32; %samples per symbol
Ts=Tb/sps; %sample period
t=0.5;
Tb=(-2*Tb:Ts:2*Tb);
alpha=2*pi*BT/(sqrt(log(2)))
gauss=(alpha*(2*t-0.5))-(alpha*(2*t+0.5));
K=pi/2;
gauss=K*gauss;
nrz=upsample(nrz_data,sps);
nrz_gauss=conv(gauss,nrz);
subplot(3,1,1);
stem(nrz_data);
title('sample input data');
xlabel('time');
ylabel('amp');

subplot(3,1,2);
stem(nrz);
title('upsampled input data');
xlabel('time');
ylabel('amp');

subplot(3,1,3);
plot(nrz_gauss);
title('gmsk output');
xlabel('time');
ylabel('amp');

nrz_gauss1 = cumsum(nrz_gauss);
nrz_gauss2 = exp(1i*nrz_gauss1);
noisy_real1 = real(nrz_gauss2);
noisy_imag1 = imag(nrz_gauss2);
%filter_noisy_real1 = matched_filter(noisy_real1,Tb,sps);
%ilter_noisy_imag1 = matched_filter(noisy_imag1,Tb,sps);


