%global packname  NMOF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.20.0
Release:          1%{?dist}
Summary:          Numerical Methods and Optimization in Finance

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.20-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions, examples and data from the book 'Numerical Methods and
Optimization in Finance' by M. Gilli, D. Maringer and E. Schumann. The
package contains, in particular, several implementations of optimisation
heuristics (for instance, Differential Evolution, Genetic Algorithms and
Threshold Accepting).

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
%doc %{rlibdir}/NMOF/NEWS
%doc %{rlibdir}/NMOF/html
%doc %{rlibdir}/NMOF/DESCRIPTION
%doc %{rlibdir}/NMOF/doc
%doc %{rlibdir}/NMOF/CITATION
%{rlibdir}/NMOF/data
%{rlibdir}/NMOF/R
%{rlibdir}/NMOF/unitTests
%{rlibdir}/NMOF/INDEX
%{rlibdir}/NMOF/NEWS.Rd
%{rlibdir}/NMOF/NAMESPACE
%{rlibdir}/NMOF/help
%{rlibdir}/NMOF/Meta
%{rlibdir}/NMOF/NMOFex

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.20.0-1
- initial package for Fedora