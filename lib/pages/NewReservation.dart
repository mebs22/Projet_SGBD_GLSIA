// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
class AjoutReservation extends StatefulWidget {
  const AjoutReservation({Key? key}) : super(key: key);

  @override
  State<AjoutReservation> createState() => _AjoutReservationState();
}

class _AjoutReservationState extends State<AjoutReservation> {
  final _formKey= GlobalKey<FormState>();
  TextEditingController numero = TextEditingController();
  TextEditingController nuite = TextEditingController();
  @override
  void dispose() {
    // TODO: implement dispose
    super.dispose();
    numero.dispose();
    nuite.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Ajouter une réservation'),
        backgroundColor: Colors.green,
        centerTitle: true,
      ),
      body:
      Container(
        margin: EdgeInsets.all((10)),

        child: Form(
          child: Column(
            children: [


              TextFormField( decoration: InputDecoration(
                labelText: 'Prenom  Client ',
                border: OutlineInputBorder(),
              ),
                validator: (value){
                  if (value == null || value.isEmpty){
                    return "Tu dois completer ce texte";
                  }
                  return null;
                },
              ),
              Padding(padding: EdgeInsets.all(5)),
              TextFormField( decoration: InputDecoration(
                labelText: 'nom  Client ',
                border: OutlineInputBorder(),
              ),
                validator: (value){
                  if (value == null || value.isEmpty){
                    return "Tu dois completer ce texte";
                  }
                  return null;
                },
              ),
              Padding(padding: EdgeInsets.all(5)),
              TextFormField( decoration: InputDecoration(
                labelText: 'numero Client ',
                hintText: 'Entrer le numero du client',
                border: OutlineInputBorder(),
              ),
                keyboardType: TextInputType.number,
                validator: (value){
                  if (value == null || value.isEmpty){
                    return "Tu dois completer ce texte";
                  }
                  return null;
                },
              ),
              Padding(padding: EdgeInsets.all(7)),
              TextFormField( decoration: InputDecoration(
                labelText: 'Numero Chambre ',
                hintText: 'Entrer la chambre choisie par le client',
                border: OutlineInputBorder(),
              ),
                keyboardType: TextInputType.number,
                validator: (value){
                  if (value == null || value.isEmpty){
                    return "Tu dois completer ce texte";
                  }
                  return null;
                },
                controller: numero,
              ),
              // ignore: prefer_const_constructors
              Padding(padding: EdgeInsets.all(5)),
              TextFormField( decoration: InputDecoration(
                labelText: 'Nuité ',
                hintText: 'Nombre de jours',
                border: OutlineInputBorder(),
              ),
                keyboardType: TextInputType.number,
                validator: (value){
                  if (value == null || value.isEmpty){
                    return "Tu dois completer ce texte";
                  }
                  return null;
                },
                controller: nuite,
              ),
              Padding(padding: EdgeInsets.all(5)),


              SizedBox(
                height: 50,
                width: double.infinity,
                child: ElevatedButton(
                  style: ButtonStyle(
                      backgroundColor: MaterialStatePropertyAll(Colors.green)),
                    onPressed: (){
                      if(_formKey.currentState!.validate()){
                        int Numero= int.parse(numero.text) ;
                        int Nuite= int.parse(nuite.text);
                        ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(content: Text("Ajout en cours..."))
                        );
                        FocusScope.of(context).requestFocus(FocusNode());
                      print(Nuite);
                      }
                    },
                    child:Text('Enregistrer'),


                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
