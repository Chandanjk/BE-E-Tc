%MSK
clear all;
close all;
clc;

pi=3.14;
Fc = 935200000;
A=1;
Tb=1; %bit duration
BT=0.3; %BT product of filter
sps=32;
Ts=Tb/sps; %sample period
Fs=1/Ts;
t=0.5;
PSD_MSK=[];
PSD_MSK_db=[];
PSD_GMSK=[];
PSD_GMSK_db=[];
for i=0:1000
    f=i/100;
    %PSD=(1/(2*Fc))*((2*(Fc^2)/pi)*(cos((pi*f)/(2*Fc)))*(sin((pi*f)/Fc))/(((Fc^2)-(f^2))*(cos((pi*f)/Fc))));
    PSD_MSK=((32*(A^2)*Tb)/(pi^2))*((cos((2*pi*f*Tb)))/(1-16*(f^2)*(Tb^2)));
    PSD_MSK_db=[PSD_MSK_db,10*log10(PSD_MSK)];
    PSD_GMSK=((32*(A^2)*Tb)/(pi^2))*((cos((2*pi*f*Tb)))/(1-16*(f^2)*(Tb^2)));
    PSD_GMSK_db=[PSD_GMSK_db,10*log10(PSD_GMSK)];
end

x=(0:1:1000);
plot(x,PSD_MSK_db);
hold on
plot(x,PSD_GMSK_db);