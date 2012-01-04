%global packname  TGUITeaching
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.13
Release:          1%{?dist}
Summary:          Teaching GUI - prototype

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-TGUICore R-tcltk R-tkrplot R-lattice R-car 

BuildRequires:    R-devel tex(latex) R-TGUICore R-tcltk R-tkrplot R-lattice R-car 

%description
Teaching-GUI prototype, for creating TGUI content to enhance classroom
teaching supported by TGUI. A Graphical User Interface to enhance and
support modern teaching methods in an interactive way.

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
%doc %{rlibdir}/TGUITeaching/doc
%doc %{rlibdir}/TGUITeaching/DESCRIPTION
%doc %{rlibdir}/TGUITeaching/html
%doc %{rlibdir}/TGUITeaching/CITATION
%{rlibdir}/TGUITeaching/Meta
%{rlibdir}/TGUITeaching/NAMESPACE
%{rlibdir}/TGUITeaching/help
%{rlibdir}/TGUITeaching/INDEX
%{rlibdir}/TGUITeaching/R
%{rlibdir}/TGUITeaching/etc

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.13-1
- initial package for Fedora