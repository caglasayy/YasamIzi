// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter_test/flutter_test.dart';

import 'package:yasamizi/main.dart';

void main() {
  testWidgets('Dashboard module test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const YasamIziApp());

    // Verify that our app bar title is there.
    expect(find.text('Yaşamİzi'), findsOneWidget);

    // Verify that dashboard cards are there.
    expect(find.text('İlaç Takibi'), findsOneWidget);
    expect(find.text('Alerji Kalkanı'), findsOneWidget);
    expect(find.text('Yaşam Koçu'), findsOneWidget);
  });
}
