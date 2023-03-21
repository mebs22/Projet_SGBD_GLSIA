// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
class SupReservation extends StatefulWidget {
  const SupReservation({Key? key}) : super(key: key);

  @override
  State<SupReservation> createState() => _SupReservationState();
}

class _SupReservationState extends State<SupReservation> {
  final _formKey= GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Supprimmer une réservation'),
        backgroundColor: Colors.green,

        centerTitle: true,
      ),
      body: Container(
        margin: EdgeInsets.all((20)),
        child: Form(
          key: _formKey,

          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(
                  labelText: 'Numero Client ',
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


              // ignore: prefer_const_constructors
              Padding(padding: EdgeInsets.all(30)),
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
              ),
              Padding(padding: EdgeInsets.all(30)),

              SizedBox(
                width: double.infinity,
                height: 50,
                child: ElevatedButton(
                  style: const ButtonStyle(
                      backgroundColor: MaterialStatePropertyAll(Colors.green)),
                  onPressed: (){
                    if(_formKey.currentState!.validate()){
                      ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(content: Text("Suspression en cours..."))
                      );
                      FocusScope.of(context).requestFocus(FocusNode());
                    }
                  },
                  child:Text('Supprimer'),


                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
