import 'package:flutter/material.dart';
import 'package:gestion_hotel/pages/ChambreLibre.dart';
import 'package:gestion_hotel/pages/ChambreOkipe.dart';
class Chambre extends StatelessWidget {
  const Chambre({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(  appBar: AppBar(

      title: const Text(
        "Gestion chambres", ),
      backgroundColor: Colors.green,

      centerTitle: true,
    ),
    body: Center(
    child: Column (
    children: [
    Padding(padding: EdgeInsets.all(20)),
    ElevatedButton.icon(
    style: ButtonStyle(
    fixedSize:  MaterialStateProperty.all(Size(200, 50)),
    backgroundColor: MaterialStatePropertyAll(Colors.green)
    ),
      onPressed:  () {
        Navigator.push(
            context,
            PageRouteBuilder(
                pageBuilder: (_, __, ___) => const ChambreOccupe()
            )
        );
      },
    label: const Text("Chambres occupées"),
    icon: Icon(Icons.remove_red_eye_outlined),

    ), Padding(padding: EdgeInsets.all(25)),
    ElevatedButton.icon(
    style: ButtonStyle(
    fixedSize:  MaterialStateProperty.all(Size(200, 50)),
    backgroundColor: MaterialStatePropertyAll(Colors.green)
    ),
      onPressed:  () {
        Navigator.push(
            context,
            PageRouteBuilder(
                pageBuilder: (_, __, ___) => const ChambreLibre()
            )
        );
      },
    label: const Text("Chambres Libres"),
    icon: Icon(Icons.remove_red_eye_outlined),

    )
    ],
    ),)
    );
  }
}