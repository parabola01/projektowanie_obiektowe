program RandomSortNumbers;
uses crt;

const DEFAULT_COUNT = 50;
      DEFAULT_MIN = 0;
      DEFAULT_MAX = 100;

var numbers: array[1..100] of integer;
    i, j, temp, minRange, maxRange, count: integer;

procedure GenerateNumbers(od, do_, ile: integer);
begin
    randomize;
    for i := 1 to ile do
        numbers[i] := random(do_ - od + 1) + od;
end;

procedure SortNumbers(ile: integer);
begin
    for i := 1 to ile - 1 do
        for j := 1 to ile - i do
            if numbers[j] > numbers[j+1] then
            begin
                temp := numbers[j];
                numbers[j] := numbers[j+1];
                numbers[j+1] := temp;
            end;
end;

procedure PrintNumbers(ile: integer);
begin
    for i := 1 to ile do
        write(numbers[i], ' ');
    writeln;
end;


begin
    { Pobieranie parametrów }
    if ParamCount = 3 then
    begin
        val(ParamStr(1), minRange, temp);
        val(ParamStr(2), maxRange, temp);
        val(ParamStr(3), count, temp);
    end
    else
    begin
        minRange := DEFAULT_MIN;
        maxRange := DEFAULT_MAX;
        count := DEFAULT_COUNT;
    end;

    GenerateNumbers(minRange, maxRange, count);
    writeln('Wylosowane liczby:');
    PrintNumbers(count);

    SortNumbers(count);
    writeln('Posortowane liczby:');
    PrintNumbers(count);
end.
