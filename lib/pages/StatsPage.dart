import 'package:flutter/material.dart';
class Stats extends StatelessWidget {
  const Stats({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(  appBar: AppBar(

      title: const Text(
        "Statistiques de l'hotel :", ),
      backgroundColor: Colors.green,

      centerTitle: true,
    ),);
  }
}

