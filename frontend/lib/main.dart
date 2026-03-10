import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const YasamIziApp());
}

class YasamIziApp extends StatelessWidget {
  const YasamIziApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Yaşamİzi',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF008080), // Teal
          primary: const Color(0xFF008080),
          secondary: const Color(0xFF000080), // Navy
        ),
        useMaterial3: true,
        appBarTheme: const AppBarTheme(
          backgroundColor: Color(0xFF008080),
          foregroundColor: Colors.white,
          centerTitle: true,
          elevation: 2,
        ),
        cardTheme: CardThemeData(
          elevation: 4,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}
