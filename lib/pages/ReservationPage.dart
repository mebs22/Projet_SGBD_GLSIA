import 'package:flutter/material.dart';
import 'package:gestion_hotel/pages/ListeReservation.dart';
import 'package:gestion_hotel/pages/NewReservation.dart';
import 'package:gestion_hotel/pages/SupReservation.dart';

class ReservationPage extends StatelessWidget {
  const ReservationPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(

        title: const Text(
          "GESTION RESERVATION :", ),
        backgroundColor: Colors.green,

        centerTitle: true,
      ),
    body: Center(
      child: Column (
        children: [

          Padding(padding: EdgeInsets.all(30)),
          ElevatedButton.icon(
            style: ButtonStyle(
                fixedSize:  MaterialStateProperty.all(Size(200, 50)),
                backgroundColor: MaterialStatePropertyAll(Colors.green)
            ),
            onPressed:  () {
              Navigator.push(
                  context,
                  PageRouteBuilder(
                      pageBuilder: (_,__,___) =>const ListeReservation()
                  )
              );
            },
            label: const Text("Voir les reservations"),
            icon: Icon(Icons.remove_red_eye_outlined),

          ), Padding(padding: EdgeInsets.all(45)),
          ElevatedButton.icon(
            style: ButtonStyle(
                fixedSize:  MaterialStateProperty.all(Size(200, 50)),
                backgroundColor: MaterialStatePropertyAll(Colors.green)
            ),
            onPressed:  () {
              Navigator.push(
                  context,
                  PageRouteBuilder(
                      pageBuilder: (_, __, ___) => const AjoutReservation())
              );
            },
            label: const Text("Nouvelle reservation"),
            icon: Icon(Icons.add),

          ),
    Padding(padding: EdgeInsets.all(45)),
          ElevatedButton.icon(
            style: ButtonStyle(
                fixedSize:  MaterialStateProperty.all(Size(200, 50)),
                backgroundColor: MaterialStatePropertyAll(Colors.green)
            ),
            onPressed:  () {
              Navigator.push(
                  context,
                  PageRouteBuilder(
                      pageBuilder: (_, __, ___) => const SupReservation()
                  )
              );
            },
            label: const Text("Supprimer  reservation(s)"),
            icon: Icon(Icons.delete),

          ),
        ],
      ),

    )
    );
  }
}
