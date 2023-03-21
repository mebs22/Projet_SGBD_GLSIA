import 'package:flutter/material.dart';
class ChambreLibre extends StatelessWidget {
  const ChambreLibre({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "CHAMBRES LIBRES", ),
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
