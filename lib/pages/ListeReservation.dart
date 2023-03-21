import 'package:flutter/material.dart';

class ListeReservation extends StatelessWidget {
  const ListeReservation({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "LISTE RESERVATIONS", ),
        backgroundColor: Colors.green,

        centerTitle: true,

      ),
      body: Center(
        child: ListView(
          children: [

          ],
        ),
      ),
    );
  }
}
