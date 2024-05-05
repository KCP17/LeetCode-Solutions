# @param {String} s
# @return {Boolean}
def halves_are_alike(s)
    half = s.length / 2
    count = 0
    for i in 0..half-1
        count += 1 if 'ueoai'.include?(s[i].downcase)
        count -= 1 if 'ueoai'.include?(s[i + half].downcase)
    end
    return count == 0
end
