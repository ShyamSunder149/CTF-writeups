# Web 

## inspector

inspect the source code to get the flag

```

picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}

```

## where are the robots

modify url to access robots.txt and there it showed up that it disallows 1bb4c.html and modify url with that and get the flag

```

picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}

```

## logon

go to the cookies of the site and modify the admin value to true to get the flag

```

picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}

```

## dont use client side

decode the javascript given in the source code

```

picoCTF{no_clients_plz_b706c5}

```

## scavenger hunt

an upgraded version of inspector.. there are totally 5 parts of the flag. first part in html. second part is css. searching for the third part in js there is a hint indexing which means we should check on robots.txt . for the fourth part there is a hint in robots.txt that its an apache server so we should check .htaccess. for the fifth part there is a hint in .htaccess that websites developed in mac so we should check .DS_Store

```

picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_fa04427c}

```


