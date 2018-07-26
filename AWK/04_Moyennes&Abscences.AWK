#!/usr/bin/awk -f

#Definitions des separateurs de champs et de lignes
BEGIN{
  FS=" ";
  RS="\n";

  nb_exam=6;

  # initialisation
  # nb_eleves_a_exam_i => |0|0|0|0|0|0|
  # sum_notes_exam => |0|0|0|0|0|0|
  for(i=0;i<nb_exam;i++){
    nb_eleves_a_exam_i[i]=0;
    sum_notes_exam[i]=0;
  }
  
  # tableau avec un nombre de cases égal au nombre de lignes (soit le nombre d'étudiants)
  # TODO
}

/abs/{
  abs_counter=0;
  for(k=0;k<nb_exam;k++){
    if($(k+3)=="abs"){
      abs_counter++;
    }
  }

  printf $1"/"$2" : " abs_counter "absence(s)\n";
  # mettre à jour (remplir) la bonne case du tableau
}

{
  for(i=0;i<nb_exam;i++){ 
    if($(i+3)!="abs"){
      nb_eleve_a_exam_i[i]=nb_eleve_a_exam_i[i]+1;
      sum_notes_exam[i]=sum_notes_exam[i]+$(i+3); 
      #printf "note exam "i" : "$(i+3)". nb eleve à l'exam : "nb_eleve_a_exam_i[i]  ". somme des notes : " sum_notes_exam[i] ".\n"  #Cette ligne si tu la décommente te permettera de voir l'evolution des valeurs de chacune des variables pour mieu comprendre.
    }  
  }
}

END{
  for(i=0;i<nb_exam;i++){
    if(nb_eleve_a_exam_i[i]!=0){
      indice = i + 1
      printf "moyenne à l'examen "indice" : "sum_notes_exam[i]/nb_eleve_a_exam_i[i]"\n" ;
    }else{
      printf "Aucun élève présent à cet examen\n"
    }
    for(j=0;j<sum_notes_exam[i]/nb_eleve_a_exam_i[i];j++){
      printf "*"
    }
    printf "\n"
  }  
  print "\nExit";
  exit 0;
}
