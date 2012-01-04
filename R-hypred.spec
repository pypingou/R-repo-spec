%global packname  hypred
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Simulation of genomic data in applied genetics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The package is intended for simulating high density genomic data. Its
focus is on genomic applications in applied genetics,namely hybrid
breeding, but it should be usefull in related fields as well.  The meiosis
is simulated under a count-location model, the genetic structure can
include additive and dominance effects. The low level nature of the
package provides great flexibility in creating all kinds of populations.

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
%doc %{rlibdir}/hypred/html
%doc %{rlibdir}/hypred/DESCRIPTION
%doc %{rlibdir}/hypred/doc
%doc %{rlibdir}/hypred/CITATION
%{rlibdir}/hypred/R
%{rlibdir}/hypred/NAMESPACE
%{rlibdir}/hypred/INDEX
%{rlibdir}/hypred/help
%{rlibdir}/hypred/libs
%{rlibdir}/hypred/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora