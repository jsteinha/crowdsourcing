%ops = sdpsettings('solver','sedumi','sedumi.eps',1e-2,'sedumi.maxiter',20);
%n = 40;
%ds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
%nucs = zeros(1,length(ds));
for i=21:39
    ds(i) = i;
    nucsM = zeros(1,5);
    for j=1:5
        nucsM(j) = nuc(n,ds(i));
    end
    nucs(i) = mean(nucsM);
end