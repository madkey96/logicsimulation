clear;
clc;
// Reading from file
fid = mopen('output.txt', 'r');
if (fid == -1) then
    error("cannot open file");
end
flines = mgetl(fid);
mclose(fid);
N = strtod(flines(1));
a = list();
for i = 2:size(flines, 1)
    t = strsplit(flines(i), ' ');
    b = list();
    for j=1:size(t,1)
        if isdigit(t(j)) then
            b($+1)=strtod(t(j));
        end
    end
    a($+1)=b;
end

// Storing the values from file
inputs = a(1);
output = a(2);

// Creating empty nodes
nodes = list();
temp = list(0,0);
for i=1:N
    nodes(i) = temp;
end

// Updating the node values according to the circuit
for i=3:size(a)
    index = a(i)(2);
    gate = a(i)(1);
    child = list();
    for j=3:size(a(i))
        child($+1)=a(i)(j);
    end
    nodes(index)(1)=gate;
    nodes(index)($+1)=child;
end

// Doing breadth first traversal to find the order
bfs = output;
count = 0;
while count<size(bfs),
    index = bfs(count+1);
    if nodes(index)(1)<>0 then
        for i=1:size(nodes(index)(3))
            for k=1:size(bfs)
                if bfs(k)==nodes(index)(3)(i) then
                    bfs(k)=null();
                    break;
                end
            end
            bfs($+1)=nodes(index)(3)(i);
        end
    end
    count = count+1;
end

// Reversing the breadth first order
bfsr = list()
for e=size(bfs):-1:1
    bfsr($+1)=bfs(e);
end

// Loop
while 1,
    // Taking inputs
    flag = 0;
    while flag==0,
        disp("Give space separated inputs for nodes ");
        disp(flines(2));
        x = input(" ", "string");
        y = strsplit(x, " ");
        if size(y,1)==size(inputs) then
            flag = 1;    
        end    
    end

    i = 1;
    for e=a(1)
        nodes(e)(2) = strtod(y(i))<>0;
        i = i+1;
    end
    
    // Evaluating the circuit
    for e=bfsr
        select nodes(e)(1)
        case 0 then
        case 1 then
            // AND gate
            nodes(e)(2)=1|1;
            for j=nodes(e)(3)
                nodes(e)(2) = nodes(j)(2)&nodes(e)(2);
            end
        case 2 then
            // OR gate
            nodes(e)(2)=0&0;
            for j=nodes(e)(3)
                nodes(e)(2) = nodes(j)(2)|nodes(e)(2);
            end
        case 3 then
            // NAND gate
            nodes(e)(2)=1|1;
            for j=nodes(e)(3)
                nodes(e)(2) = nodes(j)(2)&nodes(e)(2);
            end
            nodes(e)(2)=~nodes(e)(2);
        case 4 then
            // NOR gate
            nodes(e)(2)=0&0;
            for j=nodes(e)(3)
                nodes(e)(2) = nodes(j)(2)|nodes(e)(2);
            end
            nodes(e)(2)=~nodes(e)(2);
        case 5 then
            // NOT gate
            for j=nodes(e)(3)
                nodes(e)(2) = ~nodes(j)(2);
            end
        case 6 then
            // XOR gate
            nodes(e)(2)=0&0;
            for j=nodes(e)(3)
                if nodes(e)(3) then
                    nodes(e)(2) = ~nodes(j)(2);
                else
                    nodes(e)(2) = nodes(j)(2);
                end
            end
        case 7 then
            // NXOR gate
            nodes(e)(2)=0&0;
            for j=nodes(e)(3)
                if nodes(e)(3) then
                    nodes(e)(2) = ~nodes(j)(2);
                else
                    nodes(e)(2) = nodes(j)(2);
                end
            end
            nodes(e)(2)=~nodes(e)(2);
        case 8 then
            // BUFFER
            for j=nodes(e)(3)
                nodes(e)(2) = nodes(j)(2);
            end
        else
            error("There is a gate that I dont know");
        end
    end
    
    disp("Order of Evaluation and their outputs");
    for w=bfsr
        disp("  "+string(w)+"  " + string(nodes(w)(2)) );
    end

    disp("The required outputs are:")
    for e = output
        disp(string(e)+">>>"+string(nodes(e)(2)));
    end
end
