%global packname  MSToolkit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          The MSToolkit library for clinical trial design

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
MSToolkit library for evaluating clinical trial design and analysis
operating characteristics through simulation.

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
%doc %{rlibdir}/MSToolkit/html
%doc %{rlibdir}/MSToolkit/DESCRIPTION
%{rlibdir}/MSToolkit/R
%{rlibdir}/MSToolkit/Runit
%{rlibdir}/MSToolkit/NAMESPACE
%{rlibdir}/MSToolkit/ECTD.ini
RPM build errors:
%{rlibdir}/MSToolkit/systemTest
%{rlibdir}/MSToolkit/COPYRIGHT
%{rlibdir}/MSToolkit/demo
%{rlibdir}/MSToolkit/sasAnalysis.sas
%{rlibdir}/MSToolkit/Meta
%{rlibdir}/MSToolkit/INDEX
%{rlibdir}/MSToolkit/help
%{rlibdir}/MSToolkit/exec

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora