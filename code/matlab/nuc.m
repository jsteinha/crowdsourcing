function r=nuc(n,d)
    A = (d/n) * sign(rand(n,n)-0.5);
    Ahat = sign(A) .* logical(rand(n,n) < d/n);
    D = Ahat - A;
    M = sdpvar(n,n,'full');
    Obj = -trace(D'*M);
    Con = [M(:)>=0];
    Con = [Con;sum(M,2)<=ones(n,1)];
    Con = [Con;norm(M,'nuclear')<=2];
    solvesdp(Con,Obj);
    disp(-double(Obj));
    r=-double(Obj);
end