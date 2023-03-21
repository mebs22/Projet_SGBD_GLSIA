// ignore_for_file: prefer_const_literals_to_create_immutables

import 'package:flutter/material.dart';
class Facture extends StatelessWidget {
  const Facture({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
      title: const Text(
        "Factures", ),
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
