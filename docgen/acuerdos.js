const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType, VerticalAlign,
} = require("docx");

const CONTENT_W = 9360; // US Letter, 1" margins
const border = { style: BorderStyle.SINGLE, size: 1, color: "999999" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 80, bottom: 80, left: 120, right: 120 };

// --- student roster ---
const STUDENTS = [
  "José Eduardo Brito Celis",
  "José Francisco Escalona Villafaña",
  "Ian Miguel González Ortega",
  "Dana Gisel Reyes López",
  "Carlos Zilli Montero",
];
const PROFESOR = "Eduardo Heredia Contreras";

function headerCell(text, width) {
  return new TableCell({
    borders, width: { size: width, type: WidthType.DXA }, margins: cellMargins,
    shading: { fill: "1F3864", type: ShadingType.CLEAR }, verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ children: [new TextRun({ text, bold: true, color: "FFFFFF", size: 20 })] })],
  });
}
function bodyCell(text, width, align) {
  return new TableCell({
    borders, width: { size: width, type: WidthType.DXA }, margins: { top: 140, bottom: 140, left: 120, right: 120 },
    children: [new Paragraph({ alignment: align || AlignmentType.LEFT, children: [new TextRun({ text: text || "", size: 20 })] })],
  });
}

const cols = [620, 4740, 4000]; // #, Nombre, Firma  (sum 9360)
const rosterRows = [
  new TableRow({ tableHeader: true, children: [
    headerCell("#", cols[0]), headerCell("Nombre del alumno", cols[1]),
    headerCell("Firma", cols[2]),
  ]}),
];
STUDENTS.forEach((name, idx) => {
  rosterRows.push(new TableRow({ children: [
    bodyCell(String(idx + 1), cols[0], AlignmentType.CENTER), bodyCell(name, cols[1]),
    bodyCell("", cols[2]),
  ]}));
});

// --- evaluation scheme table ---
const evalCols = [3200, 1400, 4760];
function evalHeader(t, w) {
  return new TableCell({ borders, width: { size: w, type: WidthType.DXA }, margins: cellMargins,
    shading: { fill: "1F3864", type: ShadingType.CLEAR },
    children: [new Paragraph({ children: [new TextRun({ text: t, bold: true, color: "FFFFFF", size: 20 })] })] });
}
function evalCell(t, w, bold, align) {
  return new TableCell({ borders, width: { size: w, type: WidthType.DXA }, margins: cellMargins,
    children: [new Paragraph({ alignment: align || AlignmentType.LEFT, children: [new TextRun({ text: t, bold: !!bold, size: 20 })] })] });
}
const evalRows = [
  new TableRow({ tableHeader: true, children: [evalHeader("Componente", evalCols[0]), evalHeader("Peso", evalCols[1]), evalHeader("Condiciones", evalCols[2])] }),
  new TableRow({ children: [evalCell("Exámenes", evalCols[0], true), evalCell("40%", evalCols[1], true, AlignmentType.CENTER), evalCell("Mínimo 1, máximo 2, al final del curso. Pueden ser orales o escritos. Solo sobre temas vistos en clase o asignados.", evalCols[2])] }),
  new TableRow({ children: [evalCell("Trabajo de investigación", evalCols[0], true), evalCell("30%", evalCols[1], true, AlignmentType.CENTER), evalCell("En equipo. Con portada, índice, introducción y bibliografía. Se entrega en la plataforma/módulo, en 3 formatos, en la fecha y hora indicadas.", evalCols[2])] }),
  new TableRow({ children: [evalCell("Participación", evalCols[0], true), evalCell("20%", evalCols[1], true, AlignmentType.CENTER), evalCell("Se inicia con el 20% completo. Cada respuesta incorrecta a una pregunta al azar resta 2%.", evalCols[2])] }),
  new TableRow({ children: [evalCell("Asistencia", evalCols[0], true), evalCell("10%", evalCols[1], true, AlignmentType.CENTER), evalCell("Requiere 100% de asistencia. Una sola falta hace perder este 10%.", evalCols[2])] }),
  new TableRow({ children: [evalCell("TOTAL", evalCols[0], true), evalCell("100%", evalCols[1], true, AlignmentType.CENTER), evalCell("", evalCols[2])] }),
];

function rule(text) {
  return new Paragraph({ numbering: { reference: "rules", level: 0 }, spacing: { after: 80 },
    children: [new TextRun({ text, size: 22 })] });
}

const doc = new Document({
  numbering: { config: [{ reference: "rules", levels: [{ level: 0, format: "decimal", text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 460, hanging: 320 } } } }] }] },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: "1F3864" }, paragraph: { spacing: { before: 220, after: 120 }, outlineLevel: 0 } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } } },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: "UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO", bold: true, size: 22 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [new TextRun({ text: "Facultad de Contaduría y Administración — SUAyED", size: 20 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [new TextRun({ text: "Asignatura: Finanzas (2632)", size: 20 })] }),

      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "ACTA DE ACUERDOS — ESQUEMA DE EVALUACIÓN", bold: true, size: 30, color: "1F3864" })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: [
        new TextRun({ text: "Profesor: " + PROFESOR, size: 22 }),
        new TextRun({ text: "        Fecha: 23 de junio de 2026", size: 22 }),
      ]}),

      new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: "Los integrantes del grupo y el profesor acordaron, de manera conjunta y conforme al reglamento institucional, el siguiente esquema de evaluación y las reglas de operación del curso. Este documento se firma para dejar constancia transparente de dichos acuerdos.", size: 22 })] }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("1. Esquema de evaluación")] }),
      new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: evalCols, rows: evalRows }),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("2. Reglas del curso")] }),
      rule("Horario: 7:00 a 10:00 p.m. Tolerancia de entrada de 20 minutos; a partir del minuto 21 no se permite el acceso y cuenta como falta."),
      rule("Asistencia mínima reglamentaria del 80%. No cumplirla causa baja automática, independientemente de la calificación obtenida."),
      rule("Calificación mínima aprobatoria: 6.0. Una calificación de 5.5 no se redondea a 6.0."),
      rule("Exámenes al final del curso; pueden ser orales o escritos, teóricos o prácticos. Solo se pregunta sobre temas vistos en clase o previamente asignados."),
      rule("Trabajo de investigación en equipo, con los requisitos de formato indicados, entregado en la plataforma en la fecha y hora establecidas."),
      rule("Exposición: mínimo dos, obligatorias, sobre el mismo tema del trabajo de investigación."),

      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("3. Conformidad de los integrantes del grupo")] }),
      new Paragraph({ spacing: { after: 140 }, children: [new TextRun({ text: "Los abajo firmantes manifestamos conocer y estar de acuerdo con el esquema de evaluación y las reglas aquí descritas.", size: 22 })] }),
      new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: cols, rows: rosterRows }),

      new Paragraph({ spacing: { before: 400 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "______________________________________", size: 22 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [new TextRun({ text: "Profesor: " + PROFESOR, size: 20 })] }),
    ],
  }],
});

Packer.toBuffer(doc).then((b) => { fs.writeFileSync("Acuerdos_Finanzas_2632.docx", b); console.log("WROTE Acuerdos_Finanzas_2632.docx"); });
