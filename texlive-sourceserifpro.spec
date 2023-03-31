Name:		texlive-sourceserifpro
Version:	54512
Release:	2
Summary:	Use SourceSerifPro with TeX(-alike) systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sourceserifpro
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourceserifpro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sourceserifpro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides Source Serif Pro for LaTeX. It includes
both Type1 and OpenType fonts and selects the latter when using
XeLaTeX or LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/sourceserifpro
%{_texmfdistdir}/fonts/vf/adobe/sourceserifpro
%{_texmfdistdir}/fonts/type1/adobe/sourceserifpro
%{_texmfdistdir}/fonts/tfm/adobe/sourceserifpro
%{_texmfdistdir}/fonts/opentype/adobe/sourceserifpro
%{_texmfdistdir}/fonts/map/dvips/sourceserifpro
%{_texmfdistdir}/fonts/enc/dvips/sourceserifpro
%doc %{_texmfdistdir}/doc/latex/sourceserifpro

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
