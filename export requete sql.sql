--SELECT * FROM ventes;
--REQUETE 1
select sum(c3*c4) as chiffre_affaire_total from ventes;
--REQUETE 2
select c2 as produit, sum (c4) as vente_par_produit from ventes group by c2;
--REQUETE 3
select c5 as region,sum (4) as vente_par_region from ventes group by c5;