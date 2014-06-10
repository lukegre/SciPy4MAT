function happy_birthday()

song = sing_hb('Jacob')

end


function song = sing_hb(name)
song = {};
hb = 'Happy birthday';
for i = 1:4
    if i ~= 3
        song{i} = sprintf('%s to you,',hb);
    else
        song{i} = sprintf('%s dear %s,', hb, name);
    end
end
song = char(song);
end