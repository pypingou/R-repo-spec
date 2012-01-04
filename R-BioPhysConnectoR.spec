%global packname  BioPhysConnectoR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.7
Release:          1%{?dist}
Summary:          BioPhysConnectoR

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-snow R-matrixcalc 

BuildRequires:    R-devel tex(latex) R-snow R-matrixcalc 

%description
Utilities and functions to investigate the relation between biomolecular
structures, their interactions, and the evolutionary information revealed
in sequence alignments of these molecules.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.7-1
- initial package for Fedora