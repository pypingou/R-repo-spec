%global packname  tikzDevice
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          A Device for R Graphics Output in PGF/TikZ Format

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-filehash 

BuildRequires:    R-devel tex(latex) R-filehash 

%description
The TikZ device enables LaTeX-ready output from R graphics functions. This
is done by producing code that can be understood by the TikZ graphics
language. All text in a graphic output with the tikz() function will can
be typeset by LaTeX and therefore will match whatever fonts are currently
used in the document. This also means that LaTeX mathematics can be
typeset directly into labels and annotations!  Graphics produced this way
can also be annotated with custom TikZ commands.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/tikzDevice/html
%doc %{rlibdir}/tikzDevice/DESCRIPTION
%doc %{rlibdir}/tikzDevice/doc
%{rlibdir}/tikzDevice/tests
%{rlibdir}/tikzDevice/R
%{rlibdir}/tikzDevice/GIT_VERSION
%{rlibdir}/tikzDevice/INDEX
%{rlibdir}/tikzDevice/help
%{rlibdir}/tikzDevice/libs
%{rlibdir}/tikzDevice/NAMESPACE
%{rlibdir}/tikzDevice/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora