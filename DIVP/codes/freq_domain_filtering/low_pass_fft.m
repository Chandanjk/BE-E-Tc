%code for low pass filter
clc;
clear all;
close all;

a=imread('einstein.jpg');

c=size(a);
N=c(1);
vv=fft2(a);
vc=fftshift(vv);

D0=input('Enter cutoff frequency'); 
for u=1:1:c(1)		%Generate mask
    for v=1:1:c(2)
        D=((u-(N/2))^2+(v-(N/2))^2)^0.5;
        if D<D0;
            H(u,v)=1;
        else
            H(u,v)=0;
        end;
    end;
end;

x=vc.*H;			% Multiplication with mask
X=abs(ifft2(x));

figure(1),imshow(uint8(a));
figure(2),mesh(H);
figure(3),imshow(uint8(X));
figure(4),imagesc(H),colormap(gray);