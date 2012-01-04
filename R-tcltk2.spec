%global packname  tcltk2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.5
Release:          1%{?dist}
Summary:          Tcl/Tk Additions

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
A series of additional Tcl commands and Tk widgets with style and various
functions (under Windows: DDE exchange, access to the registry and icon
manipulation) to supplement the tcltk package

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
%doc %{rlibdir}/tcltk2/DESCRIPTION
%doc %{rlibdir}/tcltk2/html
%doc %{rlibdir}/tcltk2/NEWS
%doc %{rlibdir}/tcltk2/CITATION
%{rlibdir}/tcltk2/po
%{rlibdir}/tcltk2/gui
%{rlibdir}/tcltk2/NAMESPACE
%{rlibdir}/tcltk2/tklibs
%{rlibdir}/tcltk2/INDEX
%{rlibdir}/tcltk2/Fonts.txt
RPM build errors:
%{rlibdir}/tcltk2/help
%{rlibdir}/tcltk2/R
%{rlibdir}/tcltk2/Meta
%{rlibdir}/tcltk2/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.5-1
- initial package for Fedora